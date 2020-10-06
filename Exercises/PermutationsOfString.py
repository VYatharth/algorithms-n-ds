#number theory medium
class UserMainCode(object):
    fact_dict = dict()

    @staticmethod
    def factorial(n): 
        if n == 0: 
            return 1
        prev_fact = 1
        if((n-1) in UserMainCode.fact_dict):
            prev_fact = UserMainCode.fact_dict[n-1]
        else:
            prev_fact = UserMainCode.factorial(n-1)
            UserMainCode.fact_dict[n-1] = prev_fact

        return n *  prev_fact

    
    @classmethod
    def perm(cls,i1,input2,input3,input4):
        x,y = -1,-1
        count = 1
        for c in input4:
            if c == input2:
                x+=1
            else:
                y+=1
        n = x+y
        for i in range(1,n+1):  
            pn = UserMainCode.factorial(n)/UserMainCode.factorial(n-i)
            dx = i if i< x else x
            dy = i if i< y else y
            px = UserMainCode.factorial(x)/UserMainCode.factorial(x-dx)
            py = UserMainCode.factorial(y)/UserMainCode.factorial(y-dy)

            count += pn/(px * py)

        return int(count)




if __name__ == '__main__':
    a = UserMainCode()
    print(a.perm(3,'x','y',"xyyxy"))



