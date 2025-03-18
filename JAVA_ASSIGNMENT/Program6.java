import java.util.Scanner;

public class Program6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Taking user input
        System.out.print("Enter first number (a): ");
        int a = scanner.nextInt();
        System.out.print("Enter second number (b): ");
        int b = scanner.nextInt();

        // Arithmetic Operators
        System.out.println("\nSum: " + (a + b));
        System.out.println("Product: " + (a * b));

        // Relational Operators
        System.out.println("\na > b: " + (a > b));
        System.out.println("a == b: " + (a == b));

        // Logical Operators
        boolean cond1 = (a > 0), cond2 = (b > 0);
        System.out.println("\nLogical AND (both positive): " + (cond1 && cond2));
        System.out.println("Logical OR (at least one positive): " + (cond1 || cond2));

        scanner.close();
    }
}
