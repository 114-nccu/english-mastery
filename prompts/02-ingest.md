# N2 Ingest（分組匯入；每篇各自一張卡）

---

請依 AGENTS.md，ingest `raw/<檔名>.pdf`，建立 `wiki/sources/S<編號>.md`。

規則：
1. 只讀這一篇，不要混入其他來源或你自己的知識。
   （依需求 R07 分組匯入：同一組可以在同一次對話裡做，但每篇還是各自一張卡、互不引用。）
2. 格式完全依照 templates/card.md。
3. 每條 claim 標題寫 `### S<編號>-C<兩位數> [FACT 或 FINDING] <位置>`。位置寫 `p.頁碼`，網頁沒有頁碼就寫 `§章節名`。**特別注意 S4 使用 researchmap 早期版 PDF 時，必須在 front matter 寫 `page_basis: researchmap 早期版 PDF`，並統一採用 `§章節名`，不得混用正式期刊頁碼。**
   **沒有全文**（例如 S6）時，front matter 加 `full_text: false`，位置一律寫「摘要」，只能寫摘要裡有的內容。
   AGENTS.md 要求的「適用性」和「直接／間接證據」寫在 claim 內文，例如「適用性：…」「證據：間接（非多益）」。
4. FINDING 一定要寫「限制：」，內容是原文作者自己提到的限制，或研究設計上的限制（樣本、有無對照組、追蹤時間）。
5. 數字照原文抄寫，不要四捨五入或換算。
6. 標明 `is_L2` 和 `is_TOEIC_direct`。
7. 找不到的資訊寫「原文未提供」，不要補。
8. 完成後更新 `wiki/index.md` 和 `wiki/log.md`（日期、檔名、DOI）。

完成後，我會執行 `python scripts/check_cards.py wiki/sources`。

---

**跑完腳本**：FAIL 就把腳本輸出貼回給 AI，只修列出的問題，最多 2 輪。每篇都通過就 commit。

## AI 教學建議（入門備考規劃）放哪裡
寫在 `wiki/concepts/study-plan.md`，格式：
```
### AI-01 [AI-ADVICE] 依據 S3-C01, S4-C02
（建議內容）
```
「依據」只是說明這個建議參考了哪些研究，不代表研究證實這個建議有效。
