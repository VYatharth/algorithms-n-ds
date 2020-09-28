class Node: 
      
    # Constructor to create a new node 
    def __init__(self, id,x,y): 
        self.id = id 
        self.x = x 
        self.y = y 
        self.z = None 
        self.left = None
        self.right = None


class UserMainCode(object):
    preIndex = 0
    result = []
    @classmethod  
    def buildTree(cls,inOrder, preOrder, inStrt, inEnd, input4): 
      
        if (inStrt > inEnd): 
            return None
  
        tempId = preOrder[UserMainCode.preIndex]
        # Pich current node from Preorder traversal using 
        # preIndex and increment preIndex 
        tNode = Node(tempId, input4[tempId - 1][0], input4[tempId - 1][1]) 
        UserMainCode.preIndex += 1
  
        # If this node has no children then return 
        if inStrt == inEnd : 
            return tNode 
  
        # Else find the index of this node in Inorder traversal 
        inIndex = UserMainCode.search(inOrder, inStrt, inEnd, tNode.id) 
      
        # Using index in Inorder Traversal, construct left  
        # and right subtrees 
        tNode.left = UserMainCode.buildTree(inOrder, preOrder, inStrt, inIndex-1,input4) 
        tNode.right = UserMainCode.buildTree(inOrder, preOrder, inIndex + 1, inEnd,input4) 
  
        return tNode 
  
    @staticmethod
    def search(arr, start, end, value): 
        for i in range(start, end + 1): 
            if arr[i] == value: 
                return i 

    @staticmethod
    def calculateZ(node): 
        if node is None: 
            return 0
      
        node.z = node.x - node.y

        node.z += UserMainCode.calculateZ(node.left) 

        UserMainCode.result.append(node.z)

        return node.z + UserMainCode.calculateZ(node.right) 
      

if __name__ == '__main__':
    a = UserMainCode()
    a.preIndex = 0
    inOrder = [1,3,5,6,4,2] 
    preOrder = [2,3,1,6,5,4] 
    input4 = [[ 4,5 ], [ 9, 2 ], [ -1, 6], [ 15,-10 ], [4,6],[8,8]]

    root = a.buildTree(inOrder, preOrder, 0, len(inOrder)-1, input4) 
    a.calculateZ(root)   
    print(a.result)
