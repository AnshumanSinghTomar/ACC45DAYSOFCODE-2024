#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int i;
	cin>>i;
	while(i--)
	{
	    int x,y,z;
	    cin>>x>>y;
	    z=y/x;
	    if(z*x<y)
	    {
	        cout<<z<<endl;
	    }
	    else
	    cout<<z-1<<endl;
	}
	return 0;
}