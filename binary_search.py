def recur(a, up, lo, e):
    mid = (up + lo)//2
    if(lo>up):
        print("Not found")
    elif a[mid]<e:
        lo = mid +1
        recur(a,up,lo,e)
    elif a[mid]==e:
        print("Found")
    else:
        up = mid - 1
        recur(a, up, lo, e)

li = [1,2,4,6,7,10]
lower = 0
upper =len(li)-1
e = int(input())
while lower<=upper:
    mid = (upper + lower)//2
    if li[mid]<e:
        lower=mid+1
    elif li[mid]==e:
        print("Found")
        break
    else:
        upper = mid-1
else:
    print("Not found")
recur(li, len(li)-1, 0, e)



