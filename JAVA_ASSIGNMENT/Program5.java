import java.util.Scanner;

public class Program5 {

    public static void printSqaure(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public static void printTriangle(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = i; j < n; j++) {
                System.out.print(" ");
            }
            for (int k = 1; k <= (2 * i - 1); k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of square: ");
        int n1 = sc.nextInt();

        System.out.println("Enter the size of triangle: ");
        int n2 = sc.nextInt();

        System.out.println("Printing Square: ");
        printSqaure(n1);
        System.out.println("Printing Triangle: ");
        printTriangle(n2);
        sc.close();

    }
}