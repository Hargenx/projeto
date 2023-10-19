package Java_PP.Adapter;

public class Main {
    public static void main(String[] args) {
        LegacyPaymentSystem legacySystem = new LegacyPaymentSystem();
        PaymentGateway adapter = new LegacyPaymentAdapter(legacySystem);

        // Agora você pode usar o adapter para processar pagamentos no novo sistema
        adapter.processPayment();
    }
}