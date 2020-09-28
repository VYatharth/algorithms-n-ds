from copy import copy, deepcopy

class UserMainCode(object):
    @classmethod
    def calculateMinSteps(cls,input1,input2,input3,input4,input5):
        minSteps,k = 0,2
        initial = [ [input3] * input2 for _ in range(input1)]
        for i in range(input1):
            for j in range(input2):
                if(input5[i][j] == input4):
                    minSteps+=1
        
        while k<=input1 and k <=input2:
            clone = deepcopy(initial)
            steps=UserMainCode.calculateSteps(input3,input4,input1,input2,clone,input5, k)
            if steps!= -1 and steps < minSteps:
                minSteps = steps

            k+=1
       
        return minSteps

    
    
    @staticmethod
    def calculateSteps(input3,input4,m,n,initial,final, k): 
        steps=0
        for i in range(m-k+1):
            for j in range(n-k+1):
                if(initial[i][j] != final[i][j]):
                    UserMainCode.applyKernel(i,j,input3,input4,initial, k)
                    steps+=1

            for x in range(n-k+1,n):
                if(initial[i][x] != final[i][x]):
                    #unmatched element left
                    #mattrix cannot be transformed with this kernel size so return -1
                    return -1

        for i in range(m-k+1, m):
            for j in range(n):
                if(initial[i][j] != final[i][j]):
                    #unmatched element left
                    #mattrix cannot be transformed with this kernel size so return -1
                    return -1

        return steps

    @staticmethod
    def applyKernel(row,col,input1,input2,initial, kernel): 
        for i in range(kernel):
            for j in range(kernel):   
                if(initial[row+i][col+j] == input1):
                    initial[row+i][col+j] = input2
                else:
                    initial[row+i][col+j] = input1


if __name__ == '__main__':
    a = UserMainCode()
    print(a.calculateMinSteps(4,3,'x','y',[['y','y','x'],['y','x','y'],['y','x','y'],['y','y','x']]))

