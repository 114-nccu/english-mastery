# English Mastery｜截至 2026-11-23 的專案狀態

| 階段 | 狀態 | 證據與限制 |
|---|---|---|
| N0 需求訪談 | 完成 | 本人 10 題回答與確認；公開去識別化摘要 `interview-summary-public.md` |
| N1 來源查核 | 基本查核完成，全文封存未齊 | 8 份來源書目／頁面及核心 Claim 核對；S6 摘要限定；`raw/` 尚未完整封存 |
| N2 Wiki Ingest | 完成 | S1–S8 共 8 份來源卡、19 條來源 Claim＋2 條 AI 建議；格式檢查 PASS |
| N3 大綱 | 完成 | 12 頁；`check_outline.py` PASS |
| N4 逐頁稿 | 完成 | `check_deck.py` 初輪 FAIL、局部修正後 PASS；Round 2 PASS |
| N5 語意審查 | 部分完成 | 已使用外部審查意見修正；新對話完全獨立 AI 審查尚未完成 |
| N6 HTML 渲染／互動 | 完成並附限制 | 外部審查者回報完整 Chromium 12 頁無溢出；本站測試過程與沙盒限制詳見 Round 2 報告 |
| N7 公開發布 | **完成** | 網站 https://114-nccu.github.io/english-mastery/；原始碼 https://github.com/114-nccu/english-mastery |
| 最終作業提交 | 待本人完成 | 仍須本人確認反思、標題資料與學校系統送出 |

請以 `runs/round1/report.md`、`runs/round2/report.md` 和 `runs/round2/content-audit-2026-11-23.md` 區分不同日期／環境的驗證，不能把轉述的測試當成助手在本機親自執行的結果。

**Prompt 修訂狀態（2026-11-23）**：已在 N3 大綱規則新增術語定義 Claim 檢查、N5 審查新增視覺量化誤導檢查，見 `prompts/03-outline.md`、`prompts/05-independent-review.md`；此為事後流程改善，**尚未使用新 Prompt 重跑完整 N3→N5**。
