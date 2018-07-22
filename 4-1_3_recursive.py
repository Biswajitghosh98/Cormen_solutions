def FMS(B,low,mid,high):
    summation=0
    left_summation=-999999999
    for i in range(mid,low,-1):
        summation=summation+A[i]
        if summation>left_summation:
            left_summation=summation
            maxim_left=i
            print("maxim_left=",i)
    summation=0
    right_summation=-999999999
    for j in range(mid+1,high):
        summation=summation+A[j]
        if summation>right_summation:
            right_summation=summation
            maxim_right=j
            print("maxim_right=",j)
    return print(maxim_left,maxim_right,left_summation+right_summation)
A=[0,13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
FMS(A,0,len(A)//2,len(A)-1)

def FMAXIM(C,low,high):
    if high==low:
        return(low,high,C[low])
    else:
        mid=(low+high)//2
        (left_low,left_high,left_summation)=FMS(C,low,mid)
        (right_low,right_high,right_summation)=FMS(C,mid+1,high)
        (cross_low,cross_high,cross_summation)=FMS(C,low,high)
    if(left_summation>right_summation and left_summation>cross_summation):
        return print(left_low,",",left_high,",",left_summation)
    elif(right_summation>left_summation and right_summation>cross_summation):
        return print(right_low,",",right_high,",",right_summation)
    else:
        return print(cross_low,",",cross_high,",",cross_summation)
print("************************************************************")
FMAXIM(A,0,len(A)-1)
