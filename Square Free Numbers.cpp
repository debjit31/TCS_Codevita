#include <iostream>
#include<cmath>
#include<bits/stdc++.h>
using namespace std;
vector<long long int> findPrimeFactors(long long int n)
{
	vector<long long int> f;
	while(n%2 == 0){
		f.push_back(2);
		n = n/2;
	}
	for(int i=3;i<=sqrt(n);i+=2)
	{
		while(n%i == 0)
		{
			f.push_back(i);
			n = n / i;
		}
	}
	if(n > 2)
		f.push_back(n);
	return f;
}
int main()
{
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int t;
	cin >> t;
	while(t--)
	{
		long long int n;
	cin >> n;
	vector<long long int> primeFactors = findPrimeFactors(n);
	vector<long long int>::iterator upf; 
	
	sort(primeFactors.begin(), primeFactors.end());
	
	int size = primeFactors.size();
	
	upf = unique(primeFactors.begin(), primeFactors.begin() + size);
	
	primeFactors.resize(distance(primeFactors.begin(), upf)); 
	
 //   for(long long int i : primeFactors){
	// 	cout << i << " ";
	// }
	cout << "\n";
	int N = primeFactors.size();
	// cout << N ;
	cout << pow(2.0, (double)N) -1;
	}
	
	return 0;
}