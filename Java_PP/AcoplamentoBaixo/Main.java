package Java_PP.AcoplamentoBaixo;

public class Main {
    public static void main(String[] args) {
        Impressora impressora = new Impressora();
        Aplicativo aplicativo = new Aplicativo(impressora);

        aplicativo.imprimirDocumento("Documento de teste.");
    }
}