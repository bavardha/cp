arr = list(map(int,input().split()))
n=len(arr)

pref=[arr[0]]

for i in range(1,n):
    pref.append(max(pref[-1],arr[i]))

ans=0
for i in range(n):
    if(i==pref[i]):
        ans+=1
print(ans)

#accepted
#https://leetcode.com/problems/max-chunks-to-make-sorted