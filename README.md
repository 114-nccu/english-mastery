# English Mastery｜用學習科學準備多益 L&R

> 第十週「LLM Wiki → 教學 HTML 簡報」實作成果。2026-11-23 已公開部署；本文記錄可以查證的實際進度，非全部工作均聲稱由使用者本機執行。

## 直接開啟成果

- **HTML 簡報**：https://114-nccu.github.io/english-mastery/ （12 頁；聽力優先、閱讀其次，並包含兩題簡單互動）
- **Wiki**：[`wiki/index.md`](wiki/index.md)；`wiki/sources/S1.md`–`S8.md` 共 **8 份來源卡**、**19 條來源 Claim**，另有 **2 條明確標記的 AI 教學建議**。
- **簡報 ↔ Wiki 對照**：[`runs/round2/mapping.md`](runs/round2/mapping.md)。
- **Graph／Loop**：[`workflow/graph.md`](workflow/graph.md)。
- **流程改進已寫入 Prompt**：[`prompts/03-outline.md`](prompts/03-outline.md) 新增定義來源關卡；[`prompts/05-independent-review.md`](prompts/05-independent-review.md) 新增視覺誤導審查。這是審查後的規格修訂，並未宣稱回溯重跑舊輪次。
- **第一輪檢查**：[`runs/round1/report.md`](runs/round1/report.md)。
- **第二輪修正與檢查**：[`runs/round2/report.md`](runs/round2/report.md)；[`runs/round2/review-and-fixes.md`](runs/round2/review-and-fixes.md)。
- **最終來源抽核／狀態更新**：[`runs/round2/content-audit-2026-11-23.md`](runs/round2/content-audit-2026-11-23.md)。

## 知識庫架構與限制

- S1、S7：ETS 官方測驗／備考資源說明，**不是**教材提升分數的因果證據。
- S2、S3：一般學習科學與記憶研究，對 TOEIC 屬於間接證據。
- S4、S5：第二語言單字學習與大量閱讀研究，不能直接推出特定 TOEIC 提分幅度。
- S6：只根據出版社公開摘要建卡，`full_text: false`，不引用未取得的正文。
- S8：The Open University 公開課程的精聽／泛聽概念定義，**不是**成效研究。
- 原始文獻全文的本機 `raw/` 封存尚未完整完成；本公開儲存庫不散布受版權保護之原始 PDF。

## 真實 Workflow 與測試邊界

- N0：使用者本人回答並確認 10 題需求；公開版以去識別化摘要呈現。
- N1：核對官方來源與研究來源；部分原始 PDF 未本機封存。
- N2–N4：完成 Wiki、Claim 對應、教學大綱與 HTML 草稿。
- N5：收到使用者提供的外部審查意見並於 Round 2 修正；**全新對話、完全獨立的 AI 審查仍未紀錄為完成**。
- N6：工具包的資料結構與版面檢查完成；在 ChatGPT 沙盒中部分 Chromium 測試屬受限模式。另由外部審查者回報在完整 Chromium 環境測試全部通過；公開網站可由外部開啟，使用者回報手機網址已正常開啟。
- N7：GitHub Pages 已公開，儲存庫含 `wiki/`、`runs/`、`workflow/`；正式線上作業送出仍由使用者完成。

## 重跑程式檢查

```bash
python scripts/check_cards.py wiki/sources
python scripts/check_outline.py runs/round2/outline.md wiki/sources
python scripts/check_deck.py runs/round2/deck.html wiki/sources scripts/banned.txt
python scripts/check_render.py runs/round2/deck.html
```

`check_render.py` 需要 Playwright/Chromium；若顯示 LIMITED，不能把該次視為完整的公開站台驗證。

## 隱私與學術誠信

私人 `interview-log.md` 與 `raw/` 原文不得公開。公開的 `interview-summary-public.md` 僅保留需求決策；AI 的建議獨立標註，沒有將研究結果寫成分數保證。最終「反思」請由使用者本人根據真實日誌確認、修訂。
