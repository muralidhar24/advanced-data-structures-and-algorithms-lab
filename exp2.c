#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MIN_DEGREE 3              // t = 3, so max keys = 2t - 1 = 5
#define MAX_KEYS (2 * MIN_DEGREE - 1)

typedef struct BTreeNode {
    int keys[MAX_KEYS];
    struct BTreeNode* children[MAX_KEYS + 1];
    int num_keys;
    int is_leaf;
} BTreeNode;

// Create a new B-Tree node
BTreeNode* createNode(int is_leaf) {
    BTreeNode* node = (BTreeNode*)malloc(sizeof(BTreeNode));
    node->is_leaf = is_leaf;
    node->num_keys = 0;
    int i;
    for (i = 0; i <= MAX_KEYS; i++)
        node->children[i] = NULL;
    return node;
}

// In-order traversal
void traverse(BTreeNode* root) {
    int i;
    for (i = 0; i < root->num_keys; i++) {
        if (!root->is_leaf)
            traverse(root->children[i]);
        printf("%d ", root->keys[i]);
    }
    if (!root->is_leaf)
        traverse(root->children[i]);
}

// Search for a key, returns pointer to node if found
BTreeNode* search(BTreeNode* root, int key) {
    int i = 0;
    while (i < root->num_keys && key > root->keys[i])
        i++;

    if (i < root->num_keys && key == root->keys[i])
        return root;

    if (root->is_leaf)
        return NULL;

    return search(root->children[i], key);
}

// Split child
void splitChild(BTreeNode* parent, int i, BTreeNode* fullChild) {
    BTreeNode* newChild = createNode(fullChild->is_leaf);
    newChild->num_keys = MIN_DEGREE - 1;
	int j;
    for (j = 0; j < MIN_DEGREE - 1; j++)
        newChild->keys[j] = fullChild->keys[j + MIN_DEGREE];

    if (!fullChild->is_leaf)
        for (j = 0; j < MIN_DEGREE; j++)
            newChild->children[j] = fullChild->children[j + MIN_DEGREE];

    fullChild->num_keys = MIN_DEGREE - 1;

    for (j = parent->num_keys; j >= i + 1; j--)
        parent->children[j + 1] = parent->children[j];

    parent->children[i + 1] = newChild;

    for (j = parent->num_keys - 1; j >= i; j--)
        parent->keys[j + 1] = parent->keys[j];

    parent->keys[i] = fullChild->keys[MIN_DEGREE - 1];
    parent->num_keys++;
}

// Insert into a non-full node
void insertNonFull(BTreeNode* node, int key) {
    int i = node->num_keys - 1;

    if (node->is_leaf) {
        while (i >= 0 && key < node->keys[i]) {
            node->keys[i + 1] = node->keys[i];
            i--;
        }

        node->keys[i + 1] = key;
        node->num_keys++;
    } else {
        while (i >= 0 && key < node->keys[i])
            i--;

        if (node->children[i + 1]->num_keys == MAX_KEYS) {
            splitChild(node, i + 1, node->children[i + 1]);

            if (key > node->keys[i + 1])
                i++;
        }

        insertNonFull(node->children[i + 1], key);
    }
}

// Insert a key
BTreeNode* insert(BTreeNode* root, int key) {
    if (root->num_keys == MAX_KEYS) {
        BTreeNode* newRoot = createNode(0);
        newRoot->children[0] = root;
        splitChild(newRoot, 0, root);
        insertNonFull(newRoot, key);
        return newRoot;
    } else {
        insertNonFull(root, key);
        return root;
    }
}

// Placeholder for deletion
BTreeNode* deleteKey(BTreeNode* root, int key) {
    printf("Delete operation not implemented for key %d.\n", key);
    return root;
}

int main() {
    srand(time(NULL));
    BTreeNode* root = createNode(1);
    int arr[100], i;

    printf("Generated Random Elements:\n");
    for (i = 0; i < 100; i++) {
        arr[i] = rand() % 1000;
        printf("%d ", arr[i]);
        root = insert(root, arr[i]);
    }

    printf("\n\nB-Tree In-Order Traversal:\n");
    traverse(root);
    printf("\n");

    // Example search
    int key_to_search = arr[25];
    printf("\nSearching for key: %d\n", key_to_search);
    BTreeNode* found = search(root, key_to_search);
    if (found != NULL)
        printf("Key %d found in B-Tree.\n", key_to_search);
    else
        printf("Key %d not found in B-Tree.\n", key_to_search);

    // Example delete (not implemented)
    root = deleteKey(root, key_to_search);

    return 0;
}


