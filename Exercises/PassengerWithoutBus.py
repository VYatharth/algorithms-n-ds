
class UserMainCode(object):

    @classmethod
    def getPassengersWithoutBus(cls,input1,input2,input3,input4):
        remaining_passengers = []
        busses_filled = False
        index = 0
        passengers_without_bus = 0

        if(input3>0 and input4>0):
            j=0
            for i in range(input1):
                div= int(input2[i]/input4)
                left=0
                if(div<input3):
                    input3-=div
                    left = input2[i]%input4
                else:
                    input2[i]-=(input3*input4)
                    input3=0
                    i-=1

                if(left>0):
                    remaining_passengers.append(left)
                if(input3==0):
                    busses_filled = True
                    index = i
                    break
        else:
            busses_filled=True
            index-=1
        
        if busses_filled:
            for i in range(index+1,input1):
                passengers_without_bus+=input2[i]

            for i in range(len(remaining_passengers)):
                passengers_without_bus+=remaining_passengers[i]
        else:	
            remaining_passengers.sort()
            for i in range(len(remaining_passengers)-input3):
                passengers_without_bus+=remaining_passengers[i]

        return passengers_without_bus


if __name__ == '__main__':
    a = UserMainCode()
    print(a.getPassengersWithoutBus(2,[24,21], 2,0))