#If_Else Statements
If_Else_Statement.py

#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))


Python Conditions

Equals						-> x == y
Not Equals					-> x != y
Less than 					-> x < y
Less than or equal to		-> x <= y
Greater than				-> x > y
Greater than or equal to 	-> x >= y
Boolean OR                  -> x or y , x | y    
Boolean AND					-> x and y, x & y
Boolean NOT					-> not X


if -
else -

#If Statement

x = 70
y = 60

if x > y:
	print("x is greater than y ")

#Elif 

x = 70
y = 70

if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")

#Else

x = 50
y = 150
if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("x is less than y")

#Short Hand If

if x > y: print("x is greater than y")

#Short Hand If.....Else

x = 50
y = 150
print(x) if x > y else print(y)


#And is a logical operator

x = 50
y = 40
z = 100
if x > y and z > x:
	print("All Conditions are True")

#Or is a logical operator

x = 50
y = 40
z = 100

if x > y or z < y:
	print("One of the conditions is True")
elif x > y and z > y:
	print("All Conditions are True")
else:
	print("Nothing Else")


int(input("Examination Result : "))
100 - 90 - A
89 - 70 - B
69 - 60 - C
59 - 40 - D
39 - 0  - Fail

x = int(input("Examination Result : "))

if x < 101 and x >= 90 or x == 100:
	print("Grade A")
elif x <= 89 and x >= 70:
	print("Grade B")
elif x <= 69 and x >= 60:
	print("Grade C")
elif x <= 59 and x >= 40:
	print("Grade D")
elif x <= 39 and x > 0 or x == 0:
    print("Fail")
else:
    print("Wrong Number. Try Again!")

#Nested If is if statements in if statements

x = 50

if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
	else:
		print("No, x is not greater than 20")

elif x > 10 and x != 10 or x > 20:
	print("x is greater than 10 and 20")
else:
	print("x is not greater than 10 & 20")


if siyb student
	if python or unity or ai
		if boy or girl
		else
	else	
else: