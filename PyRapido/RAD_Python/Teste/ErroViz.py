def divisao():
    list1 = [-1, 0, 1]
    for i in list1:
        if i == 0:
            raise ZeroDivisionError("Erro por divisão por zero.")

if __name__ == '__main__':
    try:
        divisao()
    except ZeroDivisionError as e:
        print(e)