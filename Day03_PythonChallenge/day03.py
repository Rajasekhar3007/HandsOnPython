# Student Performance Analyser

name = input("Enter Your Name:")
#Personalization condition
if len(name) > 8:

  n = int(input("Enter No.of.Students:"))

  marks = [0] * n
  for i in range(n):
    marks[i] = int(input("Enter Marks:"))

  print(marks)
  valid = 0
  fail = 0
  for i in range(n):

        if marks[i] >= 90 and marks[i] <= 100:
            valid = valid + 1
            print(marks[i], "-> Excellent")

        elif marks[i] >= 75 and marks[i] <= 89:
            valid = valid + 1
            print(marks[i], "-> Very Good")

        elif marks[i] >= 60 and marks[i] <= 74:
            valid = valid + 1
            print(marks[i], "-> Good")

        elif marks[i] >= 40 and marks[i] <= 59:
            valid = valid + 1
            print(marks[i], "-> Average")

        elif marks[i] >= 0 and marks[i] <= 39:
            fail = fail + 1
            valid = valid + 1
            print(marks[i], "-> Fail")

        else:
            print(marks[i], "-> Invalid")
            
  print("Total Valid Students:", valid)
  print("Total Failed Students:", fail)

else:
    print("Name must be more than 8 characters")









