import java.util.Scanner;

public class Program1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Choose shape: 1. Circle  2. Rectangle  3. Triangle");
        int choice = scanner.nextInt();

        switch (choice) {
            case 1:
                System.out.print("Enter radius: ");
                double radius = scanner.nextDouble();
                System.out.println("Area of Circle: " + (Math.PI * radius * radius));
                break;
            case 2:
                System.out.print("Enter length and breadth: ");
                double length = scanner.nextDouble();
                double breadth = scanner.nextDouble();
                System.out.println("Area of Rectangle: " + (length * breadth));
                break;
            case 3:
                System.out.print("Enter base and height: ");
                double base = scanner.nextDouble();
                double height = scanner.nextDouble();
                System.out.println("Area of Triangle: " + (0.5 * base * height));
                break;
            default:
                System.out.println("Invalid choice!");
        }
        scanner.close();
    }
}
