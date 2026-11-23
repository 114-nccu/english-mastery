"""關卡 1：證據卡檢查（ingest 之後立刻跑）

用法：python scripts/check_cards.py wiki/sources
檢查：
  - 每張卡有必要 metadata
  - 每條 claim 標題有類型標籤 [FACT|FINDING|AI-EXPLAIN|AI-ADVICE] 和原文頁碼 p.xx
  - FINDING 類 claim 有「限制：」
  - DOI 或 url 至少一個；同一 DOI 不可重複 ingest
回傳碼：0=全過，1=有問題
"""
import re
import sys
from collections import Counter
from common import load_cards

REQUIRED = ["id", "title", "authors", "year", "venue", "type",
            "evidence_level", "is_L2", "is_TOEIC_direct", "retrieved"]
TYPES = {"FACT", "FINDING", "AI-EXPLAIN", "AI-ADVICE"}


def main(src):
    claims, metas = load_cards(src)
    problems = []
    if not metas:
        problems.append(f"{src} 底下找不到 S*.md")
    for sid, meta in metas.items():
        for k in REQUIRED:
            if not meta.get(k):
                problems.append(f"{sid}: 缺 metadata `{k}`")
        if not (meta.get("doi") or meta.get("url")):
            problems.append(f"{sid}: doi 和 url 都沒有")
    dois = Counter(m.get("doi") for m in metas.values() if m.get("doi"))
    for d, c in dois.items():
        if c > 1:
            problems.append(f"DOI 重複 ingest：{d}（{c} 次）")
    per_source = Counter(cid.split("-")[0] for cid in claims)
    for sid in metas:
        if per_source[sid] == 0:
            problems.append(f"{sid}: 沒有任何 claim")
    for cid, c in claims.items():
        if cid.startswith("AI-"):
            continue  # concepts/ 的 AI 建議不在來源卡檢查範圍
        tag = re.search(r"\[([A-Z-]+)\]", c["head"])
        if not tag or tag.group(1) not in TYPES:
            problems.append(f"{cid}: 缺類型標籤 {sorted(TYPES)}")
        if not re.search(r"(p\.\s*\S+|§\s*\S+|節\s*\S+|摘要|abstract)", c["head"], re.I):
            problems.append(f"{cid}: 缺原文位置（p.頁碼、§章節、節 名稱，或「摘要」）")
        if tag and tag.group(1) == "FINDING" and not re.search(r"限制\s*[:：]", c["body"]):
            problems.append(f"{cid}: FINDING 沒寫「限制：」")
        if tag and tag.group(1).startswith("AI-"):
            problems.append(f"{cid}: 來源卡裡不應有 AI 自行解釋，請移到 concepts/")
    for sid, meta in metas.items():
        if meta.get("full_text", "").lower() == "false":
            body = " ".join(c["head"] for k, c in claims.items() if k.startswith(sid + "-"))
            if re.search(r"p\.\s*\d", body):
                problems.append(f"{sid}: full_text=false 卻出現正文頁碼，請改標「摘要」")
    print(f"# check_cards：{len(metas)} 篇來源、{len(claims)} 條 claim")
    if problems:
        print(f"FAIL（{len(problems)} 項）")
        for p in problems:
            print("-", p)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "wiki/sources"))
