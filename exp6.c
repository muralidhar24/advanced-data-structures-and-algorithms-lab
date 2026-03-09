#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SIZE 100000  // Maximum size of the array

// Function to perform QuickSort
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = (low - 1), j;
        for (j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        quickSort(arr, low, i);
        quickSort(arr, i + 2, high);
    }
}

// Function to merge two halves of the array
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int L[n1], R[n2], i;

    for (i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (i = 0; i < n2; i++)
        R[i] = arr[mid + 1 + i];

    int j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Function to perform MergeSort
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}

// Function to generate random array
void generateRandomArray(int arr[], int size) {
	int i;
    for (i = 0; i < size; i++) {
        arr[i] = rand() % 10000;  // Random numbers between 0 and 9999
    }
}

// Function to generate best-case array (sorted array)
void generateBestCaseArray(int arr[], int size) {
	int i;
    for (i = 0; i < size; i++) {
        arr[i] = i + 1;  // Sorted array: [1, 2, 3, ..., size]
    }
}

// Function to generate worst-case array (reverse sorted array)
void generateWorstCaseArray(int arr[], int size) {
	int i;
    for (i = 0; i < size; i++) {
        arr[i] = size - i;  // Reverse sorted array: [size, size-1, ..., 1]
    }
}

// Function to measure and print execution time
void measureExecutionTime(void (*sortFunc)(int[], int, int), int arr[], int size, const char* caseType) {
    clock_t start, end;
    start = clock();
    sortFunc(arr, 0, size - 1);
    end = clock();
    double timeSpent = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Execution time for %s case (size %d): %.6f seconds\n", caseType, size, timeSpent);
}

int main() {
    int sizes[] = {1000, 5000, 10000};  // Array sizes to test
    int numSizes = sizeof(sizes) / sizeof(sizes[0]);
    int i;
    
    // Loop to test various input sizes
    for (i = 0; i < numSizes; i++) {
        int size = sizes[i];

        // Test for Random Input (Average Case)
        int randomArray[MAX_SIZE];
        generateRandomArray(randomArray, size);
        printf("\nTesting QuickSort and MergeSort with Random Input (size %d):\n", size);
        measureExecutionTime(quickSort, randomArray, size, "Average Case (QuickSort)");
        measureExecutionTime(mergeSort, randomArray, size, "Average Case (MergeSort)");

        // Test for Best Case (Sorted Input)
        int bestCaseArray[MAX_SIZE];
        generateBestCaseArray(bestCaseArray, size);
        printf("\nTesting QuickSort and MergeSort with Best Case (size %d):\n", size);
        measureExecutionTime(quickSort, bestCaseArray, size, "Best Case (QuickSort)");
        measureExecutionTime(mergeSort, bestCaseArray, size, "Best Case (MergeSort)");

        // Test for Worst Case (Reverse Sorted Input)
        int worstCaseArray[MAX_SIZE];
        generateWorstCaseArray(worstCaseArray, size);
        printf("\nTesting QuickSort and MergeSort with Worst Case (size %d):\n", size);
        measureExecutionTime(quickSort, worstCaseArray, size, "Worst Case (QuickSort)");
        measureExecutionTime(mergeSort, worstCaseArray, size, "Worst Case (MergeSort)");
    }

    return 0;
}


