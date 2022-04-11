from db.connection import cursor, conn


def search_products(name_product1, name_product2):
    cursor.execute(f"select id, name, category, price from products WHERE products.name LIKE '%{name_product1}%' or "
                   f"products.name "
                   f"like '%{name_product2}%'")
    conn.commit()
    return cursor.fetchall()


def search_users():
    cursor.execute(f"select user_id from users")
    conn.commit()
    return cursor.fetchall()