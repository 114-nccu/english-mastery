# N3 查詢 Wiki → 大綱

---

請只根據 `wiki/` 的內容，為「English Mastery——用學習科學準備多益 L&R」製作教學簡報大綱，存成 `runs/round<N>/outline.md`。

讀者：對多益和學習科學都不熟的大學生。
建議結構請參考 README 第 4 節；如果你判斷要調整，請說明理由。

格式（每頁一段）：
```
## P2 多益 L&R 長什麼樣子
type: content
goal: 讀完知道題數、時間、7 個 Part
claims: S1-C01, S1-C02
points:
- ……
```

規則：
1. 每個內容頁至少列一個 Wiki 裡**確實存在的** claim ID。
2. 如果某頁需要的內容在 Wiki 裡找不到，**不要寫那一頁**。請在檔案最後列出「缺口清單」，然後停下來。
3. 每一篇來源至少要被一頁使用。
4. 封面寫 `type: title`，參考資料頁寫 `type: refs`。
5. 每個需要讓初學者理解的術語（例如泛聽、精聽），必須有一條可追溯、能提供**概念定義**的 Claim；只有效果研究、沒有定義的術語，應列入缺口清單並停止生成該頁，不得靠 AI 常識補齊。

---

**跑完腳本**：`python scripts/check_outline.py runs/round<N>/outline.md wiki/sources`。出現「依規則停止」時，回到 N2 補資料，或刪掉那一頁。
