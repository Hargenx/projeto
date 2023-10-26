package Java_PP.indirecao;

interface Conector {
    void conectar();
}

class ConectorUSB implements Conector {
    @Override
    public void conectar() {
        System.out.println("Conectado via USB.");
    }
}
