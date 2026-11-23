# N1 來源核對工作紀錄

**日期：2026-11-22（台灣時間）**  
**進度：已啟動 N1；完成六筆官方／學術出版來源的基本書目或官方資訊核對。未完成全部原文取得及逐項 claim 查驗。**

## 已實際做的檢查

1. 開啟 ETS 官方「About the TOEIC Listening and Reading Test」頁，核對 Listening 45 分鐘 100 題、Reading 75 分鐘 100 題、Part 1–7 名稱。
2. 查驗 Dunlosky et al. (2013) 期刊與 DOI 的出版資料。
3. 開啟 PubMed 上 Cepeda et al. (2006) 頁，核對作者、期刊、年份、卷期頁、DOI。
4. 開啟 Wiley 上 Maie et al. (2025) 的全文網頁，核對作者、文章資訊、DOI 與摘要。
5. 開啟 Springer 上 Sangers et al. (2025) 的全文網頁，核對出版資訊、作者、DOI 與公開取得狀態。
6. 開啟 John Benjamins 上 Karlin & Karlin (2023) 的出版頁，核對期刊、作者、DOI 與摘要；發現完整正文下載需授權。

## 外部核查入口

- ETS：https://www.ets.org/toeic/about/listening-reading.html
- Dunlosky：https://doi.org/10.1177/1529100612453266
- Cepeda：https://pubmed.ncbi.nlm.nih.gov/16719566/
- Maie：https://onlinelibrary.wiley.com/doi/full/10.1002/tesq.3391
- Sangers：https://link.springer.com/article/10.1007/s10648-025-10068-6
- Karlin：https://benjamins.com/catalog/aila.22015.kar

## 尚未做、因此不能宣稱完成

- [ ] 實際原始 PDF／HTML 完整素材取得並備妥 `raw/`；含來源權限確認。
- [ ] 檢查工具包 `sources.md` 是否有不同的來源版本或 ⚠️ 標記（工具包目前未取得）。
- [ ] 逐篇核對關鍵 claim 的正文位置、研究限制、統計數據。
- [ ] 至少五篇完成實際 Wiki ingest（目前 0）。
- [ ] 確認 S6 可合法取得原文或找可核對全文之替代研究。
- [ ] 取得且執行四支檢查腳本於真實資料（目前未取得程式，沒有測試結果）。

## 判讀

六筆來源的基本身分確認，不等於六筆都是「完整可 ingest 的原始資料」。進入 N2 之前，必須完成實際原文與頁段證據核對。若無法達到五篇，就停止補來源。


## 2026-11-22｜工具包 v2 與追加來源查核

- 已收到並核對 `english-mastery-kit-v2.zip`，原本附件缺失問題已解決。
- S4：Wiley/ERIC 確認 TESOL Quarterly 59(4):1979–2008；研究者公開 CC BY PDF 可查詢，**尚未下載至 raw/**。
- S6：John Benjamins 正式全文需授權；找到 Academia.edu 公開正文閱讀頁，但轉存和再散布的權限**無法確認**；學校圖書館為優先合法途徑。
- `python selftest/run_selftest.py` 在此環境經過相容性處理後顯示 8/8 符合預期；原工具包渲染測試因瀏覽器缺失/導覽被限制未能直接運作。詳細內容見 `tests/toolkit-selftest-checked.txt`、`n1-v2-review.md`。
- S7 ETS 官方備考材料已找到正式頁面，僅作候選；未 ingest、不計入 5 篇。
- N1 原文下載／逐篇頁碼驗證仍未完成；**不得進入 N2 並宣稱證據完整**。

## 2026-11-22 本機交接附註（不等同 N1 全面通過）

- S4：ERIC 與 Wiley 正式期刊卷期頁碼確認 `59(4), 1979–2008`；研究者版本頁碼不同，後續卡片採 `§章節` 與 `page_basis`。本沙盒 `raw/` 仍未存入實際全文，不聲稱完成全文 ingest。
- S6：出版商書目、摘要已核；建議限時查圖書館，否則 `full_text: false`，不引用無依據的正文。
- S7：官方 Preparation Materials 頁可確認其資源類型；未保存本機快照，不能將其視為學習效果證據。
- TOEIC 時間：作答 2 小時；ETS 另述約 30 分鐘資料問卷及考試當日預留 2.5–3 小時，依所保存快照口徑表述。
- `raw/` 已設定不被 Git 追蹤，故新增 `n1-raw-manifest.md` 作為可公開且可追溯的取得紀錄。
