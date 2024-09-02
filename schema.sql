CREATE DATABASE shopping_cart;
USE shopping_cart;

-- 產品資料表
CREATE TABLE products (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    price INT NOT NULL,
    country varchar(20) NOT NULL DEFAULT ''
);

-- 購物車資料表
CREATE TABLE cart(
	user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (user_id, product_id),
    foreign key (product_id) REFERENCES products(id) ON DELETE CASCADE
);
