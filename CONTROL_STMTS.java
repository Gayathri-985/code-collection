import java.util.Scanner;

public class LoopAndConditionalDemo {

    // Function to demonstrate basic for loop
    public static void basicForLoop(int n) {
        System.out.println("\nBasic For Loop Example:");
        System.out.println("Printing numbers from 1 to " + n + ":");
        for (int i = 1; i <= n; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    // Function to demonstrate for-each loop (enhanced for loop)
    public static void forEachLoopExample() {
        System.out.println("\nFor-Each Loop Example:");
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println("Array elements:");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    // Function to demonstrate while loop
    public static void whileLoopExample(int n) {
        System.out.println("\nWhile Loop Example:");
        int i = 1;
        while (i <= n) {
            System.out.print(i + " ");
            i++;
        }
        System.out.println();
    }

    // Function to demonstrate do-while loop
    public static void doWhileLoopExample(int n) {
        System.out.println("\nDo-While Loop Example:");
        int i = 1;
        do {
            System.out.print(i + " ");
            i++;
        } while (i <= n);
        System.out.println();
    }

    // Function to demonstrate if-else statement
    public static void ifElseExample(int num) {
        System.out.println("\nIf-Else Statement Example:");
        if (num > 0) {
            System.out.println("The number " + num + " is positive.");
        } else if (num < 0) {
            System.out.println("The number " + num + " is negative.");
        } else {
            System.out.println("The number is zero.");
        }
    }

    // Function to demonstrate nested if statement
    public static void nestedIfExample(int num) {
        System.out.println("\nNested If Statement Example:");
        if (num > 0) {
            if (num % 2 == 0) {
                System.out.println("The number " + num + " is positive and even.");
            } else {
                System.out.println("The number " + num + " is positive and odd.");
            }
        } else if (num < 0) {
            if (num % 2 == 0) {
                System.out.println("The number " + num + " is negative and even.");
            } else {
                System.out.println("The number " + num + " is negative and odd.");
            }
        } else {
            System.out.println("The number is zero.");
        }
    }

    // Function to demonstrate switch case statement
    public static void switchCaseExample(int day) {
        System.out.println("\nSwitch-Case Example:");
        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Invalid day.");
        }
    }

    // Function to demonstrate break statement in loop
    public static void breakStatementExample(int n) {
        System.out.println("\nBreak Statement Example:");
        for (int i = 1; i <= n; i++) {
            if (i == 5) {
                break; // exit the loop when i is 5
            }
            System.out.print(i + " ");
        }
        System.out.println("\nLoop ended because of break statement.");
    }

    // Function to demonstrate continue statement in loop
    public static void continueStatementExample(int n) {
        System.out.println("\nContinue Statement Example:");
        for (int i = 1; i <= n; i++) {
            if (i == 3) {
                continue; // skip the number 3
            }
            System.out.print(i + " ");
        }
        System.out.println("\nLoop ended with continue statement.");
    }

    // Main method
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Welcome message
        System.out.println("Welcome to the Loops and Conditional Statements Program!");

        // Basic For Loop
        System.out.print("Enter a number to print from 1 to that number (For Loop): ");
        int num1 = scanner.nextInt();
        basicForLoop(num1);

        // For-Each Loop
        forEachLoopExample();

        // While Loop
        System.out.print("Enter a number to print from 1 to that number (While Loop): ");
        int num2 = scanner.nextInt();
        whileLoopExample(num2);

        // Do-While Loop
        System.out.print("Enter a number to print from 1 to that number (Do-While Loop): ");
        int num3 = scanner.nextInt();
        doWhileLoopExample(num3);

        // If-Else Statement
        System.out.print("Enter an integer to check if it is positive, negative or zero: ");
        int num4 = scanner.nextInt();
        ifElseExample(num4);

        // Nested If Statement
        System.out.print("Enter a number to check if it is positive/negative and even/odd: ");
        int num5 = scanner.nextInt();
        nestedIfExample(num5);

        // Switch-Case Example
        System.out.print("Enter a number between 1 and 7 to know the day of the week: ");
        int day = scanner.nextInt();
        switchCaseExample(day);

        // Break Statement in Loop
        System.out.print("Enter a number to print numbers until 5 (Break Statement): ");
        int num6 = scanner.nextInt();
        breakStatementExample(num6);

        // Continue Statement in Loop
        System.out.print("Enter a number to print all numbers except 3 (Continue Statement): ");
        int num7 = scanner.nextInt();
        continueStatementExample(num7);

        // Closing the scanner
        scanner.close();
        System.out.println("\nThank you for using the Loops and Conditional Statements Program!");
    }
}
