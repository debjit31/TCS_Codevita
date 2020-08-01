#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t1, t2, m, t=0;
    int mathew, john;
    cin >> t1 >> t2 >> m;
    int res[100];
    if(t1>0 && t2>0 && m>0)
    {
        for(int i=1;i<=t2/2; i++)
        {
            mathew = i*((2*i)-1);
            for(int j=1; j<=t2/2; j++)
            {
                john = j*(j+1)/2;
                if ((mathew == john) && (mathew>=t1 && mathew<=t2))
                    res[t++] = mathew;
            }
        }
        if(t<m)
            cout << "No number is present at this index." << "\n";
        else
            cout << res[m-1] << "\n";
            
    }
    else
    {
        cout << "Invalid Input" << "\n";
    }
    
    
    return 0;
}