# 來源清單 v2（2026-11-22，ID 已對齊你的 sources.md）

> 這份是交叉核對用的參考。**以你專案裡的 sources.md 為正式版本。** 我核對到的是書目資訊和摘要層級的內容；每條 claim 的頁碼、數字和限制，要等你打開原文 ingest 時才算查證完成。
> **以下所有研究都不是「多益分數提升」的直接證據。**

| ID | 書目 | 我這邊另外核對到的 | 仍待你確認 |
|---|---|---|---|
| S1 | ETS. About the TOEIC Listening and Reading Test. https://www.ets.org/toeic/about/listening-reading.html | 各 100 題；Listening 45 分鐘、Reading 75 分鐘；ETS 頁面另寫「約 2.5 小時，含約 30 分鐘背景問卷」 | 簡報要寫「2 小時測驗」還是「約 2.5 小時」，要標示依據；ETS 頁面會改版，請存一份 PDF 快照並記錄日期 |
| S2 | Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). *Psychological Science in the Public Interest, 14*(1), 4–58. https://doi.org/10.1177/1529100612453266 | 書目和 DOI 一致 | 一般學習研究，不是 L2 研究 |
| S3 | Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). *Psychological Bulletin, 132*(3), 354–380. https://doi.org/10.1037/0033-2909.132.3.354 | 書目和 DOI 一致 | 一般記憶研究（verbal recall），不能推出具體的「最佳間隔天數」 |
| S4 | Maie, R., Oikawa, G., Chen, Y., & Uchihara, T. (2025). Cumulative testing for L2 vocabulary learning: The impact of retrieval practice and proficiency. *TESOL Quarterly*. https://doi.org/10.1002/tesq.3391 | 作者、年份、DOI 和共同作者 Oikawa 網站上的列表一致（上一輪我判定「無法確認」，現已解決） | 卷 59、頁 1979–2008 我無法核對（Wiley 頁面我這邊抓不到），開放取得狀態也是 |
| S5 | Sangers, N. L., van der Sande, L., Welie, C., Dobber, M., & van Steensel, R. (2025). *Educational Psychology Review, 37*, Article 96. https://doi.org/10.1007/s10648-025-10068-6 | 期刊、卷、文章編號、DOI 一致 | d 值等數字請從原文表格抄錄 |
| S6 | Karlin, O., & Karlin, S. (2023). Developing L2 listening comprehension through extensive and intensive listening. *AILA Review, 36*(1), 91–111. https://doi.org/10.1075/aila.22015.kar | 期刊、卷期、頁碼已確認；出版平台售價 $35（需付費或授權） | 全文取得方式，見下方 |

## S6 全文問題的處理順序
1. 今晚先查學校圖書館電子資源（AILA Review／John Benjamins e-Platform）。
2. 取不到全文：證據卡 front matter 寫 `full_text: false`，所有 claim 的位置一律標「摘要」，**只能寫摘要裡有的內容**。`check_cards.py` 會擋下「沒有全文卻寫正文頁碼」的卡片。
3. 有全文的 S1–S5 已經達到 5 篇門檻，S6 不影響是否及格。

## 注意：第一優先「聽力」的證據最薄
需求 R02 把聽力列為第一優先，但六篇裡只有 S6 是聽力研究：單一準實驗、沒有對照組，而且可能只能讀到摘要。建議兩條路擇一：
- 簡報明說「聽力練習的研究證據目前比單字和閱讀少」（誠實，最省時間）。
- 另找一篇有全文的聽力研究補進來（要再走一次 N1，時間成本較高）。我目前沒有已核對過的候選，不推薦未查證的文章。

## R03「實務學習指南」
目前六篇沒有實務指南類來源。可以考慮把 ETS 的 Preparation Materials 頁（你 sources.md 的二級備查資料）正式 ingest 成 S7，或在反思裡說明為什麼沒有收。
