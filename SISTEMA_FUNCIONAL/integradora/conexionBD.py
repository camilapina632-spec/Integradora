import mysql.connector

try:
    conexion=mysql.connector.connect(
        host="127.0.0.1",
        user='root',
        password='',
        database='bd_blibioteca'
    )
    cursor=conexion.cursor(buffered=True)

except:
    print(f"...¡Por el momento no es posible conectarse con la base de datos intentelo mas tarde!...")
    