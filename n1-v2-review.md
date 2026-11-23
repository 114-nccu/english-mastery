# English Mastery｜工具包 v2 驗收與 N1 補充查核

查核日期：2026-11-22。此處只記錄在本工作環境確實執行的檢查，以及從公開網站核對的資訊；**Wiki ingest 仍是 0 篇**。

## 工具包驗收

- 確認收到 `english-mastery-kit-v2.zip`，內容含 `scripts/` 四支檢查程式、`selftest/`、`prompts/` 五份 prompt、`templates/`、`sources.md` 及 `README.md`。
- 原版 selftest：good/bad 的 `check_cards`、`check_outline`、`check_deck` 符合預期。`check_render` 因 Playwright 預設的 Chromium 執行檔未安裝，無法驗證；不是「正確資料渲染 FAIL」的證據。
- 執行 `python -m playwright install chromium` 遭 DNS `EAI_AGAIN` 阻擋，未成功下載。此環境已有 `/usr/bin/chromium`；修補 `check_render.py` 可在沒有 Playwright 下載的瀏覽器時尋找作業系統 Chromium，或以環境變數 `CHROMIUM_EXECUTABLE` 指定。修補版驗證輸出見 `tests/toolkit-selftest-checked.txt`。
- 此沙盒瀏覽器同時封鎖 `file://` 與 `http://127.0.0.1` 的頁面導覽，因此增加受限環境專用 `page.set_content()` fallback。此方式可測 **inline HTML/CSS 與溢出自我測試**，但不能確認真實部署的外部 CSS/JS 資源或網路連結。正式簡報仍需在實際瀏覽器/部署網站驗證。
- **相容版 selftest 的 8 個 good/bad 檢查均符合預期**，輸出見 `tests/toolkit-selftest-checked.txt`。這是模擬資料 selftest，尚未使用真實 Wiki 條目、真實簡報進行 N2–N6 檢查。

## S4（Maie et al., 2025）查核結果

- 正式題名：Cumulative Testing for L2 Vocabulary Learning: The Impact of Retrieval Practice and Proficiency。
- Ryo Maie、Gaia Oikawa、Ying Chen、Takumi Uchihara；*TESOL Quarterly*, 59(4), 1979–2008；DOI 10.1002/tesq.3391。
- 出版頁：https://onlinelibrary.wiley.com/doi/10.1002/tesq.3391
- ERIC 正式書目：https://eric.ed.gov/?id=EJ1489070
- 研究者公開 PDF：https://researchmap.jp/takumiuchihara/published_papers/49795126/attachment_file.pdf
- 該 PDF 的首末書目資訊含早期版本頁碼（Vol. 0, No. 0，版內頁碼），而 Wiley/ERIC 已提供正式卷期頁碼。之後製作 claim 的頁碼時要註明使用哪一個版本，不得混用。
- 公開 PDF 首頁標示 CC BY 開放授權。本文已取得公開可查閱網址；在本環境尚未成功下載 PDF 到本地 `raw/`，也沒有完成逐 claim 摘要與數字核對。

## S6（Karlin & Karlin, 2023）查核結果

- 正式刊載：*AILA Review*, 36(1), 91–111；DOI 10.1075/aila.22015.kar。
- 出版商頁：https://benjamins.com/catalog/aila.22015.kar （全文 PDF 需授權）
- 公開的 Academia.edu 閱讀頁面：https://www.academia.edu/106244063/Developing_L2_listening_comprehension_through_extensive_and_intensive_listening
- Academia.edu 顯示相當多的正文段落，但是否由作者合法上傳、可否下載/重製/公開分發，這輪**尚未確認**。建議以校園圖書館、出版商授權、作者直接提供為首選。未有確定合規的原文副本前，不把全文查閱、頁碼查證當成已完成。
- 研究摘要顯示受試 269 位日本大學生、分為泛聽與精聽兩組；結果對不同計量方式敏感。切勿直接聲稱「泛聽無效」或「精聽優於泛聽」為跨情境因果定律。

## S1／實務來源補強

- ETS 近期 FAQ 說明：正式考試作答時間為 2 小時（45 分聽力＋75 分閱讀），考試當天含報到/行政程序應預留 2.5–3 小時。兩種說法並不矛盾，應清楚分別標示。
- 官方準備材料頁 https://www.ets.org/toeic/test-takers/prepare.html 可考慮新增 S7，以符合使用者 R03「學術研究＋實務指南」；只有在正式 ingest 後才計入資料數量。

## 目前狀態

- N0：使用者本人訪談與摘要確認完成；文件 `requirements.md`、`AGENTS.md` 已建立。
- N1：核對來源與找到公開資料入口；實際 raw 原文檔案尚未備齊，未達「全部原文已取回」狀態。
- N2：0 篇，未開始；N3–N7 皆未開始。
