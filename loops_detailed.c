#include <stdio.h>

int main() {
    printf("\n--- Demonstrating Loops in C ---\n\n");

    // 1. Simple for loop demonstration
    printf("Simple for loop example:\n");
    for (int i = 1; i <= 10; i++) {
        printf("%d ", i);
    }
    printf("\n\n");

    // 2. Nested for loop demonstration
    printf("Nested for loop example:\n");
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }
    printf("\n");

    // 3. While loop demonstration
    printf("While loop example:\n");
    int i = 1;
    while (i <= 10) {
        printf("%d ", i);
        i++;
    }
    printf("\n\n");

    // 4. Do-while loop demonstration
    printf("Do-while loop example:\n");
    i = 1;
    do {
        printf("%d ", i);
        i++;
    } while (i <= 10);
    printf("\n\n");

    // 5. Infinite loop example (with a controlled break)
    printf("Controlled infinite loop example:\n");
    int count = 0;
    for (;;) { // Infinite loop
        printf("%d ", count);
        count++;
        if (count >= 10) {
            break; // Exit loop after 10 iterations
        }
    }
    printf("\n\n");

    // 6. Loop control statements (break and continue)
    printf("Using 'continue' to skip even numbers:\n");
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) {
            continue; // Skip even numbers
        }
        printf("%d ", i);
    }
    printf("\n\nUsing 'break' to stop at 5:\n");
    for (int i = 1; i <= 10; i++) {
        if (i == 5) {
            break; // Exit loop at 5
        }
        printf("%d ", i);
    }
    printf("\n\n");

    // 7. Complex nested loops example (multiplication table)
    printf("Multiplication table using nested loops:\n");
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            printf("%d x %d = %d\t", i, j, i * j);
        }
        printf("\n");
    }
    printf("\n");

    // 8. Loop with array processing
    int arr[5] = {1, 2, 3, 4, 5};
    printf("Processing an array using a for loop:\n");
    for (int i = 0; i < 5; i++) {
        printf("Element %d: %d\n", i + 1, arr[i]);
    }
    printf("\n");

    // 9. Reversed loop example
    printf("Reversed loop example:\n");
    for (int i = 10; i >= 1; i--) {
        printf("%d ", i);
    }
    printf("\n\n");

    // 10. Sum of numbers using a loop
    int sum = 0;
    printf("Sum of numbers from 1 to 10:\n");
    for (int i = 1; i <= 10; i++) {
        sum += i;
    }
    printf("Sum: %d\n\n", sum);

    // 11. Loop with conditional logic
    printf("Numbers divisible by 3 from 1 to 20:\n");
    for (int i = 1; i <= 20; i++) {
        if (i % 3 == 0) {
            printf("%d ", i);
        }
    }
    printf("\n\n");

    // 12. Pattern printing using loops
    printf("Pattern printing:\n");
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
    printf("\n");

    // 13. Another pattern example
    printf("Number triangle pattern:\n");
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }
    printf("\n");

    return 0;
}

