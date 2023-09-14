import pyodbc

# Establecer conexión al DSN
conn_str = 'DSN=MySQL_TFG'
conn = pyodbc.connect(conn_str)

# Crear un cursor
cursor = conn.cursor()

while True:
    # Solicitar consulta al usuario
    query = input("Ingrese su consulta SQL (o 'exit' para salir): ")
    
    # Si el usuario ingresa 'exit', sal del bucle
    if query.lower() == 'exit':
        break

    try:
        cursor.execute(query)
        try:
            for row in cursor:
                print(' '.join(map(str, row)))

        except pyodbc.ProgrammingError:
            print("La consulta se ejecutó con éxito pero no devolvió resultados.")
        
    except pyodbc.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
    except Exception as e:
        print(f"Error al ejecutar consulta: {e}")

# Cerrar conexión
conn.close()