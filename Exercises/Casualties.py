class Casualities(object):
    @classmethod
    def calculateCasualties(cls, input1,input2,input3,input4):
        if input1 == None or input2 == None or input3 == None or input4 == None:
            return None

        no_subg = input1 // input2
        no_remaining_cars = input1 % input2
        current_index = 0

        fatalities_count = 0

        for i in range(no_subg):
            initial_subg = input3[current_index:current_index + input2]
            final_subg = input4[current_index:current_index + input2]
            if Casualities.isCyclicRotation(initial_subg,final_subg) == False:
                fatalities_count += input2

            current_index += input2

        if no_remaining_cars > 0:
            initial_subg = input3[current_index:current_index + no_remaining_cars]
            final_subg = input4[current_index:current_index + no_remaining_cars]
            if Casualities.isCyclicRotation(initial_subg,final_subg) == False:
                fatalities_count += input2

        return fatalities_count
    
    @classmethod
    def isCyclicRotation(cls, initial_subg,final_subg):
        final_subg_index = final_subg.index(initial_subg[0])
        subg_count = len(initial_subg)
        for i in range(subg_count):
            if initial_subg[i] != final_subg[final_subg_index]:
                return False

            final_subg_index+=1
            if final_subg_index == subg_count:
                final_subg_index = 0

        return True

     
if __name__ == '__main__':
    a = Casualities()
print(a.calculateCasualties(6,3,[1,2,3,4,5,6],[1,3,2,5,6,4]))