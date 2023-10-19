package Java_PP.Bridge;

class PhysicalRemoteControl implements RemoteControl {
    public void powerOn() {
        System.out.println("Ligando o dispositivo fisicamente.");
    }

    public void powerOff() {
        System.out.println("Desligando o dispositivo fisicamente.");
    }
}