from queue import Queue 

class UserMainCode(object):

    @classmethod
    def getNoOfConnectedPatches(cls,input1,input2,input3):
        count = 0
        for i in range(input1):
            for j in range(input2):
                if (input3[i][j] == 1):
                    patch_size = UserMainCode.BFS(input3,input1,input2, i, j)
                    if patch_size > 0:
                        count+=1
        return count


    @staticmethod
    def BFS(mat,input1,input2, row, col) :
        patch_size = 0; 
  
        Q = Queue() 
        Q.put(( row, col ))
  

        while (not Q.empty()): 
  
            it = Q.get_nowait(); 
  
            r, c = it
  
            if (r < 0 or c < 0 or r >= input1 or c >= input2): 
                continue 
  
            if (mat[r][c] == 0): 
                continue
  
            if (mat[r][c] == 1):
  
                mat[r][c] = 0; 
  
                patch_size+=1 
            
  
            Q.put(( r + 1, c )); 
            Q.put(( r - 1, c )); 
            Q.put(( r, c + 1 )); 
            Q.put(( r, c - 1 )); 
  
        return patch_size; 


if __name__ == '__main__':
    a = UserMainCode()
    print(a.getNoOfConnectedPatches(2,2,[[1,1],[0,1]]))