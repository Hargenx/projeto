package Java_PP.Decorator;

// Decorador
abstract class CafeDecorator implements Cafe {
    protected Cafe decoratedCoffee;

    public CafeDecorator(Cafe decoratedCoffee) {
        this.decoratedCoffee = decoratedCoffee;
    }

    public double cost() {
        return decoratedCoffee.cost();
    }

    public String description() {
        return decoratedCoffee.description();
    }
}