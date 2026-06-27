print("Hello World~")
age=20
print(age)
first=int(input("enter the first num"))
second=int(input("enter the second num"))
print(first+second)
#####################################################################################################################################
while True:
    first_num=float(input("enter the first number : "))
    second_num=float(input("enter the second number : "))
    operation=input("enter operation type : ")
    if operation=="+":
        print(first_num+second_num)
    elif operation=="-":
        print(first_num-second_num)
    elif operation == "*":
            print(first_num * second_num)
    elif operation == "/":
                print(first_num/ second_num)
    else:
        print("error")
    repeat=input("do you want to preform another operation? (y/n)")
    if repeat=="yes":
        continue
    else:
        break
print("program exited")
####################################################################################################################################
phrase="nour omer"
print(phrase.index("n"))
print(phrase.replace("omer","hi"))

my_num=-5
print(abs(5))
print(pow(5,2))
print(min(9,7))
print(max(6,5))
print(round(5.4))
############################
# Mad_LipGame:
name=input("enter your name : ")
age=input("enter your age : ")
favorite_celebraty=input("enter your celebraty name : ")
print("Hi your name is + "+ name)
print(" your age is "+age)
print("your favorite celebraty is " + favorite_celebraty)
##########################################################################################################################
name=input("enter your name ")
print("Hello " + name)
###########################################################################################################################
date_of_birth=int(input("enter your date of birth "))
result=2026-date_of_birth
print(f" your age is {result}")
if result>=18:
    print("you can get a drive license ")
else:
    print("you are too young to drive ")
##################################
degrees=int(input("enter your degrees from 0 - 100"))
if degrees>=90:
    print("Excellent")
elif degrees>=50:
    print("passed")
else:
    print("failed")
##############################
number=1
while number<=3:
    print(number)
    number=number+1
print("done")
#######################################
number=5
while number>0:
    print(number)
    number=number-1
print("Blast off")
####################################
num=2
while num<=10:
    print(num)
    num=num+2
########################################
while True:
    word=input("enter words : ")

    if word=="exit":
        break
    print(word)
print("good bye")
##################################################
secret_number=6
while True:
    number=int(input("enter a number : "))
    if number==secret_number:
        print("you win ")
        break
    else:
        print("try again ")
        ##############################################################################################
        favorite_colors=["red","blue","green","yellow","pink"]
favorite_colors.append("black")
favorite_colors[0]="purple"
print(favorite_colors[0])
print(favorite_colors[2])
print(favorite_colors)
print(len(favorite_colors))
##############################################################################################################
#Dictionary
my_profile={
    "name":"nour",
    "age":21,
    "gender":"female",
    "language":"python"
}
print(my_profile["age"])
my_profile["major"]="medicine"
my_profile["language"]="Python"
del my_profile["gender"]
print(my_profile)






















































































































