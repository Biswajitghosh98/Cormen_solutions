A=[23,14,653,34,865,452,34,54,3654,45,465,47,345,436,543,5234,543,6,546,547,61,857,545,34,23,4,325,347,645,878,6,43,534,523,534,5,324,324,23,65,77,56,58,52,454]
A.sort()
print(A)
i=0
j=len(A)-1
x=int(input())
def find(A,x,i,j):
    if(A[i]+A[j]==x):
        return print(i+1,",",j+1)
    elif(A[i]+A[j]>x):
        j=j-1
        find(A,x,i,j)
    elif(A[i]+A[j]<x):
        i=i+1
        find(A,x,i,j)
    elif(i==j):
        print("Wrong input")
        return
find(A,x,i,j)
