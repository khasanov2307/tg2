from db.connection import cursor, conn


def search_products(name_product1, name_product2):
    cursor.execute(f"select id, name, category, price from products WHERE products.name LIKE '%{name_product1}%' or "
                   f"products.name "
                   f"like '%{name_product2}%'")
    conn.commit()
    return cursor.fetchall()


def search_id(product_id):
    cursor.execute(f"select id, name, category, price from products WHERE products.id = '{product_id}'")
    conn.commit()
    return cursor.fetchall()


def change_price(new_price, product_id):
    cursor.execute(f"update products set price = {new_price} where id = {product_id}")
    conn.commit()


def search_users():
    cursor.execute(f"select user_id from users")
    conn.commit()
    return cursor.fetchall()


def count_users():
    cursor.execute(f"select count(*) from users")
    conn.commit()
    return cursor.fetchone()
