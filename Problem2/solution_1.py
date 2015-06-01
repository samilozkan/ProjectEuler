 # Each new term in the Fibonacci sequence is generated by adding the previous two terms.
 # By starting with 1 and 2, the first 10 terms will be:

 # 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

 # By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibGenerator(n):
	a, b = 1, 1
	while b <= n:
		a, b = b, a + b
		yield a
sumFib = 0
for i in fibGenerator(4000000):
	if i % 2 == 0:
		sumFib += i

print('Sum: %d' %sumFib)

