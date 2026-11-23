# 工具包相容性修改（與 v2 原版比較）

只修改 `scripts/check_render.py`：
1. Playwright 預設 Chromium 不存在時，可使用本機的 `chromium` 或 `CHROMIUM_EXECUTABLE` 指定執行檔。
2. 以 loopback HTTP 嘗試讀取 HTML，避免受限瀏覽器阻擋 `file://`。
3. 本執行環境連 loopback 都被封鎖，則在全新空白頁使用 `set_content()` 載入 HTML，且印出 `LIMITATION`。

這個 fallback 是為了執行模擬自我測試，**並非完整的線上 HTML 驗收**。原版程式另存於 `vendor-original/check_render.py` 供查核。

此外，建立了 `interview-summary-public.md`，避免 GitHub 公開本人學習背景；完整 `interview-log.md` 保留在本機且被 `.gitignore` 排除。
