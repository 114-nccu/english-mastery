"""關卡 3：簡報內容檢查（HTML 產生後跑；也可對逐頁稿 HTML 跑）

用法：python scripts/check_deck.py runs/toeic-deck/deck.html wiki/sources [scripts/banned.txt]
HTML 約定：每頁 <section class="slide" data-claims="S1-C01,S6-C02">
            封面/參考資料頁加 data-type="title" 或 data-type="refs" 免檢
            不想被數字檢查的片段（例如頁碼）放在 class="nocheck" 的元素內
檢查：
  - 每個內容頁有 data-claims，ID 都存在
  - 頁面上的有意義數字（≥2 位數、小數、百分比）出現在被引用的 claim 內
  - 沒有禁用詞
  - 輸出 Wiki ↔ 簡報 對照表到 mapping.md（交件可直接用）
"""
import sys
from html.parser import HTMLParser
from pathlib import Path
from common import load_cards, significant_numbers, load_banned


class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides, self.cur, self.depth = [], None, 0
        self.skip_depth = 0
        self.title_pending = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        if tag == "section" and "slide" in classes and self.cur is None:
            self.cur = {"claims": a.get("data-claims"), "type": a.get("data-type", "content"),
                        "text": [], "title": ""}
            self.depth = 1
            return
        if self.cur is not None:
            if tag not in ("br", "img", "hr", "meta", "link", "input"):
                self.depth += 1
                if self.skip_depth or "nocheck" in classes or tag in ("script", "style"):
                    self.skip_depth += 1
            if tag in ("h1", "h2") and not self.cur["title"]:
                self.title_pending = True

    def handle_endtag(self, tag):
        if self.cur is None:
            return
        self.depth -= 1
        if self.skip_depth:
            self.skip_depth -= 1
        if tag in ("h1", "h2"):
            self.title_pending = False
        if self.depth == 0:
            self.slides.append(self.cur)
            self.cur = None

    def handle_data(self, data):
        if self.cur is None:
            return
        if self.title_pending:
            self.cur["title"] += data.strip()
        if not self.skip_depth:
            self.cur["text"].append(data)


def main(deck, src, banned_path):
    claims, metas = load_cards(src)
    banned = load_banned(banned_path)
    p = SlideParser()
    p.feed(Path(deck).read_text(encoding="utf-8"))
    problems, rows = [], []
    if not p.slides:
        problems.append('找不到 <section class="slide">，請確認 HTML 結構')
    for i, s in enumerate(p.slides, 1):
        text = " ".join(" ".join(s["text"]).split())
        label = f"第 {i} 頁「{s['title'][:20]}」"
        for w in banned:
            if w in text:
                problems.append(f"{label} 出現禁用詞「{w}」")
        if s["type"] in ("title", "refs"):
            rows.append((i, s["title"], "（免檢）"))
            continue
        ids = [x.strip() for x in (s["claims"] or "").split(",") if x.strip()]
        rows.append((i, s["title"], ", ".join(ids) or "—"))
        if not ids:
            problems.append(f"{label} 沒有 data-claims")
            continue
        missing = [x for x in ids if x not in claims]
        for x in missing:
            problems.append(f"{label} 引用的 {x} 不存在於 Wiki")
        if any(x.startswith("AI-") for x in ids) and not any(k in text for k in ("AI 建議", "AI建議", "教學示例")):
            problems.append(f"{label} 引用 AI 建議（AI-xx），頁面上卻沒有標示「AI 建議」或「教學示例」")
        source_text = " ".join(claims[x]["head"] + " " + claims[x]["body"]
                               for x in ids if x in claims)
        allowed = significant_numbers(source_text)
        for n in sorted(significant_numbers(text) - allowed):
            problems.append(f"{label} 數字「{n}」在引用的 claim 裡找不到")
    out = Path(deck).with_name("mapping.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("| 頁 | 標題 | 對應 Wiki claim |\n|---|---|---|\n")
        for r in rows:
            f.write(f"| {r[0]} | {r[1]} | {r[2]} |\n")
    print(f"# check_deck：{len(p.slides)} 頁；對照表已寫入 {out}")
    if problems:
        print(f"FAIL（{len(problems)} 項）")
        for x in problems:
            print("-", x)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    a = sys.argv
    sys.exit(main(a[1], a[2] if len(a) > 2 else "wiki/sources",
                  a[3] if len(a) > 3 else "scripts/banned.txt"))
