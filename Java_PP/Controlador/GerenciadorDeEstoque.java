package Java_PP.Controlador;

class GerenciadorDeEstoque {
    public boolean verificarDisponibilidade(int produtoId, int quantidade) {
        // Lógica para verificar a disponibilidade de produtos em estoque
        if(quantidade > 0){
            return true;
        }else{
            return false;
        }
    }

    public void atualizarEstoque(int produtoId, int quantidade) {
        // Lógica para atualizar o estoque após o processamento do pedido
    }
}