package Java_PP.Decorator;

public class Main {
    public static void main(String[] args) {
        Cafe basicCoffee = new Cafebasico();
        System.out.println("Pedido: " + basicCoffee.description());
        System.out.println("Custo: R$ " + basicCoffee.cost());

        Cafe coffeeWithMilkAndSugar = new LeiteDecorator(new AcucarrDecorator(basicCoffee));
        System.out.println("Pedido: " + coffeeWithMilkAndSugar.description());
        System.out.println("Custo: R$ " + coffeeWithMilkAndSugar.cost());
    }
}