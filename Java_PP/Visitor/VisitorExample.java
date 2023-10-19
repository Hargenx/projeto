package Java_PP.Visitor;

// Element (Elemento)
interface DocumentElement {
    void accept(Visitor visitor);
}

// Concrete Elements (Elementos Concretos)
class TextElement implements DocumentElement {
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}

class ImageElement implements DocumentElement {
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}

// Visitor (Visitante)
interface Visitor {
    void visit(TextElement text);
    void visit(ImageElement image);
}

// Concrete Visitor (Visitante Concreto)
class DocumentExporter implements Visitor {
    public void visit(TextElement text) {
        System.out.println("Exporting text element");
    }

    public void visit(ImageElement image) {
        System.out.println("Exporting image element");
    }
}

public class VisitorExample {
    public static void main(String[] args) {
        DocumentElement[] elements = {new TextElement(), new ImageElement()};
        DocumentExporter exporter = new DocumentExporter();

        for (DocumentElement element : elements) {
            element.accept(exporter);
        }
    }
}
