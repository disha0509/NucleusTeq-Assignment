import java.io.*;

public class Program24 {
    public static void main(String[] args) {
        try {
            //example.txt is in directory
            File file = new File("example.txt"); 
            BufferedReader reader = new BufferedReader(new FileReader(file));

            String line;
            System.out.println("File Content:");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found!");
        } catch (IOException e) {
            System.out.println("Error reading the file.");
        }
    }
}
