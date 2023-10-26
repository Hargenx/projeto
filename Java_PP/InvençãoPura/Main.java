package Java_PP.InvençãoPura;

public class Main {
    public static void main(String[] args) {
        Motor motor = new Motor();
        Roda roda = new Roda();
        Carro carro = new Carro(motor, roda);

        carro.acelerar();
    }
}