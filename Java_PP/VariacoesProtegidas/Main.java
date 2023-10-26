package Java_PP.VariacoesProtegidas;

public class Main {
    public static void main(String[] args) {
        Produto produto = new Produto("Jogos", 300.0);
        ProdutoComDesconto produtoComDesconto = new ProdutoComDesconto("Jogos em Promoção", produto.getPreco(), 250.0);

        System.out.println("Preço do Produto: R$" + produto.getPreco());
        System.out.println("Preço do Produto com Desconto: R$" + produtoComDesconto.getPreco());
    }
}