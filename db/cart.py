from db.connection import cursor, conn


def show_user_cart(message):
    cursor.execute(
        f'select products.name, count(*)*products.price, count(*), price from shopping_cart '
        f'join products on shopping_cart.product_id = products.id '
        f'where user_id=\'{message.from_user.id}\' group by products.id')
    conn.commit()
    return cursor.fetchall()


def add_product(count_product, callback_query, product_id):
    for i in range(int(count_product)):
        #print(count_product)
        cursor.execute("INSERT INTO shopping_cart (user_id, product_id) VALUES(?, ?)",
                       (callback_query.from_user.id, int(product_id)))
    conn.commit()


def clear_cart(callback_query):
    cursor.execute(f"DELETE FROM shopping_cart WHERE user_id = {callback_query.from_user.id}")
    conn.commit()
