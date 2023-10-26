package Java_PP.AcoplamentoFracoCoesaoAlta;

class GerenciadorDePagamentos {
    public void processarPagamento(CarrinhoCompras carrinho, MetodoPagamento metodo) {
        double total = carrinho.calcularTotal();
        metodo.efetuarPagamento(total);
    }
}
