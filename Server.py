
import socket
import time

port = 5050
servIp = "0.0.0.0"
addrBind = (servIp,port)

#formt to encode and decode messages to byte form.
format = 'utf-8'

disconnect_msg = "Disconnect!"

#Creating socket object 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#binding server socket with tuple of port number and ipv4 string.
server.bind(addrBind)

#function handels reciving and sending messages from client to server.
def handle_client (conn, addr):
    connected = True
    while connected:
            msg = conn.recv(4096).decode(format)
            
            if msg == "what's Server host name?":
                conn.send(socket.gethostname().encode(format))
            if msg == "what time it is?":
                tNow = time.localtime()
                tSend = time.strftime("%H:%M:%S",tNow)
                conn.send(tSend.encode(format))
            if msg == disconnect_msg:
                connected = False
    conn.close()
#function that starts the program and the initial connection
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {servIp}")
    while True:
        conn, addr = server.accept()
        handle_client(conn,addr)

print("[STARTING] server is starting...")
start()



