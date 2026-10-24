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

# Lists, Slicing and Methods in Python
players = ["Messi", "Ronaldo", "Neymar", "Mbappe", "Haaland"]
print("Original players :", players)

# Slicing [start:end:step]
top_three = players[0:3]
print("Top 3 players :", top_three)
reversed_players = players[::-1]
print("Reversed players list :", reversed_players)

# Common Methods: append, pop, sort
players.append("Vinicius")
removed_player = players.pop(1)  # bye Ronaldo for now
print(f"Removed: {removed_player}, Current squad: {players}")
players.sort()
print("Alphabetical squad :", players)

# Dictionaries and Sets in Python
# Dictionary (Key-Value pairs)
player_stats = {
    "name": "Messi",
    "club": "Inter Miami",
    "goals": 820,
    "has_world_cup": True
}
print(f"{player_stats['name']} plays for {player_stats.get('club')}")

# Adding new key & looping through items
player_stats["assists"] = 375
for key, value in player_stats.items():
    print(f"{key.capitalize()} -> {value}")

# Sets (Unique elements & fast lookups)
favorite_clubs = {"Barcelona", "Real Madrid", "Man City", "Barcelona"}  # duplicates auto removed
favorite_clubs.add("Bayern")
print("Unique clubs :", favorite_clubs)
print("Is Barcelona in set? :", "Barcelona" in favorite_clubs)

# List Comprehensions (Pythonic way to build lists)
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtering and mapping in a single line
even_squares = [n**2 for n in numbers_list if n % 2 == 0]
print("Squares of evens :", even_squares)

# Transforming text items
skills = ["python", "javascript", "react", "fastapi"]
upper_skills = [skill.upper() for skill in skills]
print("Upper skills :", upper_skills)
