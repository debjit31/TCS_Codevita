import bisect as bi
ar = list(map(int, input().split()))
k = int(input())
new_ar = list(set(ar))
new_ar.sort()
ans = []
for i in range(len(new_ar)):
	ind = bi.bisect(new_ar, new_ar[i]+k)
	if new_ar[ind-1] == new_ar[i]+k:
		ans.append((new_ar[i],new_ar[i]+k))
print(ans)
