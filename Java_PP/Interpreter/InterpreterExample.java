package Java_PP.Interpreter;

// Abstract Expression
interface Expression {
    int interpret();
}

// Terminal Expression
class NumberExpression implements Expression {
    private int number;

    public NumberExpression(int number) {
        this.number = number;
    }

    public int interpret() {
        return number;
    }
}

// Non-Terminal Expression
class AddExpression implements Expression {
    private Expression left;
    private Expression right;

    public AddExpression(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    public int interpret() {
        return left.interpret() + right.interpret();
    }
}

public class InterpreterExample {
    public static void main(String[] args) {
        // Parse expression: 2 + 3
        Expression expression = new AddExpression(new NumberExpression(2), new NumberExpression(3));

        int result = expression.interpret();
        System.out.println("Result: " + result);
    }
}
