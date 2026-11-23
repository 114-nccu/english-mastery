# N1 → N2 本機 Coding Agent 交接說明

**交接日期：2026-11-22；目前階段：N0 已確認，N1 尚待本機原文保存。N2–N7 未執行。**

## 本機準備

1. 解壓本專案 ZIP 至你自己的專案資料夾，使用 Antigravity／Codex／Claude Code 開啟該資料夾。
2. 確認 `interview-log.md` 和 `raw/` 在 `.gitignore` 內；公開 repo 不應包含私人完整訪談及原文 PDF。
3. 開啟終端機，執行：

```bash
python -m pip install playwright
python -m playwright install chromium
python selftest/run_selftest.py
```

4. 若 selftest 不是全部符合預期，先記錄 Python、Playwright、Chromium 版本及錯誤文字，**不能冒充 PASS**。檢查腳本仍無法驗證研究主張的語意忠實性。

## N1 原文保存與記錄

- S1／S7：把官方網頁保存為本機網頁快照，保留來源 URL、取得日期與頁面原文。S7 只表示官方「提供哪些教材」。
- S2／S3／S4／S5：透過正式期刊、機構典藏、研究者授權版本取得正文，存於私有 `raw/`；S4 註明 `page_basis: researchmap 早期版 PDF`，Claim 用 `§章節`。
- S6：僅優先查學校圖書館；取不到合法全文，記 `full_text: false`、`location: 摘要`；可不計入主要五篇完整來源。
- 所有狀態必須實際核對後才填進 `n1-raw-manifest.md`。

## Git 初始提交：含腳本、Prompt、模板與空白 Wiki 資料夾

`.gitignore` 已排除 `raw/`、私人 `interview-log.md` 與 `selftest` 產生的 `mapping.md`／截圖。**原文 PDF 不會因為放在 `raw/` 就被 Git 記錄**；也不要使用 `git add -f raw/`。

以下在**自己的電腦**與專案根目錄執行。這份交接 ZIP 沒有 Git 歷史，也沒有代替你完成第一次 commit。

```bash
# 先保留空白 Wiki 目錄（即使 ZIP 會跳過空資料夾）
mkdir -p wiki/sources wiki/concepts tests raw
: > wiki/sources/.gitkeep
: > wiki/concepts/.gitkeep

# 安裝真正的瀏覽器測試環境（一次即可）
python3 -m pip install playwright
python3 -m playwright install chromium

# 把本機自我測試結果存成獨立紀錄；有 FAIL / SKIP / LIMITED 就不可宣稱完整通過
set -o pipefail
python3 selftest/run_selftest.py | tee tests/selftest-local.txt

# 提交完整可追溯的工具與規格，而非只提交一小部分清單
git init
git add .
git diff --cached --name-only

# 安全檢查：此處若出現私人資料或 raw/ 路徑，先停止，不要 commit
if git diff --cached --name-only | grep -E '(^|/)interview-log\.md$|(^|/)raw/'; then
  echo 'STOP: staging contains private material'
else
  git commit -m 'n1: project setup, toolkit, verified source list'
fi
```

`git add .` 應包括 `scripts/`、`prompts/`、`templates/`、`selftest/` 及 `wiki/` 的 `.gitkeep`。在第一次提交前仍要人工確認 `git diff --cached --name-only`，避免其他意外的敏感檔案；`git diff --cached --name-only` 是必要但不足的安全檢查，因為檔案**內容本身**也可能有個資。

`tests/toolkit-selftest-checked.txt` 是**先前沙盒測試參考紀錄**，不能取代你新產生的 `tests/selftest-local.txt`。本機若出現 `LIMITATION: ... set_content only`，代表渲染腳本僅檢查了內嵌內容，外部 CSS／JS 沒有完整驗證；若出現 `SKIP` 亦不得報告完整 8/8。更新後的 `selftest/run_selftest.py` 會顯示 `LIMITED`／`SKIP`，並以 exit code 2 表示未完整測完；所有 8 項完整符合預期才會回傳 exit 0。

N1 原文下載後再更新 `n1-raw-manifest.md`、`sources.md`、`n1-audit.md` 並另外 commit。公開 Repo 除了避免私人訪談、`raw/` 外，也應檢查歷史提交；`.gitignore` 不會刪除已被追蹤的檔案。

## 下一步 N2：分組 ingest + 每階段檢查

順序：**官方資料（S1、S7）→ 一般學習研究（S2、S3）→ 第二語言研究（S4、S5；S6 可只用摘要）**。每篇來源獨立證據卡；每組完成後執行 `python scripts/check_cards.py wiki/sources`，只修改失敗的條目。

N2 正式執行前：`wiki/sources/` 應沒有假資料；`tests/toolkit-selftest-checked.txt` 不可充當真實資料 ingest 的測試報告。

## 須由本人完成的最後步驟

- 由你操作／授權 Coding Agent 在本機建立 Git 歷史，保留真實檢查輸出、截圖與反思。
- 將最終 `docs/index.html` 公開至 GitHub Pages 等靜態網站並在無痕視窗、手機中驗收。
- 本地 sandbox 可生成／測試部分檔案，但不能自動代表已部署公開網頁；部署必須有可開啟的真實 URL。
