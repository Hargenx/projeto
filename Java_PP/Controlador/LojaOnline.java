package Java_PP.Controlador;

class LojaOnline {
    private GerenciadorDePedidos gerenciadorDePedidos;
    private GerenciadorDeEstoque gerenciadorDeEstoque;

    public LojaOnline() {
        gerenciadorDePedidos = new GerenciadorDePedidos();
        gerenciadorDeEstoque = new GerenciadorDeEstoque();
    }

    public void processarPedido(int produtoId, int quantidade) {
        Pedido pedido = gerenciadorDePedidos.criarPedido(produtoId, quantidade);
        boolean disponivel = gerenciadorDeEstoque.verificarDisponibilidade(produtoId, quantidade);

        if (disponivel) {
            gerenciadorDePedidos.finalizarPedido(pedido);
            gerenciadorDeEstoque.atualizarEstoque(produtoId, quantidade);
            System.out.println("Pedido processado com sucesso.");
        } else {
            System.out.println("Produto fora de estoque. Pedido não processado.");
        }
    }
}