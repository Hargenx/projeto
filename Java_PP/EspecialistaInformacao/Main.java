public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente("Raphael");
        Pedido pedido1 = new Pedido(1, 100.0);
        Pedido pedido2 = new Pedido(2, 75.0);

        cliente.adicionarPedido(pedido1);
        cliente.adicionarPedido(pedido2);

        System.out.println("Cliente: " + cliente.getNome());
        System.out.println("Pedidos:");
        for (Pedido pedido : cliente.getPedidos()) {
            System.out.println("Pedido #" + pedido.getNumeroPedido() + ": R$" + pedido.getValorTotal());
        }
    }
}