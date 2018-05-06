class Node:
    def __init__(self, label, value = 0, left = None, right = None):
        self.label = label
        self.value = value
        self.left = left
        self.right = right
        
class Tree:
    def __init__(self, root):
        self.root = root


def setValue(node, k = 0):
    node.value = k
    k += 1
    if node.left!=None:
        setValue(node.left, k)
    
    if node.right!=None:
        setValue(node.right, k)
        
    
    
def setLeft(nodes, ctr):
    
    c = ctr
    while nodes[c]!= None:
        nodes[c].left = nodes[c+1]
        c += 1
        
    return c+1
    
def setLeftandRight(nodes, ctr):
    n = len(nodes)
    
    k = setLeft(nodes, ctr)
    c = k
    while c-1>=0 and c-1<n and k<n:
        
        if nodes[c-1]!=None:
            if nodes[c-1].right != None:
                c -= 1
                continue
            nodes[c-1].right = nodes[k]
            c = k+1
            k = setLeft(nodes, k)
            
            
        
        c -= 1
    


        
    
        
        
def treeBottom(tree):
    res = []
    tree = tree.replace("()", "-1")
    tree = tree.replace("(", " ")
    tree = tree.replace(")", " ")
    tree = map(int, tree.split())
    
    
    nodes = []
    ctr = 0
    n = len(tree)
    
    while ctr < n:
        if tree[ctr] != -1:
            nodes.append(Node(tree[ctr]))
        else:
            nodes.append(None)
            
        ctr += 1
        
    setLeftandRight(nodes, 0)
    setValue(nodes[0])
    res = []
    maxval = 0
    for x in nodes:
        
        if x!=None:
            print x.label, x.value, 
            if x.left==None:
                print None,
            else:
                print x.left.label,
            if x.right==None:
                print None
            else:
                print x.right.label
                
            if x.value > maxval:
                res = []
                res.append(x.label)
                maxval = x.value
            else:
                res.append(x.label)
                
    
    return res
        
    
        
        
    
    
    

