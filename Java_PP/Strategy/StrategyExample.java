package Java_PP.Strategy;

import java.util.Arrays;

// Strategy
interface SortingStrategy {
    void sort(int[] arr);
}

// Concrete Strategies
class BubbleSort implements SortingStrategy {
    public void sort(int[] arr) {
        // Implementação do Bubble Sort
        System.out.println("Bubble Sort");
        Arrays.sort(arr);
    }
}

class QuickSort implements SortingStrategy {
    public void sort(int[] arr) {
        // Implementação do Quick Sort
        System.out.println("Quick Sort");
        Arrays.sort(arr);
    }
}

// Context
class Sorter {
    private SortingStrategy strategy;

    public void setStrategy(SortingStrategy strategy) {
        this.strategy = strategy;
    }

    public void performSort(int[] arr) {
        strategy.sort(arr);
    }
}

public class StrategyExample {
    public static void main(String[] args) {
        int[] arr = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};

        Sorter sorter = new Sorter();
        sorter.setStrategy(new BubbleSort());
        sorter.performSort(arr);

        sorter.setStrategy(new QuickSort());
        sorter.performSort(arr);
    }
}
