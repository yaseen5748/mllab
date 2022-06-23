x = 0
y = 0
m = 4
n = 3
print('initial state = (0,0)')
print('capacities = (4,3)')
print('Goal state = (2,y)')
print('Rules for reference')
print('Rule 1: Fill 4-gallon jug')
print('Rule 2: Fill 3-gallon jug')
print('Rule 3: Empty 4-gallon jug')
print('Rule 4: Empty 3-gallon jug')
print('Rule 5: Pour water from 4-gallon jug into 3-gallon jug until 3-gallon jug is full')
print('Rule 6: Pour water from 3-gallon jug into 4-gallon jug until 4-gallon jug is full')
print('Rule 7: Pour all water from 4-gallon jug into 3-gallon jug')
print('Rule 8: Pour all water from 3-gallon jug into 4-gallon jug')
while x!=2:
	r = int(input('Enter rule'))
	if (r == 1):
		x = m
	elif (r == 2):
		y = n
	elif (r == 3):
		x = 0
	elif (r == 4):
		y = 0
	elif (r == 5):
		t = n - y
		y = n
		x -= t
	elif (r == 6):
		t = m - x
		x = m
		y -= t
	elif (r == 7):
		y += x
		x = 0
	elif (r == 8):
		x += y
		y = 0
	print(x,y)

