package Java_PP.AcoplamentoBaixo;

class Aplicativo {
    private Impressora impressora;

    public Aplicativo(Impressora impressora) {
        this.impressora = impressora;
    }

    public void imprimirDocumento(String documento) {
        impressora.imprimir(documento);
    }
}