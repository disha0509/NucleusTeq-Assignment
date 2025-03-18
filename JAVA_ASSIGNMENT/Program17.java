import java.util.Scanner;

class Calculator {
    // Method to add two integers
    public int add(int a, int b) {
        return a + b;
    }

    // Overloaded method to add two double values
    public double add(double a, double b) {
        return a + b;
    }

    // Overloaded method to concatenate two strings
    public String add(String a, String b) {
        return a + b;
    }
}

public class Program17 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Calculator calculator = new Calculator();

        System.out.println("Enter two values (they can be numbers or strings):");

        String input1 = scanner.next();
        String input2 = scanner.next();

        
        try {
            int int1 = Integer.parseInt(input1);
            int int2 = Integer.parseInt(input2);
            System.out.println("Addition of integers: " + calculator.add(int1, int2));
        } catch (NumberFormatException e1) {
            
            try {
                double double1 = Double.parseDouble(input1);
                double double2 = Double.parseDouble(input2);
                System.out.println("Addition of doubles: " + calculator.add(double1, double2));
            } catch (NumberFormatException e2) {
               
                System.out.println("Concatenated String: " + calculator.add(input1, input2));
            }
        }

        scanner.close();
    }
}
