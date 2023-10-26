import java.util.ArrayList;
import java.util.List;

class Cliente {
    private String nome;
    private List<Pedido> pedidos;

    public Cliente(String nome) {
        this.nome = nome;
        this.pedidos = new ArrayList<>();
    }

    public void adicionarPedido(Pedido pedido) {
        pedidos.add(pedido);
    }

    public String getNome() {
        return nome;
    }

    public List<Pedido> getPedidos() {
        return pedidos;
    }
}

