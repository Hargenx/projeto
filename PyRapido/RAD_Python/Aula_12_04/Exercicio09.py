def soma_divisor(numero):
    try:
        divisor = [1]
        for i in range(2, (numero + 1)):
            if (numero % i) == 0:
                divisor.append(i)
    except TypeError as te:
        print(f"Ocorreu um erro: {te}")
    except ValueError as ve:
        print(f"Ocorreu um erro: {ve}")
    else:
        return sum(divisor)


if __name__ == "__main__":
    print(soma_divisor(8))
    print(soma_divisor(12))
    print(soma_divisor(10))
    print(soma_divisor(98))
# 0	    1, 2, 3, 4, 5, 6, 7, 8, ...
# 1	    1
# 2	    1, 2
# 3	    1, 3
# 4	    1, 2, 4
# 5 	1, 5
# 6	    1, 2, 3, 6
# 7	    1, 7
# 8	    1, 2, 4, 8
# 9	    1, 3, 9
# 10	1, 2, 5, 10
# 11	1, 11
# 12	1, 2, 3, 4, 6, 12
# 13	1, 13
# 14	1, 2, 7, 14
# 15	1, 3, 5, 15
# 16	1, 2, 4, 8, 16
# 17	1, 17
# 18	1, 2, 3, 6, 9, 18
# 19	1, 19
# 20	1, 2, 4, 5, 10, 20
# 21	1, 3, 7, 21
# 22	1, 2, 11, 22
# 23	1, 23
# 24	1, 2, 3, 4, 6, 8, 12, 24
# 25	1, 5, 25
# 26	1, 2, 13, 26
# 27	1, 3, 9, 27
# 28	1, 2, 4, 7, 14, 28
# 29	1, 29
# 30	1, 2, 3, 5, 6, 10, 15, 30
