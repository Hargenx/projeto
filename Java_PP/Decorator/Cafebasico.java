package Java_PP.Decorator;

// Componente Concreto
class Cafebasico implements Cafe {
    public double cost() {
        return 2.0;
    }

    public String description() {
        return "Café simples";
    }
}