class Pedido {
    private int numeroPedido;
    private double valorTotal;

    public Pedido(int numeroPedido, double valorTotal) {
        this.numeroPedido = numeroPedido;
        this.valorTotal = valorTotal;
    }

    public int getNumeroPedido() {
        return numeroPedido;
    }

    public double getValorTotal() {
        return valorTotal;
    }
}