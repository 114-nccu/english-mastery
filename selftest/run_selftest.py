"""自我測試：在你的電腦上確認 4 支腳本會「該擋的擋、該過的過」。
用法（在工具包根目錄）：python selftest/run_selftest.py
good/ 每支都應該 PASS（exit 0）；bad/ 每支都應該 FAIL（exit 1）。
check_render 需要先安裝 Playwright；沒裝會標示 SKIP。"""
import subprocess, sys
from pathlib import Path

root = Path(__file__).resolve().parent
scripts = root.parent / "scripts"
ok = True
full = True
for case, expect in (("good", 0), ("bad", 1)):
    d = root / case
    cmds = {
        "check_cards": ["check_cards.py", str(d / "wiki/sources")],
        "check_outline": ["check_outline.py", str(d / "outline.md"), str(d / "wiki/sources")],
        "check_deck": ["check_deck.py", str(d / "deck.html"), str(d / "wiki/sources"), str(scripts / "banned.txt")],
        "check_render": ["check_render.py", str(d / "deck.html")],
    }
    for name, args in cmds.items():
        r = subprocess.run([sys.executable, str(scripts / args[0])] + args[1:],
                           capture_output=True, text=True, cwd=scripts)
        combined = r.stdout + r.stderr
        if name == "check_render" and "No module named 'playwright'" in combined:
            full = False
            print(f"SKIP  {case:4} {name}（未安裝 Playwright；不算完整測試）")
            continue
        limited = name == "check_render" and "LIMITATION:" in combined
        good = r.returncode == expect
        ok &= good
        full &= not limited
        label = "LIMITED" if limited and good else ("OK     " if good else "BAD    ")
        print(f"{label} {case:4} {name}：exit {r.returncode}（預期 {expect}）")
        if limited:
            print("        瀏覽器被限制，改以 set_content 進行部分測試；外部 CSS/JS 未完整驗證")
        if case == "bad" or not good:
            for line in (r.stdout + r.stderr).strip().splitlines()[1:]:
                print("        ", line)
if not ok:
    print("\nFAIL：有腳本行為不符預期，請檢查上面輸出")
    sys.exit(1)
if not full:
    print("\nINCOMPLETE：部分項目為 SKIP 或 LIMITED；不得宣稱完整 8/8 通過")
    sys.exit(2)
print("\n全部 8 項自我測試符合預期（仍不等於真實 Wiki 或正式部署已驗證）")
sys.exit(0)
