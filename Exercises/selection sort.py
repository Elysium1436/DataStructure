from time import time

from random import randrange


def selectionsort(l):
	min = l[0]
	changed=False
	index =0
	for i in range(len(l)-1):
		min=l[i]
		for j in range(i,len(l)):
			if min>l[j]:
				index=j
				min=l[j]
				changed=True
				
		
		if changed:
			l[i], l[index] = l[index], l[i]
			#print(l)

		




def main():


	l1 = [randrange(1, 10000000) for i in range(10000)]
	# l2 = [randrange(1, 10000000) for i in range(100000)]
	# l3 = [randrange(1, 10000000) for i in range(10000000)]

	t1 = time()
	selectionsort(l1)
	t2 = time()
	ti = [t2-t1]

	# t1 = time()
	# selectionsort(l2)
	# t2 = time()
	# ti.append(t2-t1)

	# t1 = time()
	# selectionsort(l3)
	# t2 = time()
	# ti.append(t2-t1)

	print(ti, l1)

main()

