package Java_PP.Polimorfismo;

public class Main {
    public static void main(String[] args) {
        Animal cachorro = new Cachorro();
        Animal gato = new Gato();

        cachorro.emitirSom();
        gato.emitirSom();
    }
}