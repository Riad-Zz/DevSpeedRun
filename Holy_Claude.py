print("Holy claude , What the hell ! ") 
# Variable and Data type  
age = 20
name = "Kamal"
sentence = f"{name} is {age}"
print(sentence , type(sentence)) 

# Input ,Output and Conversion
UserName = input("Whats your name : ")
salary = int(input("Write Down your Salary(monthly) : "))
increament = float(input("Write Down your yearly increament : "))
print(f"{UserName} , Your Salary Will be {salary + (salary * (increament/100.0))} next year")

#Conditional And Operators
goal = 2 ; time_Left = 20 ; Home = True 
if goal >= 3 or time_Left < 20:
    print("There is no way Man")
elif goal <= 2 and Home is True:
    print("Possible")
else :
    print("Great Match")

# Loops in Python 
# While Loop 
while goal != 10 :
    print(goal)
    goal+=1
    if goal == 7 :
        print(f"{goal} : Suiiiii")
        break 
# For Loops 
numbers  = [10,20,30,40,50]
for index , num in  enumerate(numbers , start=1) :
    print(index ,":", num)

for index,val in enumerate(range(1,10,2)) :
    print(index , " : " , val)


# Defining Functions 
def sum(val1 , val2) :
    result = val1 + val2 
    return result 
    
print(f"Total Sum :  {sum(10,20)}")

