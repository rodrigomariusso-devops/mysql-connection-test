import mysql.connector

config = {
    'user': '',
    'password': '',
    'host': '',
    'database': '',
}

try:
    print("Conectando ao banco de dados...")
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Conexão bem-sucedida!")

    query = "SELECT * FROM ras_pre_evento"
    print(f"Executando a query: {query}")
    cursor.execute(query)

    results = cursor.fetchall()
    if results:
        print("Resultados encontrados:")
        for row in results:
            print(row)
    else:
        print("Nenhum resultado encontrado.")

except mysql.connector.Error as err:
    print(f"Erro: {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Conexão fechada.")
