# 簡易購物車專案
這是一個使用 Flask 和 MySQL 的簡易購物車應用程式。該專案包括了商品首頁、購物車管理和簡單的 CRUD 操作。

<br>
 
## 專案結構
- `app.py`： 主應用程序檔案，包含 Flask 應用程式及路由。
- `static/`
  - `css/`
    - `styles_index.css`： 商品首頁樣式。
    - `styles_cart.css`： 購物車頁面樣式。
  - `js/`
    - `scripts_index.js`： 商品首頁的 JavaScript。
- `templates/`
  - `index.html`： 商品首頁模板。
  - `cart.html`： 購物車頁面模板。
- `schema.sql`： 用於創建資料庫和資料表的 SQL 腳本。
- `data.sql`： 用於插入初始數據的 SQL 腳本。
- `requirements.txt`： Python 依賴項列表。
- `README.md`： 專案說明文件。
- `.env`： 資料庫連接資訊。
<br>

## 環境設置
1. **安裝 Python**
    
    確保您的系統上已安裝 Python。如果尚未安裝，請從 [Python 官方網站](https://www.python.org/downloads/) 下載並安裝，建議使用 Python 3.7 或更高版本。

    安裝完成後，您可以使用以下命令來檢查 Python 是否已安裝：

    ```
    python --version
    ```

2. **安裝 MySQL**

    確保您的系統上已安裝 MySQL。如果尚未安裝，請從 [MySQL 官方網站](https://dev.mysql.com/downloads/) 下載並安裝，並需記下您 MySQL 用戶的密碼。

    安裝完成後，您可以使用以下命令來檢查 MySQL 是否正常運行：

    ```
    mysql --version
    ```

3. **創建 `.env` 文件**

    在專案根目錄下創建一個名為 `.env` 的文件，使用文本編輯器打開文件並添加所需的環境變數，並根據以下格式設置正確的值：

    ```env
    # .env 文件
    SECRET_KEY=mysecretkey               # 請替換為您的 Flask 密鑰
    DB_HOST=127.0.0.1                    # 資料庫主機，通常為 localhost 或 IP 地址
    DB_NAME=shopping_cart                # 資料庫名稱
    DB_USER=root                         # 資料庫用戶名
    DB_PASSWORD=12345@db                 # 資料庫密碼
    ```
    請填入您正確的資料庫主機、名稱、用戶名和密碼。這些值應該與您的 MySQL 伺服器配置匹配。

    <br>

4. **Python 套件**

    確保您已經安裝了所需的 Python 套件。使用以下命令安裝：

    ```bash
    pip install -r requirements.txt
    ```
<br>

## 資料庫設置
在使用此專案之前，您需要設置 MySQL 資料庫並初始化數據。請按照以下步驟操作：

1. **創建資料庫和資料表**

   使用 `schema.sql` 腳本來創建資料庫和資料表。可以通過以下指令在 MySQL 中執行：

   ```bash
   mysql -u root -p < schema.sql

2. **插入初始數據**

    使用 `data.sql` 腳本來插入初始數據。
    <br>執行以下指令：

    ```bash
    mysql -u root -p shopping_cart < data.sql
    ```

    或是執行以下指令：
    ```bash
    mysql --default-character-set=utf8mb4 -u root -p shopping_cart < data.sql
    ```

    注意：執行 data.sql 之前，請確保已經成功創建了資料庫和資料表。
    
<br>

## 運行指南
啟動 Flask 應用程式：

```bash
python app.py
```

這指令將啟動 Flask 開發伺服器，並在本地端口上運行應用程式。

打開瀏覽器，訪問 `http://127.0.0.1:3000/` 。

首頁（`/`）：瀏覽產品，可選擇數量並點擊「Add To Cart」按鈕添加產品到購物車。

查看購物車（`/cart`）：點擊「View MyCart」查看和管理已加入購物車的產品。

<br>

## 聯繫我

- Email: Yvonneyuo@gmail.com
- GitHub: [YvonYu](https://github.com/YvonYu)
