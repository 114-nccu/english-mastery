# Round 2 實際修正與驗收紀錄｜2026-11-23

本輪根據使用者提供的詳細審查意見，將錯誤退回來源／Wiki（新增 S8）及逐頁內容（P3、P4、P6、P7）節點後再渲染；原始 `runs/round1/` 保持不變。本輪不是為了製造反思而預設失敗案例。

| 關卡／測試 | 本環境執行結果 | 範圍與限制 |
|---|---|---|
| `check_cards.py wiki/sources` | PASS，8 篇來源、21 個 Claim（19 條來源 Claim＋2 條 AI 建議） | 格式／必填欄位檢查，不能取代語意核對 |
| `check_outline.py runs/round2/outline.md wiki/sources` | PASS，12 頁 | 每個內容頁引用有效 Claim，8 篇來源均被使用 |
| `check_deck.py runs/round2/deck.html wiki/sources scripts/banned.txt` | PASS，12 頁 | 主張 ID、兩位數以上數字及禁用字字面檢查；不會檢查 CSS 所隱含的誤導 |
| `check_render.py runs/round2/deck.html` | PASS **但 LIMITED**，12 頁未檢出溢出 | 沙盒封鎖本機網址，透過 Chromium `set_content` 載入，不代表正式網址可用 |
| `tests/viewport_review_round2.py` 首次執行 | FAIL（手機頁尾與導覽列重疊） | 先修正固定控制位置後發現 mobile 問題，並非模擬測試注入的假錯誤 |
| `tests/viewport_review_round2.py` 修正後 | PASS，1366×768、1440×900、390×844 | 三種視窗無導覽／頁尾重疊，水平溢出 0；測試包含翻頁與第一題互動回饋 |
| 來源 S8 原文對照 | 已核查公開課程 §4 | S8 僅支持泛聽／精聽定義，不作效益實驗依據 |
| 公開 GitHub Pages | 尚未執行 | 需由使用者登入部署後再開無痕視窗驗收 |
| 完全獨立新對話 AI 語意審查 | 尚未執行 | 本輪採使用者提供的外部審查回饋，獨立程度不可驗證 |

## 這輪提早檢查的教訓

- **N2 Wiki**：抽象名詞先確認「有定義來源」，否則內容雖遵守不能編造資料，仍無法教會初學者。
- **N4 逐頁稿**：分離研究證據與教學建議，建立 AI-02；用確定的定性分級代替沒有來源的百分比。
- **N6 渲染**：加入 CSS 視覺語意查核、不同裝置的控制項／頁尾重疊偵測。單純 check_deck 的文字符號檢查抓不到這些問題。

原始圖文差異、具體審查問題見 `review-and-fixes.md`。本檔由作業協助工具整理，最終反思須由學生本人核對與改寫。
