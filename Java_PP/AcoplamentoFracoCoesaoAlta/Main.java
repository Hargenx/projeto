package Java_PP.AcoplamentoFracoCoesaoAlta;

public class Main {
    public static void main(String[] args) {
        GerenciadorDePagamentos gerenciador = new GerenciadorDePagamentos();
        CarrinhoCompras carrinho = new CarrinhoCompras();
        Produto produto1 = new Produto("Notebook", 2500.0);
        Produto produto2 = new Produto("Smartphone", 1000.0);
        carrinho.adicionarProduto(produto1);
        carrinho.adicionarProduto(produto2);

        MetodoPagamento cartao = new CartaoCredito();
        gerenciador.processarPagamento(carrinho, cartao);

        MetodoPagamento paypal = new PayPal();
        gerenciador.processarPagamento(carrinho, paypal);
    }
}
