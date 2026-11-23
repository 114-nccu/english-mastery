"""關卡 4：渲染檢查（需要 Playwright）

安裝：pip install playwright && playwright install chromium
用法：python scripts/check_render.py runs/toeic-deck/deck.html [--links]
檢查：
  - 每個 .slide 內容是否超出頁面框（文字溢出）
  - 每頁截圖存到 screenshots/（交件時可當執行紀錄）
  - --links：檢查外部連結（需要網路）
"""
import os
import shutil
import sys
import urllib.request
from pathlib import Path
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.parse import quote

@contextmanager
def local_http(directory):
    # Serving over loopback avoids file:// restrictions in hardened browsers.
    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, *_):
            pass
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(directory)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server.server_port
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


from playwright.sync_api import sync_playwright, Error as PlaywrightError

SHOW_ALL = """
.slide{display:block!important;position:relative!important;visibility:visible!important;
opacity:1!important;transform:none!important;margin:0 0 20px 0!important}
"""

JS = """
() => [...document.querySelectorAll('.slide')].map((s, i) => {
  const r = s.getBoundingClientRect();
  let worst = 0;
  s.querySelectorAll('*').forEach(el => {
    const b = el.getBoundingClientRect();
    if (b.width === 0 && b.height === 0) return;
    worst = Math.max(worst, b.bottom - r.bottom, b.right - r.right);
  });
  return {i: i + 1, scroll: s.scrollHeight - s.clientHeight, overflow: Math.round(worst),
          title: (s.querySelector('h1,h2')||{}).textContent || ''};
})
"""


def main(deck, check_links):
    deck = Path(deck).resolve()
    shots = deck.parent / "screenshots"
    shots.mkdir(exist_ok=True)
    problems, links = [], []
    with sync_playwright() as p:
        # Prefer Playwright managed browser; optionally use OS browser when absent.
        # Override with CHROMIUM_EXECUTABLE=/path/to/chromium.
        executable = os.environ.get("CHROMIUM_EXECUTABLE")
        if not executable:
            from pathlib import Path as _Path
            cache = _Path.home() / ".cache/ms-playwright"
            if not cache.exists() or not list(cache.glob("chromium_headless_shell-*")):
                executable = shutil.which("chromium") or shutil.which("google-chrome")
        launch_kwargs = {"executable_path": executable} if executable else {}
        b = p.chromium.launch(**launch_kwargs)
        page = b.new_page(viewport={"width": 1280, "height": 720})
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        with local_http(deck.parent) as port:
            try:
                page.goto(f"http://127.0.0.1:{port}/{quote(deck.name)}")
            except PlaywrightError as e:
                if "ERR_BLOCKED_BY_ADMINISTRATOR" not in str(e):
                    raise
                # Sandbox-only fallback. Relative assets will not load: this
                # confirms inline HTML/CSS behavior, NOT a full deployment test.
                print("LIMITATION: browser navigation blocked; testing inline HTML via set_content only")
                page.close()
                page = b.new_page(viewport={"width": 1280, "height": 720})
                page.on("pageerror", lambda e: errors.append(str(e)))
                page.set_content(deck.read_text(encoding="utf-8"), wait_until="domcontentloaded")
        page.add_style_tag(content=SHOW_ALL)
        page.wait_for_timeout(300)
        results = page.evaluate(JS)
        if not results:
            problems.append('找不到 .slide 元素')
        for r in results:
            if r["overflow"] > 2 or r["scroll"] > 2:
                problems.append(f"第 {r['i']} 頁「{r['title'][:20]}」溢出 {max(r['overflow'], r['scroll'])}px")
        for n, el in enumerate(page.query_selector_all(".slide"), 1):
            el.screenshot(path=str(shots / f"slide-{n:02d}.png"))
        for e in errors:
            problems.append(f"JavaScript 錯誤：{e}")
        links = page.eval_on_selector_all("a[href^='http']", "els => els.map(e => e.href)")
        b.close()
    if check_links:
        for url in sorted(set(links)):
            try:
                req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0"})
                code = urllib.request.urlopen(req, timeout=15).status
            except Exception as e:  # noqa
                code = getattr(e, "code", str(e))
            if code != 200:
                problems.append(f"連結 {url} 回傳 {code}（DOI 網站有時會擋程式，請人工點開確認）")
    print(f"# check_render：{len(results)} 頁；截圖存於 {shots}")
    if problems:
        print(f"FAIL（{len(problems)} 項）")
        for x in problems:
            print("-", x)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], "--links" in sys.argv))
