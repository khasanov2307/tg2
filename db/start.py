from db.connection import cursor, conn


def db_start(message):
    cursor.execute(f"select user_id from users where user_id = {message.from_user.id}")
    conn.commit()
    user_id = cursor.fetchone()
    if user_id is None:
        cursor.execute("INSERT INTO users (user_id) VALUES(?)", (message.from_user.id,))
        conn.commit()
