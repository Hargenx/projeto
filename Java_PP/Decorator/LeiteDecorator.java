package Java_PP.Decorator;

// Decoradores Concretos
class LeiteDecorator extends CafeDecorator {
    public LeiteDecorator(Cafe decoratedCoffee) {
        super(decoratedCoffee);
    }

    public double cost() {
        return super.cost() + 0.5;
    }

    public String description() {
        return super.description() + ", Leite";
    }
}