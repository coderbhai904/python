# the condition is to total marks is to the 40% and each subject student contain the marks of the 33%
name = input("please enter your name :")
mark1 = int(input("Please enter your english marks :"))
mark2 = int(input("please enter your hindi marks"))
mark3 = int(input("please enter your Math  marks"))
marks4 = int(input("please enter your  sst marks "))

checker = (mark1+mark2+mark3+marks4)
# if (checker>132 and mark1>=32 and mark2>32 and mark3>32 and marks4>32):
#     print("congratulation your are succesfully pass the exam" , name)

# else:
#     print("you are fail ")

print(checker)
if (checker>=132):
    print( name,"you scored a over all passing marks  ")

elif(checker==131):
        print(name,"you are promoted to next   class")
else:
    print( name,"you are fail in the exam (over all marks)")
    print("you need to repeate the  entire Class")

if(mark1>=33):
    print(name,"your are pass in the english exam" , mark1)
elif(mark1==32):
    print(name,"You get a grace marks in english exam")
else:
    print( name,"you are fail in the english exam" , mark1)

if(mark2>=33):
    print(name,"your are pass in the hindi exam" , mark2)
elif(mark2==32):
    print(name,"You get a grace marks in hindi exam")
else:
    print("your are fail in the hindi exam",mark2)

if(mark3>=33):
    print(name,"you are pass in the Math exam",mark3)
elif(mark3==32):
    print(name,"You get a grace marks in Math exam")
else:
    print(name,"you are fail in the Math exam",mark3)
if(marks4>=33):
    print(name,"you are pass in the sst exam",marks4)
elif(mark1==32):
    print(name,"You get a grace marks in sst  exam")
else:
    print(name,"you are fail in the sst exam",marks4)

   

    # this is secound program
if(mark1==32 and mark2==32 and mark3==32 and marks4==32):
    print(name," you get a grace marks in all subject only  one marks")
    print(name , "you are promoted to next  class ")
elif(mark1<33 and mark2<33 and mark3<33):
    print("you are completed fail you have no choice to retest")


print("Thank you for using this program")
print("Program is created by vishal Gupta")
print("Have a nice day")







