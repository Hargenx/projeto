package Java_PP.InvençãoPura;

class Carro {
    private Motor motor;
    private Roda roda;

    public Carro(Motor motor, Roda roda) {
        this.motor = motor;
        this.roda = roda;
    }

    public void acelerar() {
        motor.ligar();
        roda.girar();
    }
}
