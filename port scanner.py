import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input('Host: ')
port = input("Port: ")


def PortScanner(prt):
    if s.connect_ex((host, prt)):
        print(f"{prt} is closed")
    else:
        print(f"{prt} is up")


try:
    port = int(port)
    PortScanner(port)
except:
    if port == 'A':
        limit = int(input("Port Limit: "))
        for i in range(1, limit):
            PortScanner(i)
    else:
        print("Error! Port is unknown")