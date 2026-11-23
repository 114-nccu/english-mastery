"""關卡 2：大綱覆蓋率檢查（逐頁稿之前跑）

用法：python scripts/check_outline.py runs/toeic-deck/outline.md wiki/sources
大綱格式：每頁一個標題，標題下一行寫 claims：
  ## P3 TOEIC 考什麼
  claims: S1-C01, S1-C02
  type: content          （title / refs 頁可寫 type: title 或 type: refs，免檢）
檢查：
  - 每個內容頁至少一個 claim ID，而且 ID 存在
  - 每篇來源至少被一頁使用（否則等於 ingest 了卻沒用）
  - 有頁面找不到 claim → 依停止規則：不往下生成
"""
import re
import sys
from common import load_cards


def main(outline, src):
    claims, metas = load_cards(src)
    text = open(outline, encoding="utf-8").read()
    pages = re.split(r"^##\s+", text, flags=re.M)[1:]
    problems, used = [], set()
    for p in pages:
        title = p.splitlines()[0].strip()
        ptype = re.search(r"^type:\s*(\S+)", p, re.M)
        if ptype and ptype.group(1) in ("title", "refs"):
            continue
        m = re.search(r"^claims:\s*(.*)$", p, re.M)
        ids = [x.strip() for x in (m.group(1).split(",") if m else []) if x.strip()]
        if not ids:
            problems.append(f"[{title}] 沒有任何 claim → 依規則停止，先補 Wiki")
        for i in ids:
            if i not in claims:
                problems.append(f"[{title}] claim {i} 不存在於 Wiki")
            used.add(i.split("-")[0])
    for sid in metas:
        if sid not in used:
            problems.append(f"來源 {sid} 沒有被任何一頁使用")
    print(f"# check_outline：{len(pages)} 頁")
    if problems:
        print(f"FAIL（{len(problems)} 項）")
        for x in problems:
            print("-", x)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "wiki/sources"))
