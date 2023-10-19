package Java_PP.Bridge;

// Abstração dos Dispositivos
abstract class Device {
    protected RemoteControl remoteControl;

    public Device(RemoteControl remoteControl) {
        this.remoteControl = remoteControl;
    }

    public abstract void turnOn();
    public abstract void turnOff();
}