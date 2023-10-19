package Java_PP.State;

// State (Estado)
interface VendingMachineState {
    void insertCoin();
    void selectProduct();
    void dispenseProduct();
}

// Concrete States (Estados Concretos)
class NoCoinState implements VendingMachineState {
    public void insertCoin() {
        System.out.println("Coin inserted.");
    }

    public void selectProduct() {
        System.out.println("Please insert a coin first.");
    }

    public void dispenseProduct() {
        System.out.println("Please select a product first.");
    }
}

class HasCoinState implements VendingMachineState {
    public void insertCoin() {
        System.out.println("You can't insert another coin.");
    }

    public void selectProduct() {
        System.out.println("Product selected.");
    }

    public void dispenseProduct() {
        System.out.println("Product dispensed.");
    }
}

// Context (Contexto)
class VendingMachine {
    private VendingMachineState state;

    public VendingMachine() {
        state = new NoCoinState();
    }

    public void setState(VendingMachineState state) {
        this.state = state;
    }

    public void insertCoin() {
        state.insertCoin();
    }

    public void selectProduct() {
        state.selectProduct();
    }

    public void dispenseProduct() {
        state.dispenseProduct();
    }
}

public class StateExample {
    public static void main(String[] args) {
        VendingMachine vendingMachine = new VendingMachine();

        vendingMachine.insertCoin();
        vendingMachine.selectProduct();
        vendingMachine.dispenseProduct();

        vendingMachine.setState(new HasCoinState());

        vendingMachine.insertCoin();
        vendingMachine.selectProduct();
        vendingMachine.dispenseProduct();
    }
}
