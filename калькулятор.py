a = input("Введите первое число: ")
b = input("Введите второе число: ")
c = input("Желаемое действие(+ - * /): ")
if c == "+":
    print(int(a) + int(b))
if c == "-":
    print(int(a) - int(b))
if c == "*":
    print(int(a) * int(b))
if c == "/":
    print(int(a) / int(b))
