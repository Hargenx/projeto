# Importa a biblioteca pandas para manipulação de dados
import pandas as pd

# Define a classe SupermarketModel, que será responsável pela manipulação dos dados
class SupermarketModel:
    # O construtor da classe, recebe o caminho do arquivo de dados como parâmetro
    def __init__(self, data_path):
        # Lê o arquivo CSV com os dados, usando o separador ';' e indicando que a vírgula é usada como separador decimal
        self.df = pd.read_csv(data_path, sep=";", decimal=",")
        # Converte a coluna "Date" para o formato de data e hora
        self.df["Date"] = pd.to_datetime(self.df["Date"])
        # Ordena o DataFrame com base na coluna "Date"
        self.df = self.df.sort_values("Date")

    # Método para criar uma nova coluna "Month" com o ano e mês da coluna "Date"
    def create_month_column(self):
        self.df["Month"] = self.df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

    # Método para retornar os dados filtrados por mês
    def get_data_by_month(self, month):
        return self.df[self.df["Month"] == month]
