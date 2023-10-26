package Java_PP.indirecao;

public class Main {
    public static void main(String[] args) {
        Conector conectorUSB = new ConectorUSB();
        Conector conectorBluetooth = new ConectorBluetooth();

        Dispositivo dispositivo1 = new Dispositivo(conectorUSB);
        Dispositivo dispositivo2 = new Dispositivo(conectorBluetooth);

        dispositivo1.conectarDispositivo();
        dispositivo2.conectarDispositivo();
    }
}