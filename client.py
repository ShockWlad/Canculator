from os import system
import socket

client = socket.socket()
client.connect(('localhost', 9001))

data = client.recv(1024)
print(data.decode("utf_8"))
number = input()
client.send(number.encode("utf_8"))

if number == '1':
    while True:
        data = client.recv(1024)
        print(data.decode("utf_8"))
        n = input()
        client.send(n.encode("utf_8"))
        if n == 'q': break
        else:
            data = client.recv(1024)
            print(data.decode("utf_8"))
            client.send(input().encode("utf_8"))

            data = client.recv(1024)
            print(data.decode("utf_8"))
            client.send(input().encode("utf_8"))

            data = client.recv(1024)
            print(data.decode("utf_8"))
            system('cls')
            continue



elif number == '2':
    while True:
        data = client.recv(1024)
        print(data.decode("utf_8"))
        n = input()
        client.send(n.encode("utf_8"))
        if n == 'q': break
        elif n == 'tg':
            data = client.recv(1024)
            print(data.decode("utf_8"))
            client.send(input().encode("utf_8"))

            data = client.recv(1024)
            print(data.decode("utf_8"))
            system('cls')
            continue
        else:
            data = client.recv(1024)
            print(data.decode("utf_8"))
            client.send(input().encode("utf_8"))

            data = client.recv(1024)
            print(data.decode("utf_8"))
            client.send(input().encode("utf_8"))

            data = client.recv(1024)
            print(data.decode("utf_8"))
            system('cls')
            continue

elif number == '3':
    client.close()
