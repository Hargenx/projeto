package Java_PP.Bridge;

class MobileAppRemoteControl implements RemoteControl {
    public void powerOn() {
        System.out.println("Ligando o dispositivo pelo aplicativo móvel.");
    }

    public void powerOff() {
        System.out.println("Desligando o dispositivo pelo aplicativo móvel.");
    }
}