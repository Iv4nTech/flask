import psycopg2

conexion = psycopg2.connect(database = 'bd_flask', user='usuario', host='127.0.0.1', password='usuario1234', port=5432)

cursor = conexion.cursor()
# cursor.execute("""CREATE TABLE alumno(
#                alumno_id SERIAL PRIMARY KEY,
#                alumno_name VARCHAR(25) NOT NULL,
#                alumno_surname VARCHAR(50) NULL,
#                alumno_fecha_nac DATE NULL);
#                """)
# cursor.execute("""INSERT INTO alumno(alumno_name, alumno_surname, alumno_fecha_nac)
#                VALUES('Iván', 'Gómez Jiménez', '06-03-2005');
# """)

cursor.execute("""SELECT alumno_name FROM alumno;
 """)

rows = cursor.fetchall()
conexion.commit()
cursor.close()
conexion.close()

for row in rows:
    print(row)