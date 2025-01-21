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
    printf("\n");

    return 0;
}

