import java.util.Scanner;

public class JavaBasics {

    // Function to demonstrate basic arithmetic operations
    public static void arithmeticOperations(int a, int b) {
        System.out.println("\nArithmetic Operations:");
        System.out.println("Addition: " + (a + b));
        System.out.println("Subtraction: " + (a - b));
        System.out.println("Multiplication: " + (a * b));
        System.out.println("Division: " + (a / b));
        System.out.println("Modulus: " + (a % b));
    }

    // Function to demonstrate conditional statements
    public static void conditionalDemo(int number) {
        System.out.println("\nConditional Statements:");
        if (number > 0) {
            System.out.println("The number is positive.");
        } else if (number < 0) {
            System.out.println("The number is negative.");
        } else {
            System.out.println("The number is zero.");
        }
    }

    // Function to demonstrate loops
    public static void loopDemo(int n) {
        System.out.println("\nLoop Demonstration:");
        System.out.println("First " + n + " numbers using for loop:");
        for (int i = 1; i <= n; i++) {
            System.out.print(i + " ");
        }
        System.out.println("\nNumbers using while loop:");
        int i = 1;
        while (i <= n) {
            System.out.print(i + " ");
            i++;
        }
        System.out.println();
    }

    // Function to demonstrate arrays
    public static void arrayDemo() {
        System.out.println("\nArray Demonstration:");
        int[] numbers = {10, 20, 30, 40, 50};
        System.out.println("Elements of the array:");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    // Main method
    public static void main(String[] args) {
        // Scanner for user input
        Scanner scanner = new Scanner(System.in);

        // Greeting
        System.out.println("Welcome to Java Basics Program!");

        // Input and basic arithmetic
        System.out.print("Enter two integers: ");
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        arithmeticOperations(num1, num2);

        // Conditional statements
        System.out.print("\nEnter an integer to check if it's positive or negative: ");
        int checkNumber = scanner.nextInt();
        conditionalDemo(checkNumber);

        // Loops
        System.out.print("\nEnter a number to print its sequence using loops: ");
        int sequenceNumber = scanner.nextInt();
        loopDemo(sequenceNumber);

        // Arrays
        arrayDemo();

        // Closing the scanner
        scanner.close();
        System.out.println("\nThank you for exploring Java Basics!");
    }
}
