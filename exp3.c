#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

// Min Heap Functions
void minHeapify(int arr[], int n, int i) {
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] < arr[smallest])
        smallest = left;
    if (right < n && arr[right] < arr[smallest])
        smallest = right;

    if (smallest != i) {
        int temp = arr[i];
        arr[i] = arr[smallest];
        arr[smallest] = temp;

        minHeapify(arr, n, smallest);
    }
}

void buildMinHeap(int arr[], int n) {
	int i;
    for (i = n / 2 - 1; i >= 0; i--) {
        minHeapify(arr, n, i);
    }
}

void deleteMin(int arr[], int* n) {
    if (*n <= 0)
        return;

    // Move the last element to the root
    arr[0] = arr[*n - 1];
    (*n)--;

    // Heapify the root element
    minHeapify(arr, *n, 0);
}

// Max Heap Functions
void maxHeapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;

        maxHeapify(arr, n, largest);
    }
}

void buildMaxHeap(int arr[], int n) {
	int i;
    for (i = n / 2 - 1; i >= 0; i--) {
        maxHeapify(arr, n, i);
    }
}

void deleteMax(int arr[], int* n) {
    if (*n <= 0)
        return;

    // Move the last element to the root
    arr[0] = arr[*n - 1];
    (*n)--;

    // Heapify the root element
    maxHeapify(arr, *n, 0);
}

// Function to display the heap array
void displayHeap(int arr[], int n) {
	int i;
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int minHeap[] = {5, 3, 8, 1, 2, 7, 6};
    int maxHeap[] = {5, 3, 8, 1, 2, 7, 6};
    int nMin = sizeof(minHeap) / sizeof(minHeap[0]);
    int nMax = sizeof(maxHeap) / sizeof(maxHeap[0]);

    // Build Min-Heap
    buildMinHeap(minHeap, nMin);
    printf("Min-Heap before deletion:\n");
    displayHeap(minHeap, nMin);

    // Delete root of Min-Heap (delete min)
    deleteMin(minHeap, &nMin);
    printf("Min-Heap after deleting root:\n");
    displayHeap(minHeap, nMin);

    // Build Max-Heap
    buildMaxHeap(maxHeap, nMax);
    printf("\nMax-Heap before deletion:\n");
    displayHeap(maxHeap, nMax);

    // Delete root of Max-Heap (delete max)
    deleteMax(maxHeap, &nMax);
    printf("Max-Heap after deleting root:\n");
    displayHeap(maxHeap, nMax);

    return 0;
}


