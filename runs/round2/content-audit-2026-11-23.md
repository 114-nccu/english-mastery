# English Mastery｜交件前內容與來源複核（2026-11-23）

## 審查身分與範圍

這是由**先前參與專案製作的 ChatGPT 助理**進行的第二輪核對，**不是**全新對話、與生成流程完全隔離的獨立 AI 審查。檢查依據為 Round 2 專案檔案（`wiki/sources`、`runs/round2/outline.md`、`runs/round2/deck.html`、`docs/index.html`）及可直接開啟的官方／出版社公開來源。核對日期：2026-11-23。

## 結構檢查（本次實際重跑）

- `python scripts/check_cards.py wiki/sources`：PASS；8 篇、21 條 Claim（19 條來源主張＋2 條 AI 建議）。
- `python scripts/check_outline.py runs/round2/outline.md wiki/sources`：PASS；12 頁。
- `python scripts/check_deck.py runs/round2/deck.html wiki/sources scripts/banned.txt`：PASS；12 頁。
- 本次未聲稱親自完成公開網站完整 Chromium 互動測試；外部審查者已回報完整 Chromium 的 12 頁渲染與四種視窗尺寸測試均通過。Round 2 原報告仍記錄當時沙盒 `LIMITED`。

## 外部來源抽核

| 來源 | 核對內容 | 結果 |
|---|---|---|
| S1 ETS | L&R 各 100 題；45+75 分鐘；Part 1–7；另有約 30 分鐘基本資料問卷 | 內容相符。 https://www.ets.org/toeic/about/listening-reading.html |
| S2 Dunlosky et al. | 練習測驗／分散練習評為 high utility；重讀及畫重點列為 low utility，非完全無效 | 主張與原文方向相符。 DOI:10.1177/1529100612453266 |
| S3 Cepeda et al. | 184 篇文章、317 個實驗、839 次評估；最佳間隔與保留期間相關 | 摘要核對相符。 DOI:10.1037/0033-2909.132.3.354 |
| S4 Maie et al. | 兩個既有班級各 44 人、學習 100 字、累積與非累積測驗；效果受練習及原本程度影響 | Wiley HTML 摘要和 Methods 核對相符。 DOI:10.1002/tesq.3391 |
| S5 Sangers et al. | 大量閱讀的短期正向效果約小到中等；無足夠長期追蹤 | Springer HTML 核對相符。 DOI:10.1007/s10648-025-10068-6 |
| S6 Karlin & Karlin | 269 位日本大學生、精聽與泛聽比較、原始分數和 Rasch 估計結論不同 | 出版社摘要核對相符，**僅摘要**。 DOI:10.1075/aila.22015.kar |
| S7 ETS | 官方提供 handbook、sample tests、online preparation course 等 | 官方列表核對相符；不推論效果。 https://www.ets.org/toeic/test-takers/prepare.html |
| S8 OpenLearn | Extensive＝重整體大意；Intensive＝具體資訊與細節活動 | 公開課程 §4 核對相符。 https://www.open.edu/openlearn/mod/oucontent/view.php?id=68253&section=5 |

這是針對**簡報實際呈現的關鍵數字、定義與結論的抽核**，不等於逐段驗證每篇研究的全部正文或所有學術推論。

## 仍需誠實列出的限制

1. **完全獨立的新對話 AI 審查尚未完成**。先前的外部審查意見可列入 N5，但審查者曾參與工具包設計，不能標為完全獨立。
2. **S6 只使用摘要**，無法查核未公開的完整研究方法、組間比較及所有研究限制。
3. **`raw/` 本機全文封存尚未齊全**，故此專案著重公開 Wiki 卡片與原始網址追溯；不宣稱完整可重現原始擷取。
4. **部署功能測試需分開記錄**：公開首頁可被網頁檢索開啟、使用者回報手機可開；這和在本次環境親自點擊所有互動控件並非同一件事。
5. GitHub 上舊 `README.md`、`STATUS.md`、`sources.md` 仍有「尚未部署／未 ingest」歷史字樣，應以本次更新版取代，避免評分者誤認專案未完成。

## 結論

就**已抽核的**官方題型時間、S4/S5/S6 研究數字和研究限制，以及 S8 教學定義而言，未發現需暫停提交的重大內容矛盾。可用 Round 2 作為教學 HTML 成品；正式提交前應更新狀態文件，並由學生本人核對及完成反思。不可將本檔冒稱為「完全獨立新對話 AI 審查」。
