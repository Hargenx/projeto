package Java_PP.Observer;

import java.util.ArrayList;
import java.util.List;

// Subject (Sujeito)
class NewsPublisher {
    private List<Observer> observers = new ArrayList<>();
    private String news;

    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    public void publishNews(String news) {
        this.news = news;
        notifyObservers();
    }

    private void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(news);
        }
    }
}

// Observer (Observador)
interface Observer {
    void update(String news);
}

// Concrete Observers (Observadores Concretos)
class Subscriber implements Observer {
    private String name;

    public Subscriber(String name) {
        this.name = name;
    }

    public void update(String news) {
        System.out.println(name + " received news: " + news);
    }
}

public class ObserverExample {
    public static void main(String[] args) {
        NewsPublisher newsPublisher = new NewsPublisher();

        Subscriber subscriber1 = new Subscriber("Alice");
        Subscriber subscriber2 = new Subscriber("Bob");

        newsPublisher.addObserver(subscriber1);
        newsPublisher.addObserver(subscriber2);

        newsPublisher.publishNews("Breaking news: New technology released!");
    }
}
