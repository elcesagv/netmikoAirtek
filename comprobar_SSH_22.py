from netmiko import ConnectHandler
from lista_cpes import devicesTotal
from lista_cpes import devices


for device in devices:
    try:
        #realiza la conexion con el equipo
        connection= ConnectHandler(**device)
        #imprime si la conexion esta bien echa
        print(f"conexion exitosa a la IP: {device['ip']}")
        #configura el ip service con ssh port 60022
        comandos = connection.send_command("ip service set  address=190.124.28.62/32 port=60022")
        print(comandos)
    except Exception as e:
        print(f"error conectando a la IP: {device['ip']}")
        print(f"el error es {e}")
        print()
        



    





