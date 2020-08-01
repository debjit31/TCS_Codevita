#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() 
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	long int b,n;
	cin >> b >> n;
	int input;
	vector<int> ar;
	bool invalidinput = false;
	if((b>=1 && b<=10000) && (n>=1 && n<=1000000000))
	{
		for(int i=0;i<n;i++)
		{
			cin >> input;
			if(input >= 1 && input <= 100000)
				ar.push_back(input);
			else{
				cout << "Invalid Input";
				invalidinput = true;
				break;
			}
		}
		bool dead = false;
		if(invalidinput == false)
		{
			for(int i=0; i<ar.size(); i++)
			{
				if(b >= ar[i])
				{
					b = b - (ar[i]%2 + ar[i]/2);
				}
				else{
					dead = true;
					break;
				}
			}
			if(dead == true)
				cout << "NO";
			else
				cout << "YES";
		}
		
	}
	else{
		cout << "Invalid Input";
	}
	return 0;
}