#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int b[3],cnt=0;
	    for(int i=0;i<3;i++){
	        cin>>b[i];
	        if(b[i]==0){
	            cnt++;
	        }
	    }
	    if(cnt>=2){
	        cout<<"Water filling time"<<endl;
	    }
	    else if(cnt<2){
	        cout<<"Not now"<<endl;
	    }
	}
	return 0;
}
