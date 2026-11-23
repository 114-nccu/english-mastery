# English Mastery｜來源與使用狀態（2026-11-23 更新）

> 下列 8 份資料均已建立 `wiki/sources/Sx.md` 證據卡。當中 19 條為有來源的 Claim，另有 2 條 AI 教學建議（不算研究證據）。`check_cards.py` 檢查 PASS。**已 ingest 不代表每份原始 PDF 已保存於 `raw/`。**

| ID | 正式來源 | 入口 | 在 Wiki 的用途 | 使用界線 |
|---|---|---|---|---|
| S1 | ETS, *About the TOEIC Listening and Reading Test* | https://www.ets.org/toeic/about/listening-reading.html | 官方測驗定位、7 個 Part、100+100 題及 45+75 分鐘 | 只作官方測驗事實，網站版本應註明查閱日 |
| S2 | Dunlosky et al. (2013), *Psychological Science in the Public Interest*, 14(1), 4–58. DOI 10.1177/1529100612453266 | https://doi.org/10.1177/1529100612453266 | 練習測驗、間隔練習、重讀／畫重點的相對效用 | 一般學習科學，非 TOEIC 直接效果 |
| S3 | Cepeda et al. (2006), *Psychological Bulletin*, 132(3), 354–380. DOI 10.1037/0033-2909.132.3.354 | https://doi.org/10.1037/0033-2909.132.3.354 | ISI 與保留間隔的關係 | 一般言語記憶研究；沒有所有人通用的最佳天數 |
| S4 | Maie et al. (2025), *TESOL Quarterly*, 59(4), 1979–2008. DOI 10.1002/tesq.3391 | https://doi.org/10.1002/tesq.3391 | 累積測驗、兩個既有班級各 44 人、100 字學習 | 使用 Wiley HTML 的 §章節名稱定位，不混用早期 PDF 頁碼；非 TOEIC 提分證據 |
| S5 | Sangers et al. (2025), *Educational Psychology Review*, 37, article 96. DOI 10.1007/s10648-025-10068-6 | https://doi.org/10.1007/s10648-025-10068-6 | 大量閱讀的短期小至中等正向效果 | 缺乏足夠長期追蹤；非 TOEIC 直接分數證據 |
| S6 | Karlin & Karlin (2023), *AILA Review*, 36(1), 91–111. DOI 10.1075/aila.22015.kar | https://doi.org/10.1075/aila.22015.kar | 精聽／泛聽研究結果與測量指標比較 | `full_text: false`，**僅引用出版商公開摘要** |
| S7 | ETS, *TOEIC Test Preparation Materials* | https://www.ets.org/toeic/test-takers/prepare.html | 官方考生手冊、樣題及準備課程等資源存在 | 資源存在不等於研究證明教材必然有效 |
| S8 | The Open University (OpenLearn), *How to Learn a Language*, Week 5 §4 | https://www.open.edu/openlearn/mod/oucontent/view.php?id=68253&section=5 | 泛聽（聽大意）與精聽（聽具體資訊）的定義 | 教學定義，不是比較效果的因果研究 |

## 來源版本與權限

- 各項 Claim 詳見 `wiki/sources/S1.md`–`S8.md`，可用 `runs/round2/mapping.md` 追溯簡報頁面。
- S4 正式卷期頁碼可作書目；Claim 位置依最終 Wiki 卡片使用 `§Methods`、`§Results` 等章節。其 `page_basis` 為 Wiley 正式 HTML 的章節定位，避免與早期 PDF 的頁碼混用。
- S6 全文未獲授權取得，不填正文頁碼、不從摘要推測未公開的結果。
- 有些原始檔尚未保存至本機 `raw/`，公開 Repo 不附論文全文。這不影響已建立之 Wiki 卡片存在，但限制了來源可重現的程度。
