"""共用工具：讀取證據卡。

證據卡格式（wiki/sources/S6.md）：
---
id: S6
doi: 10.1007/s10648-025-10068-6
...
---
### S6-C01 [FINDING] p.12
內容……
限制：……
"""
import re
from pathlib import Path

CLAIM_HEAD = re.compile(r"^###\s+(S\d+-C\d+|AI-\d+)\s*(.*)$", re.M)


def parse_front_matter(text):
    meta = {}
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta


def load_cards(sources_dir):
    """回傳 (claims, metas)。claims: {claim_id: {'head':..., 'body':..., 'file':...}}
    也會讀取同層 concepts/ 裡的 AI-xx 條目（AI 教學建議）。"""
    claims, metas = {}, {}
    files = sorted(Path(sources_dir).glob("S*.md"))
    concepts = Path(sources_dir).parent / "concepts"
    extra = sorted(concepts.glob("*.md")) if concepts.exists() else []
    for f in files + extra:
        text = f.read_text(encoding="utf-8")
        if f in files:
            metas[f.stem] = parse_front_matter(text)
        heads = list(CLAIM_HEAD.finditer(text))
        for i, h in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            claims[h.group(1)] = {
                "head": h.group(2).strip(),
                "body": text[h.end():end].strip(),
                "file": f.name,
            }
    return claims, metas


NUM = re.compile(r"\d+(?:[.,]\d+)?%?")


def significant_numbers(text):
    """只檢查「有意義」的數字：兩位數以上、含小數或百分比。
    單一位數（Part 1、第 3 頁）太常見，略過。"""
    out = set()
    for n in NUM.findall(text):
        core = n.rstrip("%").replace(",", "")
        if len(core.replace(".", "")) >= 2 or "." in core or n.endswith("%"):
            out.add(n.replace(",", ""))
    return out


def load_banned(path):
    p = Path(path)
    if not p.exists():
        return []
    return [w.strip() for w in p.read_text(encoding="utf-8").splitlines()
            if w.strip() and not w.startswith("#")]
