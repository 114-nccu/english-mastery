# 來源與查核清單｜N1 書目核對及 Round 2 補充來源

> 本檔只記錄本輪實際核對到的書目／官方頁面，以及需要繼續處理的原文核對工作。**目前 Wiki 已建立 S1–S8 八份來源卡，通過格式檢查，但原文完整本機保存仍待確認。** 本檔為正式來源表；歷史工具包資料僅供核對。

| ID | 資料與書目 | DOI／官方網址 | 已確認 | 待處理 | N1 狀態 |
|---|---|---|---|---|---|
| S1 | ETS, *About the TOEIC Listening and Reading Test*（官方網頁，無 DOI） | https://www.ets.org/toeic/about/listening-reading.html | 官方網站；200 題，聽力 100 題 45 分鐘、閱讀 100 題 75 分鐘，Part 1–7 | 儲存合規的官方資料快照；記錄引用位置與抓取日期 | 書目／關鍵官網事實已核 |
| S2 | Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). *Improving Students’ Learning With Effective Learning Techniques: Promising Directions From Cognitive and Educational Psychology*. *Psychological Science in the Public Interest*, 14(1), 4–58 | https://doi.org/10.1177/1529100612453266 | 出版網站／PubMed 書目與 DOI | 取得原文並核對具體段落與研究限定；不可直接推出 TOEIC 提分 | 書目已核；未 ingest |
| S3 | Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). *Distributed Practice in Verbal Recall Tasks: A Review and Quantitative Synthesis*. *Psychological Bulletin*, 132(3), 354–380 | https://doi.org/10.1037/0033-2909.132.3.354 | PubMed 作者／期刊／年卷／頁／DOI；公開原文 PDF 有入口 | 核對正文引用位置與完整數據；注意為一般記憶研究 | 書目已核；未 ingest |
| S4 | Maie, R., Oikawa, G., Chen, Y., & Uchihara, T. (2025). *Cumulative Testing for L2 Vocabulary Learning: The Impact of Retrieval Practice and Proficiency*. *TESOL Quarterly*, **59(4)**, 1979–2008 | https://doi.org/10.1002/tesq.3391 | Wiley/ERIC 確認正式刊載 59(4):1979–2008、作者、DOI；研究者公開 CC BY 全文 PDF 可線上查閱（但尚未儲存至 raw/） | 本機保存研究者公開全文；claim 位置統一採 §章節名稱；front matter 註明 `page_basis: researchmap 早期版 PDF`；研究設計與限制仍待 N2 對照 | **N1 書目及全文入口已核**；尚未下載至 raw、未 ingest |
| S5 | Sangers, N. L., van der Sande, L., Welie, C., Dobber, M., & van Steensel, R. (2025). *Learning a Language Through Reading: A Meta-analysis of Studies on the Effects of Extensive Reading on Second and Foreign Language Learning*. *Educational Psychology Review*, 37, article 96 | https://doi.org/10.1007/s10648-025-10068-6 | Springer 官網開放全文、作者、出版日、DOI | 核對研究設計、追蹤效果和限制；避免過度延伸至 TOEIC | 書目已核；未 ingest |
| S6 | Karlin, O., & Karlin, S. (2023). *Developing L2 Listening Comprehension Through Extensive and Intensive Listening*. *AILA Review*, 36(1), 91–111 | https://doi.org/10.1075/aila.22015.kar | 出版社官方書目與摘要；269 位日本大學生之研究資訊 | **正式 PDF 需授權**：僅短時間查詢學校圖書館，無合法全文則標記 `full_text: false` 並只用摘要；不引用無法核對的正文頁碼 | ⚠️ 書目＋摘要已核；全文非阻擋條件 |
| S7 | ETS, *TOEIC Test Preparation Materials*（官方網頁，無 DOI） | https://www.ets.org/toeic/test-takers/prepare.html | 官方網頁提供考生手冊、樣題與備考資源資訊 | 保存官方頁面快照；僅支持「提供哪些資源」等 FACT，**不能**當作資源效果的因果證據 | **N1 官方頁面已查得**；未保存快照、未 ingest |

| S8 | The Open University, OpenLearn. *How to Learn a Language*, Week 5, Section 4, *Listening: the Big Picture*（網頁未標發表年） | https://www.open.edu/openlearn/mod/oucontent/view.php?id=68253&section=5 | 查閱課程全文 §4，包含 Activity 6 對 extensive／intensive listening 的定義及 Discussion 的活動例子 | 僅作概念定義，不作效果或多益提分證據；若需本機封存，取得符合授權的個人閱讀副本或記錄網頁參照即可 | **N1 線上來源查閱完成；2026-11-23 新增，尚未封存 raw** |

## 來源與版本控制規則

- **S4 頁碼基準**：正式期刊書目保留 `59(4), 1979–2008`；研究者公開 early-view PDF 的內文頁碼不得混用。S4 證據卡應填 `page_basis: researchmap 早期版 PDF`，Claim 位置統一用 `§章節`（例如 `§Results`），並核對該節確有此敘述。
- **S6 全文授權**：先透過學校圖書館查詢；無授權全文時，不保存來路不明的 PDF、不填正文頁碼；如果要使用摘要，在卡片標示 `full_text: false` 和位置 `摘要`。摘要不支持的統計細節不可補。
- **S7 角色**：屬於官方備考資源目錄，不能推論使用某教材必然改善英文或 TOEIC 成績。
- **TOEIC 測驗時間**：ETS 正式作答為聽力 45 分鐘＋閱讀 75 分鐘＝2 小時；另有約 30 分鐘基本資料問卷，FAQ 建議到場預留 2.5–3 小時。引用時依保存快照記錄 `retrieved` 日期及具體口徑，不能把行政時間說成作答時間。
- **公開 GitHub**：`raw/` 依 `.gitignore` 保持不追蹤。只提交 `n1-raw-manifest.md`、來源清單與查核紀錄，不上傳原文全文。

## 查核入口（瀏覽器開啟）

- S4 ERIC：https://eric.ed.gov/?id=EJ1489070
- S4 Wiley 卷期：https://onlinelibrary.wiley.com/toc/15457249/2025/59/4
- S4 作者公開 PDF：https://researchmap.jp/takumiuchihara/published_papers/49795126/attachment_file.pdf
- S6 出版社：https://benjamins.com/catalog/aila.22015.kar
- S7 ETS 備考資料：https://www.ets.org/toeic/test-takers/prepare.html
- ETS 測驗：https://www.ets.org/toeic/about/listening-reading.html
- ETS FAQ：https://www.ets.org/toeic/about/faq/test-taker-related-faq.html

**重要：**本次新增查核僅完成網頁／書目身分核對，仍未建立 Wiki 或執行真實資料檢查。N1 原始檔案已否實際取得，應以本機 `n1-raw-manifest.md` 及檔案存在為準。
