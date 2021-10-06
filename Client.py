
import socket

port = 5050

disconnect_msg = "Disconnect!"

#formt to encode and decode messages to byte form.
format = 'utf-8'

ServerIp = input("Enter ipv4 format of server, "
                 "if clent and server run on same machine  press Y: ")
if(ServerIp.upper() == "Y"):
    ServerIp = "127.0.0.1"
else:
    ServerIp = input("Enter Ip: ")

addr = (ServerIp,port)
#Creating socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#binding client socket with tuple of port number and ipv4 string.
client.connect(addr)

#function to send messages to server and print ans.
def send(msg):
    client.send(msg.encode(format))
    print(client.recv(4096).decode(format))

print("computer name is:")
send("what's Server host name?")
print("Current time is:")
send("what time it is?")
send(disconnect_msg)
client.close()


