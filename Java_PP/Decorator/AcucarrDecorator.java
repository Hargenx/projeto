package Java_PP.Decorator;

class AcucarrDecorator extends CafeDecorator {
    public AcucarrDecorator(Cafe decoratedCoffee) {
        super(decoratedCoffee);
    }

    public double cost() {
        return super.cost() + 0.2;
    }

    public String description() {
        return super.description() + ", Açúcar";
    }
}