package Java_PP.AcoplamentoFracoCoesaoAlta;

class CartaoCredito implements MetodoPagamento {
    @Override
    public void efetuarPagamento(double valor) {
        System.out.println("Pagamento com cartão de crédito no valor de R$" + valor);
    }
}