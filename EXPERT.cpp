#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main() 
{
    int T;
    cin>>T;
    while(T--)
    {
        int a,b;
            cin>>a>>b;
        if((float)a/2<=b)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
   }
    return 0;
}

