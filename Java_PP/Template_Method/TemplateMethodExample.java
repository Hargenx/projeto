package Java_PP.Template_Method;

// Abstract Class
abstract class OrderProcessor {
    public void processOrder() {
        selectProduct();
        calculateTotal();
        payment();
        printReceipt();
    }

    protected abstract void selectProduct();
    protected abstract void calculateTotal();
    protected abstract void payment();
    protected abstract void printReceipt();
}

// Concrete Class
class OnlineOrderProcessor extends OrderProcessor {
    protected void selectProduct() {
        System.out.println("Product selected online.");
    }

    protected void calculateTotal() {
        System.out.println("Total calculated online.");
    }

    protected void payment() {
        System.out.println("Payment processed online.");
    }

    protected void printReceipt() {
        System.out.println("Receipt sent via email.");
    }
}

public class TemplateMethodExample {
    public static void main(String[] args) {
        OrderProcessor processor = new OnlineOrderProcessor();
        processor.processOrder();
    }
}
