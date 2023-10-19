package Java_PP.Bridge;

class TV extends Device {
    public TV(RemoteControl remoteControl) {
        super(remoteControl);
    }

    public void turnOn() {
        System.out.println("TV está ligada.");
        remoteControl.powerOn();
    }

    public void turnOff() {
        System.out.println("TV está desligada.");
        remoteControl.powerOff();
    }
}