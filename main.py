import pymysql
import datetime

#funcao de inserção de dados na db
def insert_matricula(id, lugar, matricula, hora_entrada):
    try:
        conn = pymysql.connect(host="localhost", user="root", passwd="", db="estacionamento")

        myCursor = conn.cursor()
        insert_matricula = """INSERT INTO lugares (id, lugar, matricula, hora_entrada) 
                                VALUES (%s, %s, %s, %s) """

        record = (id, lugar, matricula, hora_entrada)
        myCursor.execute(insert_matricula, record)
        conn.commit()
    except pymysql.connect.Error as error:
        print("Erro a inserir na base de dados {}".format(error))

        if conn.is_connected():
            myCursor.close()
            conn.close()

#update da hora de saída
def update_hora(hora_saida, lugar):

    try:
        conn = pymysql.connect(host="localhost", user="root", passwd="", db="estacionamento")
        myCursor = conn.cursor()

        sql_update = """UPDATE lugares 
                        SET hora_saida = %s 
                        WHERE lugar = %s"""
        record = (hora_saida, lugar)
        myCursor.execute(sql_update, record)
        conn.commit()

    except pymysql.connect.Error as error:

        print("Erro a atualizar a hora {}".format(error))
        if conn.is_connected():
            myCursor.close()
            conn.close()

#Apagar dados ao sair
def delete_lugar():
    delete_lugar = "DELETE FROM lugares WHERE lugar = "+alugar2+""
    myCursor = conn.cursor()
    myCursor.execute(delete_lugar)
    conn.commit()

#Menu principal
def menu():
    print("Parque de Estacionamento\n")
    print("1- Consultar lugares")
    print("2- Inserir matricula")
    print("3- Sair do parque")
    print("4- Terminar programa")

#Chamar menu
menu()
option = int(input("\nEscolha uma opção:"))

#While de options
while option != 0:
    if option == 1:
        print("\nConsultar lugares")
        conn = pymysql.connect(host="localhost", user="root", passwd="", db="estacionamento")
        select_matricula = "SELECT * FROM lugares ORDER BY lugar"
        myCursor = conn.cursor()
        myCursor.execute(select_matricula)
        print("\nNumero total de lugares ocupados:", myCursor.rowcount)
        print("Numero total de lugares disponiveis:", 50 - myCursor.rowcount)
        print("\nLista de lugares: \n")
        dados_veiculos = myCursor.fetchall()
        for row in dados_veiculos:
            print("Lugar: ", row[1], "     Matrícula: ", row[2])
            print("Hora entrada: ", row[3], "\n")
        menu()
        option = int(input("\nEscolha uma opção:\n"))
    elif option == 2:
        #Inserção de dados
        print("\nIntroduza os seus dados")
        aid = id
        conn = pymysql.connect(host="localhost", user="root", passwd="", db="estacionamento")
        select_matricula = "SELECT * FROM lugares ORDER BY lugar"
        myCursor = conn.cursor()
        myCursor.execute(select_matricula)
        print("\nNumero total de lugares disponiveis:", 50 - myCursor.rowcount)
        row_lugares = myCursor.fetchall()
        print("\nLugares indisponíveis: (1-50)")
        print("\nLugares Ocupados:")
        for row in row_lugares:
            print(row[1], end="  ")
        alugar = int(input("\nEscolha um lugar:"))
        myCursor.execute("SELECT lugar, COUNT(*) FROM lugares WHERE lugar = %s GROUP BY lugar", (alugar,))
        row_count = myCursor.rowcount
        while row_count != 0:
            print("\nJá se encontra ocupado.")
            alugar = int(input("\nEscolha um lugar:"))
            myCursor.execute("SELECT lugar, COUNT(*) FROM lugares WHERE lugar = %s GROUP BY lugar", (alugar,))
            row_count = myCursor.rowcount
        amatricula = input("Escreva matricula: ")
        ahora_entrada = datetime.datetime.now()
        insert_matricula(aid, alugar, amatricula, ahora_entrada)
        print("Adicionado com sucesso\n\n")
        menu()
        option = int(input("\nEscolha uma opção:\n"))
    elif option == 3:
        print("\nSair do parque: ")
        ahora_saida = datetime.datetime.now()
        alugar2 = input("Introduza o lugar a que se encontra estacionado (1-50):")
        update_hora(ahora_saida, alugar2)
        conn = pymysql.connect(host="localhost", user="root", passwd="", db="estacionamento")
        select_matricula = "SELECT * FROM lugares WHERE lugar = "+alugar2+""
        myCursor = conn.cursor()
        myCursor.execute(select_matricula)
        dados_veiculo = myCursor.fetchall()
        for row in dados_veiculo:
            print("Lugar: ", row[1], "")
            print("Matrícula: ", row[2])
            print("Hora entrada: ", row[3])
            print("Hora saída: ", row[4])
        time_min = (row[4] - row[3])
        total_seconds = time_min.total_seconds()
        minutes = total_seconds / 60
        print("\nEsteve no parque: {:.0f}".format(minutes), "minutos\n")
        if minutes <= 15:
            print("Valor a pagar: 0.20€")
        elif minutes <= 30:
            print("Valor a pagar: 0.40€")
        elif minutes <= 60:
            print("Valor a pagar: 0.60€")
        elif minutes <= 120:
            print("Valor a pagar: 0.80€")
        elif minutes <= 180:
            print("Valor a pagar: 2.80€")
        elif minutes <= 205:
            print("Valor a pagar: 3.05€")
        elif minutes <= 220:
            print("Valor a pagar: 3.30€")
        elif minutes <= 235:
            print("Valor a pagar: 3.60€")
        else:
            print("Tempo excedido, o seu carro irá ser rebocado")
        delete_lugar()
        print("Obrigado e boa viagem!")
        break
    elif option == 4:
        exit()
    else:
        print("\nErro, introduza uma opção válida\n")
        menu()
        option = int(input("\nEscolha uma opção:\n"))
