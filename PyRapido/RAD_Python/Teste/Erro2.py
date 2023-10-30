try:
    f = open('Nomes.txt')
    s = f.readline()
    i = int(s.strip())
except (IOError, ValueError):
    print("Ocorreu um erro de E/S ou um ValueError")
except:
    print("Um erro inesperado ocorreu")
    raise

