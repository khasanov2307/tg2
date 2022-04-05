from db.connection import cursor, conn


def search_products(name_product1, name_product2):
    cursor.execute(f"select name, category, price from products WHERE products.name LIKE '%{name_product1}%' or "
                   f"products.name "
                   f"like '%{name_product2}%'")
    conn.commit()
    return cursor.fetchall()
