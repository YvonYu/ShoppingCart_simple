# pip3 install mysql-connector-python
# 載入套件
import mysql.connector
from flask import *
from mysql.connector import Error
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')  # 必須設定 secret_key 才能使用 Flash

db_config = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

# 連接到 MySQL
def db_connect():
    return mysql.connector.connect(**db_config)

# 模擬用戶ID
def get_user_id():
    return 1

# 商品首頁
@app.route('/')
def index():
    try:
        with db_connect() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT * FROM products')
                products = cursor.fetchall()
    except Error as e:
        print(f'Database error: {e}')
        products = []
    return render_template('index.html', products = products)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # 利用request取得表單name為quantity的欄位值
    # 接收POST方法的Query String
    quantity = int(request.form['quantity'])
    user_id = get_user_id()
    try:
        with db_connect() as conn:
            with conn.cursor() as cursor:
                # 獲取用戶購物車中該商品的數量
                cursor.execute('''
                    SELECT quantity FROM cart WHERE user_id = %s AND product_id = %s
                ''',(user_id, product_id))
                current_quantity = cursor.fetchone()
                if current_quantity:
                    current_quantity = current_quantity[0]
                else:
                    current_quantity = 0
                # 計算總數量
                total_q = current_quantity + quantity
                if total_q > 9:
                    quantity = 9 - current_quantity
                    flash('發生錯誤，單一品項最大能購買數量為9，請前往購物車檢查！', 'error')
                elif total_q <= 9:
                    cursor.execute('''
                        INSERT INTO cart(user_id, product_id, quantity)
                        VALUES(%s, %s, %s)
                        ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity)
                    ''',(user_id, product_id, quantity))
                    conn.commit()
                    flash('商品已成功加入購物車', 'success')
    except Error as e:
        print(f'Database error: {e}')
        flash('新增商品到購物車時發生錯誤，請再試一次', 'error')
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    total_price_formatted = '0'  # Initialize with a default value
    cart_items = []
    try:
        with db_connect() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute('''
                    SELECT products.name, products.price, cart.quantity, cart.product_id, products.country
                    FROM cart
                    JOIN products ON cart.product_id = products.id
                    WHERE cart.user_id = %s
                ''', (get_user_id(),))
                cart_items = cursor.fetchall()

                # 計算總價
                total_price = sum(item['price'] * item['quantity'] for item in cart_items)
                total_price_formatted = '{:,.0f}'.format(total_price)
    except Error as e:
        print(f'Database error: {e}')
        cart_items = []
    return render_template('cart.html', cart_items = cart_items, total_price = total_price_formatted)

# 新增或減少數量
@app.route('/update_quantity/<int:product_id>/<action>', methods=['POST'])
def update_quantity(product_id, action):
    # if action =='minus'，update_quantity = -1。
    update_quantity = 1 if action == 'plus' else -1
    try:
        with db_connect() as conn:
            with conn.cursor() as cursor:
                # 更新數量，使用 GREATEST 確保數量不會<1
                cursor.execute('''
                    UPDATE cart
                    SET quantity = GREATEST(1, quantity + %s)
                    WHERE user_id = %s AND product_id = %s
                ''', (update_quantity, get_user_id(), product_id))
                conn.commit()

    except Error as e:
        print(f'Database error: {e}')
    return redirect(url_for('cart'))


@app.route('/remove_cart_item/<int:product_id>', methods = ['POST'])
def remove_cart_item(product_id):
    try:
        with db_connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM cart WHERE user_id = %s AND product_id = %s',(get_user_id(), product_id,))
                conn.commit()
    except Error as e:
        print(f'Database error: {e}')
    return redirect(url_for('cart'))

@app.route('/clear_cart')
def clear_cart():
    try:
        with db_connect() as conn:
            with conn.cursor() as cursor:
                # 清空 cart 資料表
                cursor.execute('DELETE FROM cart WHERE user_id = %s',(get_user_id(),))
                conn.commit()
    except Error as e:
        print(f'Database error: {e}')
    return redirect(url_for('cart'))


if __name__ == '__main__':
    app.run( port=3000, debug=True )