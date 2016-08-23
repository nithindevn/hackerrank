import itertools
n=int(input())
for i in range(n):
	string=input()
	l=[]*len(string)
	for i in range(len(string)):
		l.append(string[i])
	l=tuple(l)
	L=[]
	previous=()
	for current in itertools.permutations(l, len(l)):
		if current==previous and previous==l:
			print("no answer")
		elif previous==l:
			print(''.join(current))
			break
		previous=current
