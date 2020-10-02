


def findOrder(symbols):
    gc = 0;
    charArray = [chr(i+97) for i in range(len(symbols) + 1)]
    finalStr=""
    for x in symbols:
        if(x == '>'):
            gc +=1
        else:
            if(gc>0):
                for y in range(gc,0,-1):
                    finalStr += charArray.pop(y)
                gc=0
            
            finalStr += charArray.pop(0)

    if(gc>0):
        for y in range(gc,0,-1):
            finalStr += charArray.pop(y)
        gc=0
            
    finalStr += charArray.pop(0)

    print(finalStr)
    



findOrder('>><')
    # Write Your Code Here
