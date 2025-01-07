#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes
void addTwoNumbers(int a, int b);
void swap(int *x, int *y);
void calculateAreaOfCircle(float radius);
void displayStudentInfo(struct Student student);
void writeToFile(const char *filename, const char *data);
void readFromFile(const char *filename);

struct Student {
    char name[50];
    int age;
    float marks;
};

// Main function
int main() {
    int num1, num2;
    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);

    // Demonstrating basic arithmetic operation
    addTwoNumbers(num1, num2);

    // Demonstrating pointer and swapping values
    printf("Before swapping: num1 = %d, num2 = %d\n", num1, num2);
    swap(&num1, &num2);
    printf("After swapping: num1 = %d, num2 = %d\n\n", num1, num2);

    // Demonstrating a loop and condition
    printf("Even numbers between 1 and 20:\n");
    for (int i = 1; i <= 20; i++) {
        if (i % 2 == 0) {
            printf("%d ", i);
        }
    }
    printf("\n\n");

    // Array Example
    int arr[5] = {10, 20, 30, 40, 50};
    printf("Array elements:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n\n");

    // Using structures
    struct Student student1 = {"John Doe", 20, 85.5};
    displayStudentInfo(student1);

    // File handling example (Write to file)
    writeToFile("student_data.txt", "This is a test message.\n");

    // File handling example (Read from file)
    readFromFile("student_data.txt");

    // Using functions to calculate area of a circle
    float radius;
    printf("Enter the radius of a circle: ");
    scanf("%f", &radius);
    calculateAreaOfCircle(radius);

    return 0;
}

// Function definitions

// Function to add two numbers
void addTwoNumbers(int a, int b) {
    int sum = a + b;
    printf("Sum of %d and %d is %d\n\n", a, b, sum);
}

// Function to swap two numbers using pointers
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

// Function to calculate area of a circle
void calculateAreaOfCircle(float radius) {
    float area = 3.14 * radius * radius;
    printf("Area of the circle with radius %.2f is %.2f\n\n", radius, area);
}

// Function to display student information using a structure
void displayStudentInfo(struct Student student) {
    printf("Student Information:\n");
    printf("Name: %s\n", student.name);
    printf("Age: %d\n", student.age);
    printf("Marks: %.2f\n\n", student.marks);
}

// Function to write data to a file
void writeToFile(const char *filename, const char *data) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file for writing.\n");
        return;
    }
    fprintf(file, "%s", data);
    fclose(file);
    printf("Data written to file successfully.\n\n");
}

// Function to read data from a file
void readFromFile(const char *filename) {
    FILE *file = fopen(filename, "r");
    char buffer[255];
    if (file == NULL) {
        printf("Error opening file for reading.\n");
        return;
    }
    printf("Data read from file:\n");
    while (fgets(buffer, 255, file) != NULL) {
        printf("%s", buffer);
    }
    fclose(file);
    printf("\n");
}

