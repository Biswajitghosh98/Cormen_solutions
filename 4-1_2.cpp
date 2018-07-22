#include <iostream>

using namespace std;

int main()
{
    int A[17]={0,13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7};
    int sum=0;
    for(int i=0;i<=15;i++)
        {   
            int temp=0;
            for(int j=i;j<=16;j++)
            {
                temp+=A[j];
                cout<<"i="<<i<<"j="<<j<<endl;
                if(temp>sum) 
                { 
                    cout<<sum<<endl;
                    sum=temp;
                    
                }
            }
        }
    cout<<sum<<endl;
    return 0;
}
