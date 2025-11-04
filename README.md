# 入廠證件辨識服務 API 文件

這是一個使用 Swagger UI 顯示的 OCR API 文件網頁。

## 專案簡介

此服務提供多種文件類型的光學字元辨識 (OCR) 功能，包括：

### 證件類別
- 中華民國身分證
- 全民健康保險卡
- 中華民國居留證
- 外勞護照 (越南)

### 車輛類別
- 汽車行照
- 柴油車排煙檢測表
- 自主管理標章

### 保險類別
- 勞工職業災害保險及保護法第10條規定 (特別加保)
- 勞保局E化加保申報表 (單筆)
- 勞保被保險人投保資料表
- 勞保個人加保完成線上列印
- 勞保團體加保完成線上列印

## 檔案結構

```
.
├── index.html          # API 文件主頁面
├── openapi.json        # OpenAPI 3.0 規格文件
├── server.py           # Python 簡易 HTTP 伺服器
└── README.md           # 本說明文件
```

## 使用方式

### 啟動伺服器

伺服器已配置為自動啟動在端口 5000。你可以在 Replit 的 Webview 中查看文件。

如需手動啟動：
```bash
python server.py
```

### 瀏覽文件

伺服器啟動後，開啟瀏覽器並訪問：
- 在 Replit 中：點擊 Webview 標籤
- 本地開發：http://localhost:5000

## API 使用範例

```bash
curl -X POST "http://localhost:2024/ocr/identity/id_card" \
  -H "accept: application/json" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/your/id_card.jpg"
```

### 回應範例

成功回應 (200 OK)：
```json
{
  "status": "success",
  "data": {
    "姓名": "王小明",
    "出生年月日": "民國81年10月21日",
    "統一編號": "A123456789"
  }
}
```

錯誤回應：
- **400 Bad Request:** 檔案類型無效
- **422 Unprocessable Entity:** 驗證錯誤
- **500 Internal Server Error:** 伺服器內部錯誤

## 技術細節

- **OpenAPI 版本:** 3.0.0
- **Swagger UI 版本:** 5.10.3 (透過 CDN)
- **伺服器:** Python HTTP Server
- **端口:** 5000

## 授權

入廠證件辨識服務 · OCR Recognition © 2024
