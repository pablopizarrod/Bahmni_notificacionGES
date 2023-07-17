# Importar módulos

# Módulo para manejar el tiempo
import time

# Módulo para la conexión a la base de datos MySQL
import mysql.connector

# Módulo para realizar solicitudes HTTP
import requests

# Módulo para cargar variables de entorno desde un archivo .env
from dotenv import load_dotenv

# Módulo para acceder a funciones del sistema operativo
import os

# Conexión a la base de datos MySQL

# Establecer la conexión con la base de datos MySQL utilizando los valores de las variables de entorno
openmrsdb = mysql.connector.connect(
    host=os.getenv("openmrsip_var"),  # Obtener la dirección IP del host desde una variable de entorno
    user=os.getenv("user_var"),  # Obtener el nombre de usuario desde una variable de entorno
    password=os.getenv("password_var"),  # Obtener la contraseña desde una variable de entorno
    database=os.getenv("openmrs")  # Obtener el nombre de la base de datos desde una variable de entorno
)


while True:
    # Crear un cursor para ejecutar consultas en la base de datos
    openmrscursor = openmrsdb.cursor()

    # Ejecutar una consulta SQL para obtener los valores de order_id de la tabla orders
    # Filtrar por order_type_id=2 y excluir los order_id que ya existen en la tabla orderPrescriptions con un estado 'E'
    openmrscursor.execute("select obs_id from obs od where od.obs_type_id=2"
                          "and od.obs_id not in (select odp.obs_id  from obs odp"
                          "where odp.status='E')")
    
    # Obtener todos los resultados de la consulta
    openmrsResult = openmrscursor.fetchall()

    # Confirmar los cambios en la base de datos
    openmrsdb.commit()

    # Iterar sobre cada resultado obtenido
    for resul in openmrsResult:
        try:
            # Construir una sentencia SQL para insertar un nuevo registro en la tabla orderPrescriptions
            # con el order_id, un prescriptor_id de 'apiDaemon', un estado 'E' y la fecha actual
            stmtq ="insert into obs (obs_id,creator,status,date_created)values("+str(resul[0])+",'apiDaemon','E',CURDATE())"
            
            # Ejecutar la sentencia SQL
            openmrscursor.execute(stmtq)
            
            # Confirmar los cambios en la base de datos
            openmrsdb.commit()
        except:
            True
    
    # Pausar la ejecución durante 5 segundos
    time.sleep(5)
