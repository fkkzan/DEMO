# Question 1
x = 99
print("The value of x :", x)
print(type(x))

# Question 2
input("Enter the first number : ")
input("Enter the second number: ")


#Question 3
d = {"Python":"Programming"}
(d1,d2), = d.items()
print("The 1st values:", d1)
print("The 2nd values:", d2)

#Question 4
a = {2:20, 1:10}
b = {3:30, 4:40}
c = {5:50, 6:60}
a.update(c)
c.update(a)
print("The first dictionary contains:",a )
print("The second dictionary contains:",b)
print("The third dictionary contains:",c)
print("The new dictionary contains:", c)

