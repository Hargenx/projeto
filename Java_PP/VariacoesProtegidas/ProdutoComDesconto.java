package Java_PP.VariacoesProtegidas;

class ProdutoComDesconto extends Produto {
    private double desconto;

    public ProdutoComDesconto(String nome, double preco, double desconto) {
        super(nome, preco);
        this.desconto = desconto;
    }

    @Override
    public double getPreco() {
        return super.getPreco() - desconto;
    }
}
