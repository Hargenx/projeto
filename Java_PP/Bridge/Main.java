package Java_PP.Bridge;

public class Main {
    public static void main(String[] args) {
        RemoteControl physicalRemote = new PhysicalRemoteControl();
        RemoteControl mobileAppRemote = new MobileAppRemoteControl();

        Device tv = new TV(physicalRemote);
        Device smartTV = new TV(mobileAppRemote);

        tv.turnOn(); // Liga a TV fisicamente
        smartTV.turnOn(); // Liga a Smart TV pelo aplicativo móvel
    }
}