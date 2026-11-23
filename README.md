# English Mastery｜用學習科學準備多益 L&R

> **本版已實際產生 Wiki 與 HTML 簡報。** 這不是只有流程和工具的空白工具包。來源在線上查閱後做成證據卡，但原文 PDF 未全部在此沙盒下載；S6 僅公開摘要。網站尚未外部部署。請見 `STATUS.md`。

## 給老師看的入口

1. `docs/index.html` — 12 頁可本機開啟的教學 HTML，左右鍵與畫面按鈕翻頁、兩個簡單問答。
2. `wiki/index.md` — 8 篇來源卡、19 條有出處的來源 Claim、2 條 AI 教學示例。
3. `runs/round2/mapping.md` — **最新版** HTML 每頁與 Wiki Claim 的對照。Round 1 原始版仍保留。
4. `workflow/graph.md` — N0–N7 Graph、檢查節點、Loop 退回和停止規則。
5. `runs/round1/report.md` 與 `runs/round2/report.md` — 第一輪及外部回饋後修正版的實際檢查紀錄。
6. `submission-draft.md` — 六項作業繳交內容的草稿；不能在補齊網址前原封提交。

## 實際執行檢查

在專案根目錄執行：

```bash
python scripts/check_cards.py wiki/sources
python scripts/check_outline.py runs/round2/outline.md wiki/sources
python scripts/check_deck.py runs/round2/deck.html wiki/sources scripts/banned.txt
python scripts/check_render.py runs/round2/deck.html
python tests/interaction_check.py
```

`check_render` 需要 Playwright 與 Chromium；出現 `LIMITATION` 時只是受限的 inline HTML 檢查，不能冒稱完整網站驗收。`interaction_check.py` 也使用 `set_content`，只測互動 JS、非公開站台整體運作。

## GitHub Pages 發布

將本專案放在 GitHub 儲存庫。GitHub Pages 設定：Deploy from a branch → `main` → `/docs`。由於 `docs/index.html` 為單檔 HTML，不需要打包工具或外部框架。請手動測試公開網址、相對資源與互動功能後再填進 `submission-draft.md`。

**隱私與版權：** `interview-log.md` 與 `raw/` 已加入 `.gitignore`；不要把私人訪談原始檔和來源 PDF 直接公開上傳。`interview-summary-public.md` 可作為去識別化訪談成果。

## 原始來源及未完成事項

- `sources.md`：書目與原始網址
- `n1-raw-manifest.md`：逐筆存取狀態與未保存檔案
- `tests/manual_content_review.md`：內部內容對照，**不是**獨立新對話審查
- `workflow/independent-review-prompt.md`：獨立 AI 審查專用 Prompt

本次完成的是工作環境裡可驗證的部分；尚未宣稱有外部站台、使用者本人 Git 提交或獨立 AI 審查結果。

## Round 2 追加來源與版面修正（2026-11-23）

- S8：The Open University OpenLearn 開放課程的泛聽／精聽教學定義，非成效實驗。
- P4 補足兩種聽法的定義；P6 將未支持的因素和 AI 建議區分；P7 用定性標籤取代沒有來源的百分比長條。
- 桌面版導覽與頁碼分離；手機改為可捲動閱讀模式。詳見 `runs/round2/review-and-fixes.md`。
