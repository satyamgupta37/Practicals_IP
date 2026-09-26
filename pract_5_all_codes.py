#Question no:1
for i in range(1,11):
  if(i==5):
    break
  print(i)

#Question no:2
for i in range(1,11):
  if (i%3== 0):
    continue
  print(i)

#Question no:3
#program using break:
for i in range(1,11):
    if(i==5):
    break
  print(i)

#program using continue:
for i in range(1,11):
  if i==5:
    continue
  print(i)

#Question no:4
n=int(input("Enter number of elements to be added: "))
numbers=[]
for i in range(n):
  value=int(input("Enter elements: "))
  numbers.append(value)
search=int(input("Enter the number to search: "))
found=False
for i in range(len(numbers)):
  if numbers[i]==search:
    print(search,"Found at position",i)
    found=True
    break
if(found==False):  
  print(search,"not found in the list.")

#Question no:5
n=int(input("Enter a number: "))

for i in range(1,101):
  if (i%n==0):
    print("First number divisible by",n,"is",i)
    break;

#Question no:6
n=int(input("Enter number of elements to be added: "))
numbers=[]
for i in range(n):
  num=int(input("Enter number: "))
  numbers.append(num)

for num in numbers:
  if num<0:
    continue
  print(num)

#Question no:7
total=0
while True:
  num=int(input("Enter a number: "))
  if num==0:
    break
  if num<0:
    continue
    total += sum
  print("Sum=",total)

#Question no:8
correct_password="python123"
for i in range(1,4):
  password=input("Enter password: ")
  if password == correct_password:
    print("Login Successful")
    break
  else:
    print("Incorrect password")

#Question no:9
#print numbers from 1 to 5
for i in range(1,6):
  if i==3:
    pass
  else:
    print(i)

#Question no:10
for i in range(1,6):
  if (i%2==0):
    continue
  print(i)
  
