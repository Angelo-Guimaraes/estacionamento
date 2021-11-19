import pymysql
import datetime

#Conexão à BD
conn = pymysql.connect(host="localhost", user="root", passwd="", db="estacionamento")
myCursor = conn.cursor()


myCursor.execute("""CREATE TABLE lugares
   (
    id int AUTO_INCREMENT primary key,
    lugar int,
    matricula varchar(20),
    hora_entrada datetime,
    hora_saida datetime
    )
 """)
