# 入廠證件辨識服務 API 文件專案

## 專案概述

這是一個使用 Swagger UI 展示的 OCR (光學字元辨識) API 文件網頁。該服務提供多種台灣文件類型的 OCR 識別功能，包括身分證、健保卡、居留證、護照、車輛文件和勞保文件等。

**重要特點：完全離線運作，無需網路連線即可查看 API 文件。**

## 專案架構

### 核心檔案
- **index.html** - 主要的 API 文件頁面，使用 Swagger UI 展示
- **openapi.json** - OpenAPI 3.0 規格文件，包含所有 API 端點定義
- **server.py** - FastAPI 伺服器，配置為在 0.0.0.0:5000 運行
- **pyproject.toml** - Python 專案配置，包含 FastAPI 和 Uvicorn 依賴
- **swagger-ui/** - Swagger UI 本地靜態資源 (1.8MB)
  - swagger-ui.css
  - swagger-ui-bundle.js
  - swagger-ui-standalone-preset.js
  - favicon-32x32.png
- **README.md** - 使用者說明文件

### 技術堆疊
- **前端**: HTML5 + Swagger UI 5.10.3 (本地離線版)
- **Web 框架**: FastAPI 0.121.0
- **ASGI 伺服器**: Uvicorn 0.38.0 (with standard extras)
- **Python 版本**: 3.11
- **規格**: OpenAPI 3.0.0
- **端口**: 5000 (webview)
- **離線使用**: ✅ 完全支援

## 最近變更

**2024-11-04**
- 建立初始專案結構
- 從附件複製 OpenAPI 規格文件 (1,436 行)
- 設定 Swagger UI 展示頁面
- **升級至 FastAPI**: 從簡易 HTTP Server 升級為 FastAPI + Uvicorn
  - 使用 FastAPI middleware 處理 cache control headers
  - 改用 Uvicorn ASGI 伺服器提供更好的效能
  - 配置靜態檔案服務
- **本地化 Swagger UI 資源**: 下載所有 Swagger UI 資源至本地
  - 從 jsdelivr CDN 下載 swagger-ui.css (149KB)
  - 從 jsdelivr CDN 下載 swagger-ui-bundle.js (1.4MB)
  - 從 jsdelivr CDN 下載 swagger-ui-standalone-preset.js (226KB)
  - 從 jsdelivr CDN 下載 favicon-32x32.png
  - 總大小：1.8MB
  - 更新 index.html 使用本地路徑
  - 使用 FastAPI StaticFiles 掛載靜態資源
  - **現在支援完全離線使用**
- 設定 workflow 以在 port 5000 自動啟動服務

## API 服務概述

此 OCR 服務支援以下文件類型：

### 證件類別
- 中華民國國民身分證
- 全民健康保險卡
- 中華民國居留證
- 外勞護照（越南）

### 車輛類別
- 汽車行照
- 柴油車排煙檢測表
- 自主管理標章

### 保險類別
- 勞工職業災害保險特別加保
- 勞保局E化加保申報表
- 各種勞保投保資料表

## 開發筆記

### Workflow 配置
- Workflow 名稱: `api-docs`
- 命令: `python server.py`
- 輸出類型: webview
- 端口: 5000

### 重要實作細節
1. **FastAPI Framework**: 使用 FastAPI 作為 Web 框架，提供現代化的異步 API 開發體驗
2. **Cache Control**: 透過 FastAPI middleware 配置 no-cache headers 以確保文件更新能立即反映
3. **ASGI Server**: Uvicorn 提供高效能的 ASGI 伺服器，支援異步處理
4. **本地靜態資源**: 所有 Swagger UI 資源已下載至 swagger-ui/ 目錄
5. **靜態檔案服務**: FastAPI 的 StaticFiles 和 FileResponse 提供優化的檔案傳輸
6. **離線運作**: 無需任何 CDN 連線，完全自給自足

## 使用方式

伺服器會自動啟動。使用者可以：
1. 在 Replit Webview 中查看文件
2. 瀏覽所有 API 端點
3. 查看請求/回應範例
4. 測試 API 呼叫格式
5. **離線環境中使用** - 無需網路連線

## 未來改進建議
- 可考慮添加 API 測試功能（需要實際 API key）
- 可新增深色/淺色主題切換
- 可添加語言切換功能（中文/英文）
- 可以考慮壓縮靜態資源以減少檔案大小
