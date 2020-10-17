class UserMainCode(object):
    @classmethod
    def noOfSubsets(cls,input1,input2,input3):
        UserMainCode.count_cache = [[0 for i in range(input3)] for i in range(input1)] 
        UserMainCode.is_calculated = [[0 for i in range(input3)] for i in range(input1)] 
        count= UserMainCode.calculateCount(input2, 0, 0, input1, input3)
        allzero = True
        for i in range(input1):
            if input2[i] != 0:
                allzero = False
        if(allzero):
            return 1

        return count

    count_cache = []
    is_calculated = []
    
    @staticmethod
    def calculateCount(input2, i, current_remainder, input1, input3): 
        if (i == input1): 
            if (current_remainder == 0): 
                return 1
            else: 
                return 0
    
        # If the state has been solved before 
        # return the value of the state 
        if (UserMainCode.is_calculated[i][current_remainder]): 
            return UserMainCode.count_cache[i][current_remainder] 
    
        # Setting the state as solved 
        UserMainCode.is_calculated[i][current_remainder] = 1
    
        # Recurrence relation 
        UserMainCode.count_cache[i][current_remainder] = UserMainCode.calculateCount(input2, i + 1,  current_remainder, input1, input3) + UserMainCode.calculateCount(input2, i + 1, (current_remainder + input2[i]) % input3, input1, input3) 
        return UserMainCode.count_cache[i][current_remainder]  

if __name__ == '__main__':
    a = UserMainCode()
    print(a.noOfSubsets(3,[5,5,5],5))

