import socket
import math

class Standard :
    def adder (v,x,y):
        if v == '+':
            return x + y
        elif v == '-':
            return x - y
        elif v == '*':
            return x * y
        elif v == '/':
            if y != 0:
                return x / y
class Engineering (Standard):
    def adder2 (v,x):
        if v == 'tg':
            if -90 <= x <= 90 :
                return math.tan(x)

sock = socket.socket()
sock.bind(('localhost', 9001))
sock.listen(1)

user, addres = sock.accept()

menu = "Выберите действие которое хотите сделать:\n""Стандартный: 1\n""Инженерный: 2\n""Выйти: 3"
user.send(menu.encode("utf-8"))
data = user.recv(1024)
number = int(data.decode("utf_8"))

if (number == 1):
    while True:
        menu = "\nВыберите действие которое хотите сделать:\n""Сложить: +\n""Вычесть: -\n""Умножить: *\n""Поделить: /\n""Выйти: q"
        user.send(menu.encode("utf-8"))
        data = user.recv(1024)
        v = data.decode("utf_8")

        user.send("Напишите любое первое число: ".encode("utf-8"))
        data = user.recv(1024)
        x = int(data.decode("utf_8"))

        user.send("Напишите любое второе число: ".encode("utf-8"))
        data = user.recv(1024)
        y = int(data.decode("utf_8"))

        user.send("Результат :".encode("utf-8"))
        result = Standard.adder(v,x,y)
        user.send(str(result).encode("utf-8"))
        print(result)
elif (number == 2):
    while True:
        menu = "\nВыберите действие которое хотите сделать:\n""Сложить: +\n""Вычесть: -\n""Умножить: *\n""Поделить: /\n""Тангенс(-90 до 90): tg\n""Выйти: q"
        user.send(menu.encode("utf-8"))

        data = user.recv(1024)
        v = data.decode("utf_8")
        if v == 'tg':
            user.send("Напишите любое первое число: ".encode("utf-8"))
            data = user.recv(1024)
            x = int(data.decode("utf_8"))

            user.send("Результат :".encode("utf-8"))
            result = Engineering.adder2(v, x)
            user.send(str(result).encode("utf-8"))
            print(result)
        else:
            user.send("Напишите любое первое число: ".encode("utf-8"))
            data = user.recv(1024)
            x = int(data.decode("utf_8"))

            user.send("Напишите любое второе число: ".encode("utf-8"))
            data = user.recv(1024)
            y = int(data.decode("utf_8"))

            user.send("Результат :".encode("utf-8"))
            result = Engineering.adder(v,x,y)
            if result != None :user.send(str(result).encode("utf-8"))
            print (result)