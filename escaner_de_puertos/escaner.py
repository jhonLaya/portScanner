import socket

conection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ports = [21, 22, 23, 25, 53, 80, 101, 123, 137, 138, 139, 443, 445, 587, 591, 3306, 5000, 8000]

def port_scan(ports, ip):
    """ Dados una lista de puertos y una ip, retorna los puertos abiertos

        Args:
        ports (list): lista de puertos
        ip (str): ip a escanear

        Returns:
        (str): mensaje con el puerto abierto
    """
    for port in ports:
        resultado = conection.connect_ex((ip, port))
        if resultado == 0:
            print('[+]El puerto {} esta abierto'.format(port))



if __name__ == '__main__':
    port_scan(ports, '192.168.1.108')
