package Java_PP.Memento;

// Memento
class DocumentMemento {
    private String content;

    public DocumentMemento(String content) {
        this.content = content;
    }

    public String getContent() {
        return content;
    }
}

// Originator
class Document {
    private String content;

    public void setContent(String content) {
        this.content = content;
    }

    public DocumentMemento createMemento() {
        return new DocumentMemento(content);
    }

    public void restoreMemento(DocumentMemento memento) {
        content = memento.getContent();
    }

    public void printContent() {
        System.out.println("Document Content: " + content);
    }
}

public class MementoExample {
    public static void main(String[] args) {
        Document document = new Document();
        document.setContent("Hello, World!");

        document.printContent();

        DocumentMemento memento = document.createMemento();

        document.setContent("This is a new content.");
        document.printContent();

        document.restoreMemento(memento);
        document.printContent();
    }
}
