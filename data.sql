CREATE DATABASE shopping_cart;
SHOW databases;
USE shopping_cart;

-- 產品資料表
CREATE TABLE products (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    price INT NOT NULL
);
SHOW TABLES;
SELECT * FROM products;
INSERT INTO products(name, price) VALUES('富士蘋果', 40);
INSERT INTO products(name, price) VALUES('愛妃蘋果', 80);
INSERT INTO products(name, price) VALUES('葡萄柚', 60);
INSERT INTO products(name, price) VALUES('麝香葡萄', 700);
INSERT INTO products(name, price) VALUES('水梨', 80);

DELETE FROM products WHERE id=6;
-- 使用 ALTER TABLE 為name添加「唯一」索引
ALTER TABLE products ADD CONSTRAINT unique_name UNIQUE (name);

ALTER TABLE products ADD country varchar(255) NOT NULL DEFAULT '';
ALTER TABLE products DROP COLUMN country;
-- 臨時禁用安全更新模式
SET SQL_SAFE_UPDATES = 0;
UPDATE products SET country='韓國' WHERE name = '水梨';
-- 重新啟用安全更新模式
SET SQL_SAFE_UPDATES = 1;


-- 購物車資料表
CREATE TABLE cart(
	user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (user_id, product_id),
    foreign key (product_id) REFERENCES products(id) ON DELETE CASCADE
);
SELECT * FROM cart;

SELECT products.name, products.price, cart.quantity FROM cart JOIN products ON cart.product_id = products.id;

SELECT products.name, products.price, cart.quantity, cart.product_id, products.country
                    FROM cart
                    JOIN products ON cart.product_id = products.id
                    WHERE cart.user_id = 1;
                    -- GROUP BY cart.product_id;
                    
-- 移除資料表中的所有資料列
TRUNCATE TABLE cart;
DROP TABLE cart;

-- 如果插入的 user_id 和 product_id 的组合已經存在於 cart 表中，
-- 則不會插入新紀錄，而是更新現有紀錄的 quantity
-- INSERT INTO cart(user_id, product_id, quantity)
--                    VALUES(%s, %s, %s)', (user_id, product_id, quantity)
--                    ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity)



