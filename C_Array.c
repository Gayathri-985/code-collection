#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

// Function prototypes
void basicArrayExample();
void multiDimensionalArray();
void sortArray(int arr[], int size);
int binarySearch(int arr[], int size, int key);
void dynamicArrayExample();
void arrayOfStructures();

// Structure for holding student information
struct Student {
    char name[50];
    int roll_no;
    float marks;
};

// Main function
int main() {
    // Display basic array operations
    printf("Basic Array Operations:\n");
    basicArrayExample();

    // Multi-dimensional array operations
    printf("\nMulti-Dimensional Array Example:\n");
    multiDimensionalArray();

    // Sorting and searching in array
    printf("\nSorting and Searching in Array:\n");
    int arr[] = {45, 23, 12, 89, 34, 77, 56};
    int size = sizeof(arr) / sizeof(arr[0]);
    printf("Original array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    sortArray(arr, size);
    printf("Sorted array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Binary Search
    int key = 34;
    int result = binarySearch(arr, size, key);
    if (result != -1) {
        printf("Element %d found at index %d\n", key, result);
    } else {
        printf("Element %d not found\n", key);
    }

    // Dynamic array example
    printf("\nDynamic Array Example:\n");
    dynamicArrayExample();

    // Array of Structures example
    printf("\nArray of Structures Example:\n");
    arrayOfStructures();

    return 0;
}

// Basic Array Operations: Declaration, Initialization, Iteration
void basicArrayExample() {
    int arr[5] = {1, 2, 3, 4, 5};  // Static initialization

    printf("Array elements (using static initialization):\n");
    for (int i = 0; i < 5; i++) {
        printf("Element at index %d: %d\n", i, arr[i]);
    }

    // Modification of array elements
    arr[2] = 99;
    printf("\nModified array:\n");
    for (int i = 0; i < 5; i++) {
        printf("Element at index %d: %d\n", i, arr[i]);
    }
}

// Multi-Dimensional Array Example
void multiDimensionalArray() {
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // Accessing multi-dimensional array elements
    printf("Matrix elements:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

// Sorting array using Bubble Sort
void sortArray(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap elements
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Binary Search function
int binarySearch(int arr[], int size, int key) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == key) {
            return mid;
        }
        else if (arr[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;  // Element not found
}

// Dynamic Array Example
void dynamicArrayExample() {
    int *arr;
    int size;

    // Ask for the size of the array
    printf("Enter the number of elements you want to store: ");
    scanf("%d", &size);

    // Dynamically allocate memory
    arr = (int *)malloc(size * sizeof(int));
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }

    // Take input from user for dynamic array
    printf("Enter %d elements:\n", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }

    // Display dynamic array
    printf("Dynamic Array elements:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Free dynamically allocated memory
    free(arr);
}

// Array of Structures Example
void arrayOfStructures() {
    struct Student students[3] = {
        {"Abbu", 1, 85.5},
        {"Chai", 2, 90.0},
        {"Manoj", 3, 88.5}
    };

    // Display array of structures
    printf("Student Information:\n");
    for (int i = 0; i < 3; i++) {
        printf("Name: %s, Roll No: %d, Marks: %.2f\n", students[i].name, students[i].roll_no, students[i].marks);
    }
}

