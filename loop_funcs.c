#include <stdio.h>

// Function prototypes
void simpleForLoop();
void nestedForLoop();
void whileLoopExample();
void doWhileLoopExample();
void infiniteLoopExample();
void loopControlStatements();

int main() {
    printf("\n--- Demonstrating Loops in C ---\n\n");

    // 1. Simple for loop demonstration
    printf("Simple for loop example:\n");
    simpleForLoop();

    // 2. Nested for loop demonstration
    printf("\nNested for loop example:\n");
    nestedForLoop();

    // 3. While loop demonstration
    printf("\nWhile loop example:\n");
    whileLoopExample();

    // 4. Do-while loop demonstration
    printf("\nDo-while loop example:\n");
    doWhileLoopExample();

    // 5. Infinite loop example (controlled break to avoid infinite execution)
    printf("\nControlled infinite loop example:\n");
    infiniteLoopExample();

    // 6. Loop control statements (break and continue)
    printf("\nLoop control statements example:\n");
    loopControlStatements();

    return 0;
}

// Simple for loop demonstration
void simpleForLoop() {
    for (int i = 1; i <= 10; i++) {
        printf("%d ", i);
    }
    printf("\n");
}

// Nested for loop demonstration
void nestedForLoop() {
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }
}

// While loop demonstration
void whileLoopExample() {
    int i = 1;
    while (i <= 10) {
        printf("%d ", i);
        i++;
    }
    printf("\n");
}

// Do-while loop demonstration
void doWhileLoopExample() {
    int i = 1;
    do {
        printf("%d ", i);
        i++;
    } while (i <= 10);
    printf("\n");
}

// Infinite loop example (with a controlled break)
void infiniteLoopExample() {
    int count = 0;
    for (;;) { // Infinite loop
        printf("%d ", count);
        count++;
        if (count >= 10) {
            break; // Exit loop after 10 iterations
        }
    }
    printf("\n");
}

// Loop control statements (break and continue)
void loopControlStatements() {
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
}

