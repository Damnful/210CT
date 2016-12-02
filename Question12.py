class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
    
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)

def in_order(tree):
    stack = [tree]
    # make a new stack with root

    while len(stack) > 0:
        if tree:
            # whilst there are still nodes to traverse
            while tree.left:
                stack.append(tree.left)
                tree = tree.left
        # if no more left children, go to the right children
        popped = stack.pop()
        tree = None
        if popped:
            print(popped.value)
            tree = popped.right
            stack.append(tree)
            
def tree_sort(a):
    for i in a:
        tree_insert(t, i)
    in_order(t)
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  a = [10, 5, 2, 3, 4, 11]
  tree_sort(a)
