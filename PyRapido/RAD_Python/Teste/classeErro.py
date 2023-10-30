class TemperaturaInvalida(Exception):
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def __str__(self):
        return f'A temperatura {self.temperatura} está abaixo do limite'

if __name__ == '__main__':
    try:
        raise TemperaturaInvalida(30)
    except TemperaturaInvalida as e:
        print('Erro: ', e)