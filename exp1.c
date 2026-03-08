#include <stdio.h>
#include <stdlib.h>

// ------------------------ AVL Tree Node Definition ------------------------

typedef struct Node {
    int key;
    struct Node *left;
    struct Node *right;
    int height;
} Node;

// ------------------------ Utility Functions ------------------------

int height(Node *N) {
    return (N == NULL) ? 0 : N->height;
}

int max(int a, int b) {
    return (a > b) ? a : b;
}

Node* newNode(int key) {
    Node* node = (Node*) malloc(sizeof(Node));
    node->key = key;
    node->left = node->right = NULL;
    node->height = 1;
    return node;
}

// ------------------------ Rotations ------------------------

Node* rightRotate(Node *y) {
    Node *x = y->left;
    Node *T2 = x->right;
    x->right = y;
    y->left = T2;
    y->height = max(height(y->left), height(y->right)) + 1;
    x->height = max(height(x->left), height(x->right)) + 1;
    return x;
}

Node* leftRotate(Node *x) {
    Node *y = x->right;
    Node *T2 = y->left;
    y->left = x;
    x->right = T2;
    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;
    return y;
}

// ------------------------ Balancing ------------------------

int getBalance(Node *N) {
    return (N == NULL) ? 0 : height(N->left) - height(N->right);
}

// ------------------------ Insert Function ------------------------

Node* insert(Node* node, int key) {
    if (node == NULL) return newNode(key);

    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);
    else
        return node;

    node->height = 1 + max(height(node->left), height(node->right));

    int balance = getBalance(node);

    if (balance > 1 && key < node->left->key)
        return rightRotate(node);

    if (balance < -1 && key > node->right->key)
        return leftRotate(node);

    if (balance > 1 && key > node->left->key) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    if (balance < -1 && key < node->right->key) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

// ------------------------ Delete Function ------------------------

Node *minValueNode(Node* node) {
    Node* current = node;
    while (current->left != NULL)
        current = current->left;
    return current;
}

Node* deleteNode(Node* root, int key) {
    if (root == NULL) return root;

    if (key < root->key)
        root->left = deleteNode(root->left, key);
    else if (key > root->key)
        root->right = deleteNode(root->right, key);
    else {
        if ((root->left == NULL) || (root->right == NULL)) {
            Node *temp = root->left ? root->left : root->right;
            if (temp == NULL) {
                temp = root;
                root = NULL;
            } else *root = *temp;
            free(temp);
        } else {
            Node* temp = minValueNode(root->right);
            root->key = temp->key;
            root->right = deleteNode(root->right, temp->key);
        }
    }

    if (root == NULL) return root;

    root->height = 1 + max(height(root->left), height(root->right));

    int balance = getBalance(root);

    if (balance > 1 && getBalance(root->left) >= 0)
        return rightRotate(root);

    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }

    if (balance < -1 && getBalance(root->right) <= 0)
        return leftRotate(root);

    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}

// ------------------------ In-order Traversal to File ------------------------

void inorderToFile(Node* root, FILE *fp) {
    if (root != NULL) {
        inorderToFile(root->left, fp);
        fprintf(fp, "%d ", root->key);
        inorderToFile(root->right, fp);
    }
}

// ------------------------ Main Function (Console Application Entry Point) ------------------------

int main() {
    Node* root = NULL;
    FILE *infile = fopen("C:\ads aa c\Input.txt", "r");
    FILE *outfile;
    int num;

    if (infile == NULL) {
        printf("Input file not found.\n");
        return 1;
    }

    while (fscanf(infile, "%d", &num) != EOF) {
        root = insert(root, num);
    }
    fclose(infile);

    // Sample insert and delete operations
    root = insert(root, 15);
    root = deleteNode(root, 10);

    outfile = fopen("output.txt", "w");
    inorderToFile(root, outfile);
    fclose(outfile);
    printf("AVL tree constructed and written to output.txt\n");
    return 0;
}


