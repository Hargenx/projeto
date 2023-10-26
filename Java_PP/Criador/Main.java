package Java_PP.Criador;

public class Main {
    public static void main(String[] args) {
        FabricaDeCarros fabrica = new FabricaDeCarros();
        Carro carro = fabrica.criarCarro("Palio", "Marrom");

        System.out.println("Carro: \n\tModelo: " + carro.getModelo() + ", Cor: " + carro.getCor());
    }
}