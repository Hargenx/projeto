package Java_PP.indirecao;

class Dispositivo {
    private Conector conector;

    public Dispositivo(Conector conector) {
        this.conector = conector;
    }

    public void conectarDispositivo() {
        conector.conectar();
    }
}
