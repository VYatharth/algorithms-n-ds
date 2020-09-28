def checkBST(root):
    if root == None:
        return True
    return wrapper(root, float("inf"), -float("inf"))

def wrapper(root, maxSoFar, minSoFar):
    if root == None:
        return True
    if root.data >= maxSoFar or root.data <= minSoFar:
        return False
    rightIsTree= wrapper(root.right, maxSoFar, root.data)
    leftIsTree= wrapper(root.left, root.data, minSoFar)
    if root.left != None and not leftIsTree:
        return False
    elif root.right != None and not rightIsTree:
        return False
    return True