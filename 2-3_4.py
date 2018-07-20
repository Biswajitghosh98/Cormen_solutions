A=[12,314,5135,653,2,4,7623,745,51,325,437,14,7,5434,13,1,78,985,64,52,4,124,436,5,435,35654,12,3,745,3,23]
print(A)
def sort(B,i,j):
    temp=B[j]
    k=j-1
    while (k>=i and k<=j-1):
        if (B[k]>temp):
            
            B[k+1]=B[k]
            print(k)
            k=k-1
        else:
            break
    B[k+1]=temp
def Ins(C,i,j):
    if i+1 < j:
        j=j-1
        Ins(C,i,j)
    sort(C,i,j)

Ins(A,0,len(A))
print(A)
