package Java_PP.Controlador;

class GerenciadorDePedidos {
    public Pedido criarPedido(int produtoId, int quantidade) {
        // Lógica para criar um pedido
        return new Pedido(produtoId, quantidade);
    }

    public void finalizarPedido(Pedido pedido) {
        // Lógica para finalizar um pedido
    }
}