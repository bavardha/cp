arr = list(map(int,input().split()))
n=len(arr)

if n<3:
    print(0)

pref=[arr[0]]

for i in range(1,n):
    pref.append(max(pref[-1],arr[i]))

suff=[arr[-1]]

for i in range(n-2,-1,-1):
    suff.append(max(suff[-1],arr[i]))
    
print(pref,suff)
suff=suff[::-1]
ans=0
for i in range(1,n-1):
    temp= min(pref[i-1],suff[i+1])-arr[i]
    if(temp>0):
        ans+=temp
print(ans)


#accepted
#https://leetcode.com/problems/trapping-rain-water



        

