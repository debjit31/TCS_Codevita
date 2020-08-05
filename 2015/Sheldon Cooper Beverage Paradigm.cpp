#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n,x;
	cin >> n;
	vector<int> ar(n, 0);
	for(int i=0; i<n;i++)
	{
		cin >> ar[i];	
	}
	cin >> x;
	bool found = false;
	for(int i=0; i<n ;i++)
	{
		for(int j=i+1; j<n; j++)
		{
			for(int k=j+1; k<n;k++)
			{
				if(ar[i]+ar[j]+ar[k] == x){
					found = true;
					break;
				}
			}
		}
	}
	if(found == true)
		cout << "True" << "\n";
	else
		cout << "False" << "\n";
		

	return 0;
}