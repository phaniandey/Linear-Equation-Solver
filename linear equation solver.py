while True:
    print("Welcome to solving 2 linear equations with 2 variables")
    def linearsol(sol1,sol2):
        a1,b1,c1,a2,b2,c2=sol1[0],sol1[1],sol1[2],sol2[0],sol2[1],sol2[2]
        if(a1==a2 or b1==b2):
            a3=a1-a2
            b3=b1-b2
            c3=c1-c2
            if(a3==0):
                if(c3!=0):
                    y=(-c3)/b3
                    z=-((y*b1)+c1)
                    x=z/a1
                    return x,y
                else:
                    x=(-c1)/a1
                    return x,0
            
            else:
                if(c3!=0):
                    x=(-c3)/a3
                    z=-((x*a1)+c1)
                    y=z/b1
                    return x,y
                else:
                    y=(-c1)/b1
                    return 0,y
        elif(a1!=0 and a2!=0):
            a3=(a1*a2)-(a2*a1)
            b3=(b1*a2)-(b2*a1)
            c3=(c1*a2)-(c2*a1)
            y=(-c3)/b3
            x=((-c1)+(-(b1*y)))/a1
            return x,y
        elif(a1==0 or a2==0):
            if(a1==0):
                y=(-c1)/b1
                x=-(c2+(b2*y))/a2
                return x,y
            else:
                y=(-c2)/b2
                x=-(c1+(b1*y))/a1
                return x,y
    sol1=[]
    sol2=[]
    n=["a1","b1","c1"]
    m=["a2","b2","c2"]
    for i in (n):
        n=int(input("enter {} value ".format(i)))
        sol1.append(n)
    for j in (m):
        n=int(input("enter {} value ".format(j)))
        sol2.append(n)
    if(sol1[0]==0 and sol1[1]==0 and sol1[2]==0):
        print("it is single linear equation")
    elif(sol1[0]==0 and sol1[1]==0):
         print("it has no solutions")
    elif(sol1[0]==0 and sol2[0]==0):
        print("it has no solution")
    elif(sol1[1]==0 and sol2[1]==0):
        print("it has no solution")
    elif(sol2[0]!=0 and sol2[1]!=0 and sol2[2]!=0):
        if((sol1[0]/sol2[0])==(sol1[1]/sol2[1])==(sol1[2]/sol2[2])):
            print("it has infinite solutions")
        elif((sol1[0]/sol2[0])==(sol1[1]/sol2[1])):
            print("it has no solutions")
        else:
            result=linearsol(sol1,sol2)
            print("x value {} and y value {}".format(result[0],result[1]))
    else:
        if(sol2[0]==0 and sol2[1]==0 and sol2[2]==0):
            print("it is single linear equation")
        elif(sol2[0]==0 and sol2[1]==0):
            print("it has no solutions")
        elif(sol2[0]==0 or sol2[1]==0 or sol2[2]==0):
            result=linearsol(sol1,sol2)
            print("x value {} and y value {}".format(result[0],result[1]))
        
        
            
            
    
