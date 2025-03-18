import java.util.Scanner;

public class Program7 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        System.out.println("------Temperature Conversion-------");
        System.out.println("1. Celsius to Fahrenheit");
        System.out.println("2. Farenheit to Celsius");
        System.out.println("Enter your choice: ");
        int ch=sc.nextInt();

        double convertedTemp;

        if(ch==1){
            System.out.println("Enter temperatur in Celsius: ");
            double celsius = sc.nextDouble();
            convertedTemp  =(celsius * 9 / 5) + 32;
            System.out.println("Temperature in Fahrenheit: "+convertedTemp+ "°F");
        }
        else{
            System.out.println("Enter temperatur in Fahrenheit: ");
            double Fahrenheit = sc.nextDouble();
            convertedTemp  =(Fahrenheit * 9 / 5) + 32;
            System.out.println("Temperature in Celsius: "+convertedTemp+ "°C");
        }
        sc.close();
    }
}