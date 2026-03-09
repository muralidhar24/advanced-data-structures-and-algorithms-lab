#include <stdio.h>
#include <stdlib.h>

#define MAX 100

// Queue structure for BFS
typedef struct {
    int items[MAX];
    int front, rear;
} Queue;

void initQueue(Queue* q) {
    q->front = q->rear = -1;
}

int isEmpty(Queue* q) {
    return q->front == -1;
}

void enqueue(Queue* q, int value) {
    if (q->rear == MAX - 1)
        return;
    if (isEmpty(q))
        q->front = 0;
    q->items[++q->rear] = value;
}

int dequeue(Queue* q) {
    if (isEmpty(q))
        return -1;
    int item = q->items[q->front];
    if (q->front >= q->rear)
        q->front = q->rear = -1;
    else
        q->front++;
    return item;
}

// -----------------------------
// Using Adjacency Matrix
// -----------------------------
void BFT_Matrix(int graph[MAX][MAX], int n, int start) {
    int visited[MAX] = {0}, i;
    Queue q;
    initQueue(&q);

    visited[start] = 1;
    enqueue(&q, start);

    printf("BFT using Adjacency Matrix: ");
    while (!isEmpty(&q)) {
        int v = dequeue(&q);
        printf("%d ", v);
        for (i = 0; i < n; i++) {
            if (graph[v][i] && !visited[i]) {
                visited[i] = 1;
                enqueue(&q, i);
            }
        }
    }
    printf("\n");
}

void DFT_Matrix_Helper(int graph[MAX][MAX], int n, int v, int visited[MAX]) {
    visited[v] = 1;
    printf("%d ", v);
    int i;
    for (i = 0; i < n; i++) {
        if (graph[v][i] && !visited[i]) {
            DFT_Matrix_Helper(graph, n, i, visited);
        }
    }
}

void DFT_Matrix(int graph[MAX][MAX], int n, int start) {
    int visited[MAX] = {0};
    printf("DFT using Adjacency Matrix: ");
    DFT_Matrix_Helper(graph, n, start, visited);
    printf("\n");
}

// -----------------------------
// Using Adjacency List
// -----------------------------
typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

typedef struct Graph {
    int numVertices;
    Node* adjLists[MAX];
} Graph;

Graph* createGraph(int vertices) {
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    graph->numVertices = vertices;
    int i;
    for (i = 0; i < vertices; i++)
        graph->adjLists[i] = NULL;
    return graph;
}

void addEdge(Graph* graph, int src, int dest) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = dest;
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;

    newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = src;
    newNode->next = graph->adjLists[dest];
    graph->adjLists[dest] = newNode;
}

void BFT_List(Graph* graph, int start) {
    int visited[MAX] = {0};
    Queue q;
    initQueue(&q);

    visited[start] = 1;
    enqueue(&q, start);

    printf("BFT using Adjacency List: ");
    while (!isEmpty(&q)) {
        int v = dequeue(&q);
        printf("%d ", v);

        Node* temp = graph->adjLists[v];
        while (temp) {
            int adjVertex = temp->vertex;
            if (!visited[adjVertex]) {
                visited[adjVertex] = 1;
                enqueue(&q, adjVertex);
            }
            temp = temp->next;
        }
    }
    printf("\n");
}

void DFT_List_Helper(Graph* graph, int v, int visited[MAX]) {
    visited[v] = 1;
    printf("%d ", v);

    Node* temp = graph->adjLists[v];
    while (temp) {
        if (!visited[temp->vertex])
            DFT_List_Helper(graph, temp->vertex, visited);
        temp = temp->next;
    }
}

void DFT_List(Graph* graph, int start) {
    int visited[MAX] = {0};
    printf("DFT using Adjacency List: ");
    DFT_List_Helper(graph, start, visited);
    printf("\n");
}

// -----------------------------
// Main Program
// -----------------------------
int main() {
    int n = 5; // Number of vertices

    // Adjacency Matrix Example
    int matrix[MAX][MAX] = {0};
    matrix[0][1] = matrix[1][0] = 1;
    matrix[0][2] = matrix[2][0] = 1;
    matrix[1][3] = matrix[3][1] = 1;
    matrix[2][4] = matrix[4][2] = 1;

    BFT_Matrix(matrix, n, 0);
    DFT_Matrix(matrix, n, 0);

    // Adjacency List Example
    Graph* graph = createGraph(n);
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);

    BFT_List(graph, 0);
    DFT_List(graph, 0);

    return 0;
}
