class UserMainCode(object):
    @classmethod
    def getMinExchange(cls,input1,input2,input3):
        if(input2==input3 or input1==1):
            return 0

        largeNoPossibleExchanges = []
        smallNoPossibleExchanges = []
        minExchangingStudents = []
        smallerExchangesSet = set()

        larger,smaller = 0,0

        if(input3>input2): 
            larger=input3
            smaller=input2
        else:
            larger=input2
            smaller=input3


        while(larger>=1 and larger!=smaller): 
            largeNoPossibleExchanges.append(larger)
            larger=int(larger/2)


        if(larger==smaller):
            largeNoPossibleExchanges.append(smaller)
            return (2*len(largeNoPossibleExchanges))-3

        while(smaller>=1) :
            smallNoPossibleExchanges.append(smaller)
            smallerExchangesSet.add(smaller)
            smaller=int(smaller/2)

        matchItem = 0

        for item in largeNoPossibleExchanges:
            minExchangingStudents.append(item)

            if(item in smallerExchangesSet):
                matchItem=item
                break

        foundIndex= smallNoPossibleExchanges.index(matchItem)
        for i in range(foundIndex-1,-1,-1):
            minExchangingStudents.append(smallNoPossibleExchanges[i])

        return (2*len(minExchangingStudents))-3;


if __name__ == '__main__':
    a = UserMainCode()
    print(a.getMinExchange(3,2, 3))