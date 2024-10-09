#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int i;
	cin>>i;
	while(i--){
	    int n,x;
	    cin>>n>>x;
	    if(x==0 || n==x)
	    cout<<0<<endl;
	    else if(n-x>x)
	    cout<<x<<endl;
	    else
	    cout<<n-x<<endl;
	    
	    
	}
	return 0;
}
