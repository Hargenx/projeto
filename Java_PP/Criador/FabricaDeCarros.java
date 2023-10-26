package Java_PP.Criador;

class FabricaDeCarros {
    public Carro criarCarro(String modelo, String cor) {
        return new Carro(modelo, cor);
    }
}
