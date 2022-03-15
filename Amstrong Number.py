#User Input
A = int(input("Enter Any number: "))
sum = 0
cube = A
while cube > 0:
   digit = cube % 10
   sum += digit ** 3
   cube //= 10
if A == sum:
   print(A,"is an Armstrong number")
else:
   print(A,"is not an Armstrong number")
