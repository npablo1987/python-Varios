import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE persona (rut VARCHAR(100), nombre VARCHAR(100), apellidop VARCHAR(100), apellidom VARCHAR(100), email VARCHAR(100), edad INTEGER)")

usuarios = [
            ('1-1','Pablo','Vilches','Valenzuela','kyovilches@gmail.com',34),
            ('1-2','Pablo','Vilches','Valenzuela','kyovilches@gmail.com',34),
            ('1-3','Pablo','Vilches','Valenzuela','kyovilches@gmail.com',34),
            ('1-4','Pablo','Vilches','Valenzuela','kyovilches@gmail.com',34),
            ('1-5','Pablo','Vilches','Valenzuela','kyovilches@gmail.com',34)
           ]

cursor.executemany("INSERT INTO persona VALUES (?,?,?,?,?,?)", usuarios)
conexion.commit()


cursor.execute("SELECT * from persona")
usuarios = cursor.fetchall()

for u in usuarios:
    print(u)


conexion.close()






