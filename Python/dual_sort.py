from random import randrange
from timeit import default_timer
m = []
s = 0

def quick_sort(l):
    dual_sort(l,0,len(l)-1,3)
    return l

def swap(l,lo,hi):
    l[lo],l[hi] = l[hi],l[lo]
    #temp = l[lo]
    #l[lo] = l[hi]
    #l[hi] = temp
    
def dual_sort(l,lo,hi,div):
    length = hi - lo
    if length < 27:
        # perform insertion sort
        i = lo+1
        while i<= hi:
        #for i in xrange(lo + 1, hi+ 1):
            j = i
            while j > lo and (l[j] < l[j - 1]):
                swap(l, j, j - 1)
                j -= 1
            i+=1
        return
    third = length / div
    # medians
    m1 = lo + third
    m2 = hi - third
    if m1 <= lo:
        m1 = lo + 1
    if m2 >= hi:
        m2 = hi - 1
    if l[m1] < l[m2]:
        l[m1],l[lo] = l[lo],l[m1]
        l[m2],l[hi] = l[hi],l[m2]
        #swap(l,m1,lo)
        #swap(l,m2,hi)
    else:
        l[m1],l[hi] = l[hi],l[m1]
        l[m2],l[lo] = l[lo],l[m2]
        #swap(l,m1,hi)
        #swap(l,m2,lo)
    # pivots
    piv1 = l[lo]
    piv2 = l[hi]
    # pointers
    less = lo + 1
    more = hi - 1
    # sorting
    i = less
    while i <= more:
    #for i in xrange(less,more+1):
        if l[i] < piv1:
            swap(l,i,less)
            less += 1
        elif l[i] > piv2:
            while i < more and l[more] > piv2:
                more -= 1
            swap(l,i,more)
            more -= 1
            if l[i] < piv1:
                swap(l,i,less)
                less += 1
        i+=1
    # swaps
    dist = more - less
    if dist < 13:
        div += 1
    swap(l, less - 1, lo)
    swap(l, more + 1, hi)
    # subarrays
    dual_sort(l, lo, less -2, div)
    dual_sort(l, more + 2, hi,div)
    # equal elements
    if (dist > length - 13) and piv1 != piv2:
        for i in xrange(less,more+1):
            if l[i] == piv1:
                swap(l,i,less)
                less += 1
            elif l[i] == piv2:
                swap(l,i,more)
                more -= 1
                if l[i] == piv1:
                    swap(l,i,less)
                    less += 1
    # subarray
    if piv1 < piv2:
        dual_sort(l,less,more,div)

for i in xrange(1000):
    ans = []
    for j in xrange(1000):
        ans.append(randrange(3))
    start = default_timer()
    quick_sort(ans)
    #ans.sort()
    stop = default_timer()
    m.append(stop-start)
for j in m:
    s+=j
print float(s) / len(m)
