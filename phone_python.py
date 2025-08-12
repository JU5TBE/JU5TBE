
save = True
first_save = True
new_save = True



user_info = {
    "name": "God",
    "age": "ad .infinitum"
}

user_info["email"] = "god@gmail.com"
print(user_info)
#adding the the same key just overrides info in that key

info_dict = user_info
print(info_dict)#modifying the copy mods the original
# like the borrow checker in rust but they don't check

if save == True:
    if first_save == True:
        dict_copy = user_info.copy()
    else:
         new_save = dict_copy.copy()
         del dict_copy
         
try:
    print(dict_copy)
except:
    print("taste successful")    

del user_info["age"] #delete stored info
print(user_info)
#user_info.pop("") also works
#user_info.popitem() pops the last item

#user_info.update(dict_copy)  combines two ducts,Key rules
    
if "name" in user_info:
    del user_info["name"] #delete
    print(user_info)
else:
    print("unavailable")   
    
    
try:
    print(user_info["name"])
except:
    print("removed successfully")   
    
print(dict_copy) #to remind you that the copy noted the-
#-info before we made changes to the original   


#sets, unordered, mutable, no duplcates
#set = {"curlyBracesLikeDictionary", "noKeys", 25, True, 25}
#the number 25 is not repeated, kinda like keys in dict
#print(set) 
#set2 = {set} creates set copy

#set2 = set([2, 25]) list in set, set not callable tho

#string_st =  set("hello") prints o, l, h, e
#empty set is recognised as dictionary
#rather use set method

#set.add(False)
#print(set)
#set.remove(False)
#set.discard(False) removes but if null no err
#clear and pop act here as well, like most data sets
#pop returns the thing then removes
#.union() combines without duplication
#.intersection() creates set for duplicates
#.difference() sets in set a but not set b
#.symmetric_difference() takes all different in both sets
#.update() updates without duplication
#.issubset first set elements all available in set2
#.isdisjoint, opposite of issubset
a = frozenset([1, 2])
print(a) #this works but the set() doesn't somehow

set_copy = frozenset(a) #cannot be mutated tho
#only Union intersection difference etc work
print(set_copy)





















button_clicked = True
removeBtn_clicked = True
clearBtn_clicked = True
undo_clicked = True
add_limit = 0
limit = 4
list = []

name = input("name ")

def hello(name):
    print("Welcome, " + str(name))
    return 1

if len(name) > 0:
     hello(name)
else:
        
        name = input("rewrite name ")
         
         
     
#hello(name)


if hello(1) == 1:
    reason = input("why are you here: ")
    print(reason)

def addtask():
   add_limit = 0
   limit = 4
   list = []

   while add_limit <= limit:
#if add limit is less than or equals to limit,Code below executes    
      if button_clicked:

       add_to_list = input("add to list: ")#asks for user to write what to add
       list.append(add_to_list)#adds user input to list
       print(list)#displays full list
       add_limit += 1 #helps create a limit for additions to list
  
  

       
      
      if add_limit > limit:
#when all spaces are used,I can then sell my soul    
       print('''you have reached the free
       plan limit,Subscribe for 5 dollars
       a month to gain unlimited spaces''')      
#end of anything to do with the while loop  


    
    
def countdown():    
    if list.index("countdown"):#if true is in the list
    
        countdown = input("select time ")
        countdown = int(countdown)
        i = countdown
        i = int(i)
        while i > -1:
            countdown -= 1
            print(countdown)
            i -= 1
            if i ==  0:
                 print("time has run out") 
     
    
    
    
def clear_btn():
    if clearBtn_clicked:#if user wants to remove everything
        double_check = input("to clear all enter 1: ")
        clear = double_check
        if clear == 1:#if user does write 1
             list.clear()#remove everything in the list
             print("list cleared successfully")
 
 
    
def undo():    
    if undo_clicked:
        undo = input("write undo to undo: ")
        if undo == "undo":#if user wrote undo
            list.pop()#undoes last change 
         
         
#...basically when you pay to remove a limit
#your just paying for two lines of code to be removed
#addtask()#calls out a function


def personal_info():
 class personal_info:
       name = "name"
       age = "age"
       gender = "male/female"
       email = "email"
       def description(self):
        desc_str = "%s is a %s %s with %.2f." 
        (self.name, self.age, self.gender, self.email)
        return desc_str
 
        
        
        
 person1 = personal_info()
 person1.name = input("name: ")
 person1.age = input("age: ")
 person1.gender = input("gender ")
 person1.email = input("email ")

#personal_info()




#print(personal_info.description())
#print(personal_info.description())
    
    
    
    
    
#dictionaries
def dictionary():
    personal_info = {
        "name": "anonymous",
        "age": "12"
    }

    usr_input = input("check for: ")
    print(personal_info.get(usr_input, "not recognisable"))
    dictionary()
        
#dictionary()    


#guessing game
import random
randomN = 0

def random_Number():
    print("it works")
    randomly_created_number = yield random.randint(1, 3)
    ###########################
random_Number() 
print(randomly_created_number)   
right_guess = randomly_created_number

attempts = 1

while attempts <= 3:
    
    user_input = input("guess number: ")
    
    if int(user_input) == right_guess:
        print("You guessed right")
        break
    else:
        print("try again")     
        attempts += 1
        
        
        
def remove():
    remove = input("what would you like to remove: ")
    if remove in list:
        list.remove(remove)
        print("removed")
    else:
        print("not available try again")
        remove = input("make sure it's there: ")
        remove()
            
            
remove()













print("Hello, World!")
#print=write

name = input("what are we? ")
#user enters data

name = name.lower()
#makes it lowercase whatever the input

if name == "atoms":
 #code below will exercute if name is = atom
    print("hello atoms")
    #code in if statement is indented
#code written this way doesn't apply it if statement
 
 
 
 
 
 #\n makes the text occur in a new line   
print(" write in a new line\nthis is how you can do it")





#you can check if is written in small letters only
#by add is to lower(),it will state either true or false
phrase = "I have beEn Dead for bilLions of yeArs"
phrase = phrase.lower().islower()#can add multiple phrases together





newWord = "length and index functions"
length_newWord = len(newWord)
index_newWord = newWord[5]
print(length_newWord)
print(index_newWord)





#replaces
newWord = newWord.replace("length", "Replace")
print(newWord)





#if phrase is not all lowercase basically
if phrase == False:
    print("phrase is false")
else:
        print("phrase is true")
   
   
#remainder operator
print(10 % 3)
#this is 10 / 3 which has remainder 1 

num = 112.55
print(str(num) + " numbr iz naw streng") 
print(int(num))#remove .55(no round off)
print(str(pow(3, 2)) + " 3 raised to 2")
print(str(max(2, 9, 8, 5,)) + " is max num")
print(str(min(2, 9, 8, 5,)) + " is mim num")
print(str(round(3.678)) + " rounding off function")


from math import *#imports extra math func
#research this from import thinlg

print(str(floor(3.99)) + " removes decimals")
print(int(3.99999999999))
print("not sure what the difference is")
print(str(ceil(3.000001)) + " rounds up no matter what")
print(str(sqrt(36)) + " square root")


#login thing google how to make last
name = input("Enter your name: ")
len_name = len(name)
if len_name > 5:
     print("Err, name must be less than 5 chatactes")
     name = input("Enter your name: ")
     print("Hi, " + name)
     
else:     
   print("Hi, " + name)
  



#basic_calc 
firstNum = input("Enter number: ")
secondNum = input("Enter number: ")  
answer = float(firstNum) + float(secondNum)
answer = str(answer)
print("answer is: " + answer)



#madlib game
#ahh sh*t here we input again.
color = input("pick a color: ")
plural_noun = input("insert plural noun: ")
celeb = input("insert celeb: ")

print("Roses are " + color)
print(plural_noun + "are blue")
print("I love " + celeb)


#finally something I don't know
#lists
#its literally the same thing as JavaScript 
#dude calls them list, us engineers call them arrays
#yah, njiniyela njiniyeling
list = [ True,"a list ", 45,"inside these brackets"]
print(list[-1])
print(list[-2:])#-2 onwards
print(list[1:3])#1 to 2
list[0] = False
print(list[0])



#adding two lists together
numbers = [36, 10, 3, 4, 45, 6, 18, 8,]
strings = ["name", True, "other name"]
strings.extend(numbers) 
#print(strings)
strings.append(True)#adds at the end
#print(strings)
list = []



#
button_clicked = False

if button_clicked:
    
    add_to_list = input("add to list: ")
    list.append(add_to_list)
    print(list)

    
#if strings.index("countdown"):#if true is in the list
    
    countdown = input("select time ")
    countdown = int(countdown)
    i = countdown
    i = int(i)
    while i > -1:
        countdown -= 1
        print(countdown)
        i -= 1
        if i ==  0:
          print("time has run out") 
     
     
#tuples and  lists a basically the same
#only difference is that tuples can't be changed   
tuple1 = ("Tom", "genius","executes comment code")
tuple_in_list = [("a list"), ("with tuples"), ("inside")]
list_in_tuple = (["tuple with a list"], ["just nje"])
tuple_in_list.append(("adding a tuple to a list"))


def say_hi(name, age):
    print("hi " + name + age)
    

say_hi("Anonymous", "19")
say_hi("ju5tbe", 19)


name = input("name ")

def hello(name):
    print("Welcome, " + name)
    return 1

if len(name) > 0:
     hello(name)
else:
         print("write name")
         name = input("rewrite name ")
         
         
     



if hello(1) == 1:
    reason = input("why are you here ")
    print(reason)
    
    
    
#dictionaries
personal_info = {
    "name": "anonymous",
    "age": "12"
}

usr_input = input("name ")
print(personal_info.get(usr_input))


lists = ["item1", "item2", "item3"]

for list in lists:
    print(lists)
   #will display all items in list
     #list 0 to list 2 etc but not 3 if range 1,10 range = 1,9
   
   
for index in range(Len(lists)):
    if index === 0:
        print("first item creation")
    print(index)
    #friends 0, friends 1 etc
    
       
for index in range(1200):
    print(1200)    
    



numbers = [36, 10, 3, 4, 45, 6, 18, 8,]
numbers.sort()
numbers.reverse()
print(numbers)
Ans = numbers[0] / numbers[-1]
print(Ans)
copy_numbers = numbers.copy()
print(copy_numbers)







def calculator():
    
    var1 = input("write number: ")
    var2 = input("symbol: ")
    var3 = input("second number: ")

    if len(var1) and len(var3) > 0:#a flex if statement
        if var2 == "+":
            def add():
                answer = int(var1) + int(var3)
                print(answer)
            add() 
            calculator()       
        elif var2 == "-":
            def subtract():
                answer = int(var1) - int(var3)
                print(answer)
            subtract() 
            calculator()   
        elif var2 == "/":
            def divide():
                answer = int(var1) / int(var3)
                print(answer)
            divide()  
            calculator()
        elif var2 == "*":
            def multiply():
                answer = int(var1) * int(var3)
                print(answer)
            multiply()
            calculator()  
        else:
            print(''' err pls add signs below
            + - / * 
            where necessary ''')  
            
            calculator()
    else:
        print("add a few numbers")
calculator()            
            
     

    


def car_game():
    user_input = input("> ")
    
    if user_input == "start":
        print("engine started...")
        car_started = True
        go = False
        stopped = False
        car_game()
        return car_started
    elif user_input == "go":
        print("speed: 100kph...")
        car_started = False
        go = True
        stopped = False
        car_game()
        return go  
    elif user_input == "stop":
        print("engine stopped...")
        car_started = False
        go = False
        stopped = True
        car_game()
        return car_stopped
    else:
        print("commands = start, stop, go...")    
    if car_started:
        print("car already started...")
        car_game()
    elif go:
        print("speed: 1200kph,max speed archieved...")
        car_game()
    elif car_stopped:
        print("car already stopped...")
        car_game() 
    
    
car_game()   










try:
    answer = 10/1
    number = int(input("enter Number!: "))
    print(number)
except ZeroDivisionError as err:
    print(err)    
except ValueError as err:
    print(err)
    print("basically enter a fucken number")  
    number = int(input("I ain't playing: "))
    number = str(number)
    print("your number is " + number + " ...goodboy")
    
 #probably better than if else   
 
 
power = open("text.txt", "r+")
#with the append you can store sort of permanent info
#for employee in power.readlines():
#   print(employee)
    
print(power.readlines()[0])



power.close()
#r reads file, w writes file, a appends(only add info)
#r+ reads and writes, prob isn't safe

JavaScriptappend = open("append57.js", "w")
#creates new files
JavaScriptappend.write("\nconsole.log('test complete')")






from callclass import student       
my_name = input("name: ")
my_age = input("age: ")
my_height = input("height: ")
my_race = input("race: ")
my_looks = input("looks: ")



I = student("Nkosiyapha", 19, "5ft 10", "Black", "6.5 to 8")
testing = student(my_name, my_age, my_height, my_race, my_looks)   


print(testing.attractiveness)   
class student:
    def __init__ (self, name, age, height, race, attractiveness):
        self.name = name
        self.age = age
        self.height = height
        self.race = race
        self.attractiveness = attractiveness



