#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t; cin>>t; while(t--){
	int x,y; 
	cin>>x>>y;
	int z= 500-2*x;
	int a=1000-4*(x+y);
	int b=500-2*(x+y);
		int c= 1000-4*y;
		int e=b+c;
		int f=z+a;
	if(e>f){cout<<e<<endl;}
	else{cout<<f<<endl;}
	
	

	}
	return 0;
}