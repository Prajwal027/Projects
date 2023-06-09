import java.util.Scanner;

public class lab1 {

    public static void main(String[] args) {

        // Creates a reader instance which takes
        // input from standard input - keyboard
        Scanner rea = new Scanner(System.in);
       
        System.out.print("Enter a number: ");

        // nextInt() reads the next integer from the keyboard
        int number = rea.nextInt();

        // println() prints the following line to the output screen
        System.out.println("You entered: " + number);
        rea.close();
    }
}