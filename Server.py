
import socket
import time

port = 5050
servIp = "0.0.0.0"
addrBind = (servIp,port)
format = 'utf-8'
print(servIp)
print(socket.gethostname())
disconnect_msg = "Disconnect!"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addrBind)

def handle_client (conn, addr):
    connected = True
    while connected:
            print("connected")
            msg = conn.recv(4096).decode(format)
            print(msg)
            if msg == "what's Server host name?":
                conn.send(socket.gethostname().encode(format))
            if msg == "what time it is?":
                tNow = time.localtime()
                tSend = time.strftime("%H:%M:%S",tNow)
                conn.send(tSend.encode(format))
            if msg == disconnect_msg:
                connected = False
    conn.close()
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {servIp}")
    while True:
        conn, addr = server.accept()
        handle_client(conn,addr)

print("[STARTING] server is starting...")
start()



