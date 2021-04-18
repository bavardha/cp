n,p,q,r=map(int,input().split())
arr = list(map(int,input().split()))
n=len(arr)

if n==1:
    print(arr[0]*(p+q+r))
else:
    pref=[arr[0]]
    if(p>0):
        for i in range(1,n):
            pref.append(max(pref[-1],arr[i]))
    else:
        for i in range(1,n):
            pref.append(min(pref[-1],arr[i]))
    suff=[arr[-1]]
    if(r>0):
        for i in range(n-2,-1,-1):
            suff.append(max(suff[-1],arr[i]))
    else:
        for i in range(n-2,-1,-1):
            suff.append(min(suff[-1],arr[i]))
    suff=suff[::-1]
    ans= float('-inf')
    for i in range(n):
        ans=max(ans, p*pref[i]+q*arr[i]+r*suff[i])
    print(ans)


#accepted
#https://codeforces.com/problemset/problem/855/B


        

