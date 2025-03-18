import java.util.Scanner;

public class Program14 {
    public static int linearSearch(int[] arr, int key) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int n = scanner.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter array elements:");
        for (int i = 0; i < n; i++) arr[i] = scanner.nextInt();

        System.out.print("Enter element to search: ");
        int key = scanner.nextInt();

        int result = linearSearch(arr, key);
        if (result != -1) System.out.println("Element found at index: " + result);
        else System.out.println("Element not found");
        
        scanner.close();
    }
}
