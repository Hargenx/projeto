# Importa a classe SupermarketModel do módulo model e a classe SupermarketView do módulo view
from model.model import SupermarketModel
from view.view import SupermarketView

# Define a classe SupermarketController, que será responsável por controlar a lógica do aplicativo
class SupermarketController:
    # O construtor da classe recebe o caminho do arquivo de dados como parâmetro
    def __init__(self, data_path):
        # Cria uma instância da classe SupermarketModel, passando o caminho do arquivo de dados como argumento
        self.model = SupermarketModel(data_path)
        # Cria uma instância da classe SupermarketView
        self.view = SupermarketView()

    # Método run, que executa a lógica do aplicativo
    def run(self, month):
        # Obtém os dados filtrados por mês chamando o método get_data_by_month do modelo
        df_filtered = self.model.get_data_by_month(month)
        # Chama o método display_page da visão, passando os dados filtrados como argumento
        self.view.display_page(df_filtered)
