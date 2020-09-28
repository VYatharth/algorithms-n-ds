from queue import Queue 

class UserMainCode(object):

    @classmethod
    def getNoOfConnectedPatches(cls,input1,input2,input3):
        rempep = []
        flag = False
        index = 0
        totalPep = 0

        if(input3>0 and input4>0):
            j=0
            for i in range(input1):
                div= input2[i]/input4
                left=0
                if(div<input3):
                    input3-=div
                    left = input2[i]%input4
                else:
                    input2[i]-=(input3*input4)
                    input3=0
                    i-=1

                if(left>0):
                    rempep.append(left)
                if(input3==0):
                    flag = True
                    index = i
                    break
        else:
            flag=true
            index-=1
        
        if flag:
            for i in range(index+1,input1):
                totalPep+=input2[i]

            for i in range(len(rempep)):
                totalPep+=rempep[i]
        else:	
            rempep.sort()
            for i in range(len(rempep)-input3):
                totalPep+=rempep[i]

        return totalPep


if __name__ == '__main__':
    a = UserMainCode()
    print(a.getNoOfConnectedPatches(2,2,[[1,1],[0,1]]))