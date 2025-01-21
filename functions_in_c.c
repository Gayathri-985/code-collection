#include <stdio.h>
#include <math.h>
#include <string.h>

// Function prototypes
int add(int a, int b);
float divide(float a, float b);
void greet();
void printArray(int arr[], int size);
int factorial(int n);
int isPalindrome(char str[]);
void swap(int *x, int *y);

int main() {
    // 1. Simple arithmetic function demonstration
    int x = 10, y = 20;
    printf("Addition of %d and %d is: %d\n", x, y, add(x, y));

    float a = 15.0, b = 3.0;
    printf("Division of %.2f by %.2f is: %.2f\n", a, b, divide(a, b));

    // 2. Greet function
    greet();

    // 3. Printing an array using a function
    int numbers[] = {1, 2, 3, 4, 5};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    printf("Array elements: ");
    printArray(numbers, size);

    // 4. Recursion: Factorial
    int num = 5;
    printf("Factorial of %d is: %d\n", num, factorial(num));

    // 5. String operations: Check palindrome
    char str1[] = "madam";
    printf("Is '%s' a palindrome? %s\n", str1, isPalindrome(str1) ? "Yes" : "No");

    char str2[] = "hello";
    printf("Is '%s' a palindrome? %s\n", str2, isPalindrome(str2) ? "Yes" : "No");

    // 6. Pointers: Swapping two numbers
    int p = 5, q = 10;
    printf("Before swapping: p = %d, q = %d\n", p, q);
    swap(&p, &q);
    printf("After swapping: p = %d, q = %d\n", p, q);

    return 0;
}

// Function to add two integers
int add(int a, int b) {
    return a + b;
}

// Function to divide two floating-point numbers
float divide(float a, float b) {
    if (b != 0) {
        return a / b;
    } else {
        printf("Error: Division by zero!\n");
        return 0.0;
    }
}

// Function to print a greeting
void greet() {
    printf("Hello! Welcome to the C programming function demonstration.\n");
}

// Function to print elements of an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Recursive function to calculate factorial
int factorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

// Function to check if a string is a palindrome
int isPalindrome(char str[]) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - i - 1]) {
            return 0;
        }
    }
    return 1;
}

// Function to swap two integers using pointers
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

