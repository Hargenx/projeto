package Java_PP.Adapter;

// Adapter para o Sistema Legado
class LegacyPaymentAdapter implements PaymentGateway {
    private LegacyPaymentSystem legacySystem;

    public LegacyPaymentAdapter(LegacyPaymentSystem legacySystem) {
        this.legacySystem = legacySystem;
    }

    public void processPayment() {
        legacySystem.processPaymentLegacy();
    }
}