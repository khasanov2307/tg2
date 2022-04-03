from db.connection import cursor, conn


def show_category():
    cursor.execute("select distinct category from products order by category ASC")
    conn.commit()
    return cursor.fetchall()


def show_products(category):
    cursor.execute(f"SELECT id, name, price FROM products where category = '{category}'")
    conn.commit()
    return cursor.fetchall()


def show_id_products(category):
    cursor.execute(f"select id from products where category = '{category}'")
    conn.commit()
    return cursor.fetchall()
