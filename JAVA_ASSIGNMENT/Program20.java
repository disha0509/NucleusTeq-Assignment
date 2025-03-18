import java.util.Scanner;

public class Program20 {
    public static int countVowels(String str) {
        int count = 0;
        str = str.toLowerCase(); 
        for (char ch : str.toCharArray()) {
            if ("aeiou".indexOf(ch) != -1) { 
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();

        int vowelCount = countVowels(input);
        System.out.println("Number of vowels: " + vowelCount);
        
        scanner.close();
    }
}
