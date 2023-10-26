package Java_PP.AcoplamentoFracoCoesaoAlta;

class PayPal implements MetodoPagamento {
    @Override
    public void efetuarPagamento(double valor) {
        System.out.println("Pagamento com PayPal no valor de R$" + valor);
    }
}
