import mysql.connector


def get_mysql_data():
    conn = mysql.connector.connect(
        host='localhost',      # your MySQL host
        user='your_username',  # your MySQL username
        password='your_password',  # your MySQL password
        database='your_database'   # your database name
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT month, net_profit_margin FROM profit_margins ORDER BY month")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    months = [row[0] for row in data]
    margins = [row[1] for row in data]
    return months, margins
