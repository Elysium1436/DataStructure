from time import time



def findlinear(l,target):

	for i,x in enumerate(l):
		
		if x == target:
			return i

	return -1


def findbinary(l,target):

	if target == l[0]:
		return 0

	if target == l[-1]:
		return len(l)-1

	low, high = 0, len(l)-1

	while low <= high:
		mid = (low + high)//2
		item=l[mid]
		if target == mid:
			return mid

		elif target < mid:
			high = mid-1
		elif target > mid:
			low = mid+1


	return -1





l=list(range(1_000_000))

t11=time()
we=l.index(0)
t12=time()

times=[t12-t11]

t11=time()
we=l.index(999_999)
t12=time()

times.append(t12-t11)

t11=time()
we=findlinear(l,0)
t12=time()

times.append(t12-t11)

t11=time()
we=findlinear(l,999_999_999)
t12=time()

times.append(t12-t11)

t11=time()
we=findbinary(l,0)
t12=time()

times.append(t12-t11)

t11=time()
we=findbinary(l,999_999_999)
t12=time()

times.append(t12-t11)

print(times)