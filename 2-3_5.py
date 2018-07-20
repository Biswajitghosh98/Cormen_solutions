A=[1,2,3,6,7,9,11,15,18,28,34,55,67,133,146,267]

def bs(B,i,j):
    if(i!=j):
        if(B[(i+j)//2]==a):
            print((i+j)//2)
            return
        elif(B[(i+j)//2]<a):
            bs(B,(i+j)//2+1,j)
        elif(B[(i+j)//2]>a):
            bs(B,i,(i+j)//2)
    elif(i==j and A[i] != a):
        return print("incorrect input")
a=int(input())
bs(A,0,len(A))
