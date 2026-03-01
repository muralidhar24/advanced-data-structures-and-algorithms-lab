import random

class BTreeNode:
  def __init__(self, t, leaf=False):
    self.t = t
    self.leaf = leaf
    self.keys = []
    self.children = []

  def traverse(self):
    for i in range(len(self.keys)):
        if not self.leaf:
            self.children[i].traverse()
        print(self.keys[i], end=" ")
        if not self.leaf:
            self.children[-1].traverse()

  def search(self, k):
    i = 0
    while i < len(self.keys) and k > self.keys[i]:
        i += 1

    if i < len(self.keys) and self.keys[i] == k:
        return self

    if self.leaf:
        return None

    return self.children[i].search(k)

  def split_child(self, i, y):
    z = BTreeNode(y.t, y.leaf)
    t = y.t
    z.keys = y.keys[t:]
    y.keys = y.keys[:t - 1]
    if not y.leaf:
        z.children = y.children[t:]
        y.children = y.children[:t]
    self.children.insert(i + 1, z)
    self.keys.insert(i, y.keys.pop())

  def insert_non_full(self, k):
    i = len(self.keys) - 1
    if self.leaf:
        self.keys.append(None)
        while i >= 0 and k < self.keys[i]:
            self.keys[i + 1] = self.keys[i]
            i -= 1
        self.keys[i + 1] = k
    else:
        while i >= 0 and k < self.keys[i]:
            i -= 1
        i += 1
        if len(self.children[i].keys) == 2 * self.t - 1:
            self.split_child(i, self.children[i])
            if k > self.keys[i]:
                i += 1
        self.children[i].insert_non_full(k)

  def remove(self, k):
    i = 0
    while i < len(self.keys) and k > self.keys[i]:
        i += 1

    if i < len(self.keys) and self.keys[i] == k:
        if self.leaf:
            self.keys.pop(i)
        else:
            self.remove_from_non_leaf(i)
    else:
        if self.leaf:
            print(f"Element {k} not found in the tree.")
            return
        flag = (i == len(self.keys))
        if len(self.children[i].keys) < self.t:
            self.fill(i)
        if flag and i > len(self.keys):
            self.children[i - 1].remove(k)
        else:
            self.children[i].remove(k)

  def remove_from_non_leaf(self, i):
    k = self.keys[i]
    if len(self.children[i].keys) >= self.t:
        pred = self.get_pred(i)
        self.keys[i] = pred
        self.children[i].remove(pred)
    elif len(self.children[i + 1].keys) >= self.t:
        succ = self.get_succ(i)
        self.keys[i] = succ
        self.children[i + 1].remove(succ)
    else:
        self.merge(i)
        self.children[i].remove(k)

  def get_pred(self, i):
    curr = self.children[i]
    while not curr.leaf:
        curr = curr.children[-1]
    return curr.keys[-1]

  def get_succ(self, i):
    curr = self.children[i + 1]
    while not curr.leaf:
        curr = curr.children[0]
    return curr.keys[0]

  def fill(self, i):
    if i != 0 and len(self.children[i - 1].keys) >= self.t:
        self.borrow_from_prev(i)
    elif i != len(self.keys) and len(self.children[i + 1].keys) >= self.t:
        self.borrow_from_next(i)
    else:
        if i != len(self.keys):
            self.merge(i)
        else:
            self.merge(i - 1)

  def borrow_from_prev(self, i):
    child = self.children[i]
    sibling = self.children[i - 1]
    child.keys.insert(0, self.keys[i - 1])
    if not child.leaf:
        child.children.insert(0, sibling.children.pop())
    self.keys[i - 1] = sibling.keys.pop()

  def borrow_from_next(self, i):
    child = self.children[i]
    sibling = self.children[i + 1]
    child.keys.append(self.keys[i])
    if not child.leaf:
        child.children.append(sibling.children.pop(0))
    self.keys[i] = sibling.keys.pop(0)

  def merge(self, i):
    child = self.children[i]
    sibling = self.children[i + 1]
    child.keys.append(self.keys.pop(i))
    child.keys.extend(sibling.keys)
    if not child.leaf:
        child.children.extend(sibling.children)
    self.children.pop(i + 1)

class BTree:
  def __init__(self, t):
    self.root = BTreeNode(t, True)
    self.t = t

  def traverse(self):
    if self.root is not None:
        self.root.traverse()
    print()

  def search(self, k):
    return self.root.search(k) if self.root else None

  def insert(self, k):
    root = self.root
    if len(root.keys) == 2 * self.t - 1:
        new_root = BTreeNode(self.t, False)
        new_root.children.append(self.root)
        new_root.split_child(0, self.root)
        self.root = new_root
        self.root.insert_non_full(k)
    else:
        root.insert_non_full(k)

  def remove(self, k):
    if not self.root:
        print("The tree is empty")
        return
    self.root.remove(k)
    if len(self.root.keys) == 0:
        if not self.root.leaf:
            self.root = self.root.children[0]
        else:
            self.root = None

# Main Program
btree = BTree(5)
elements = random.sample(range(1, 200), 100)
# Insert elements
for elem in elements:
  btree.insert(elem)

print("\nB-Tree traversal after insertions:")
btree.traverse()

# Search and delete based on user input
while True:
  try:
    user_input = input("\nEnter a number to search or delete (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    number = int(user_input)
    if btree.search(number):
        print(f"Element {number} found.")
        action = input("Do you want to delete it? (yes/no): ").lower()
        if action == 'yes':
            btree.remove(number)
            print(f"Element {number} deleted.")
            print("B-Tree traversal after deletion:")
            btree.traverse()
    else:
        print(f"Element {number} not found.")
  except ValueError:
    print("Please enter a valid number or 'exit' to quit.")