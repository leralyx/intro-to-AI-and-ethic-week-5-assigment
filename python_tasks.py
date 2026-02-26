a = [10, 20, 30, 40, 50]
b = a[-2:-4]
c = a[-4:-2]
print(b)
print(c)

#output:
#[]
#[20,30]

#why:
# here the result of the first onr is empty brackets -> since we cant take from right to left every slice should be taken from left to right 
#for the second one the logic is saved from left to right thats why we ve got this result from item with index -4 to -2

#-------------------------------------------------------------------------------------------------------------------------------

def change(data):
  data[0] = 100
  data = [1, 2, 3]
  return data

lst = [5, 6, 7]
result = change(lst)
print(lst)
print(result)

#output:
#[100,6,7]
#[1, 2, 3]

#why:
#process -> we ve created a list ([100,6,7]) , after that we ve created a variable which value is the result of the function. In the invokation we ve put that list as an argument so that the function receive a parameter to work with since the function is parametorized this is allow. "data" is our receive list and param.. Now we take the item of the list with the index 0 and we chage it. After we can see that now we change the list complitly, but in python it is important to consider that when you change a the list , the previous it dont desappear it is just reminded as previous list so it is kinda there but is not usable for us now.After there is a return of the data variable which is the new list that we ve just assign. 
#now we now that the value assign to result variable is the new list.After we have print lst and the result is [100,6,7] -> this happen bc lst itself was modify and the replacement do not mean how i ve said previous that the value disappear no just somewhere in some condition it will use the new value somewhere the previous. Now since we can the lst that was the initial variable we ve got it modify version. And for the last one it is just the result of the return of the function so [1, 2, 3].

#---------------------------------------------------------------------------------------------------------------------------------

def count_letters(text):
    dic = {}
    for letter in text :
           dic[letter] = text.count(letter)
    return print(dic)
            

count_letters("appple")

#---------------------------------------------------------------------------------------------------------------------------------

# data = (1, 2, 3)
# data[1] = 100

#first thing to understand is that tuples are immutable which means that you can make change on them.Since tuples cant be modified, you must create a new tuple.
#data = (1, 2, 3)
#data = (1, 4, 8)
#print(data) now it is going to work

#---------------------------------------------------------------------------------------------------------------------------------

# x = 10
# def test():
#   print(x)
#   x = 5
 
# test()

#here the problem is that we have a local x=5 that was create after being call which dumb bc even in real life you wont call someone that do not exist yet same here. Dont mistake the fact that we have a global variable , this variable was create before the function so the function dont see it kinda , but if you you had put the keyword global it would have worked.

#---------------------------------------------------------------------------------------------------------------------------------

def filter_numbers(numbers):
    result = []   
    
    for number in numbers:
        if number % 2 == 0 and number % 4 != 0:
            result.append(number)
    
    return result  


lst = [1,2,3,4,5,6,7,8,9,10,44,48,42]

filtered = filter_numbers(lst)
print(filtered)

#---------------------------------------------------------------------------------------------------------------------------------

def add_grade(student, subject, grade):
    student["grades"][subject] = grade
    
student = {
    "name": "Karisha",
    "grades": {
        "math": 90,
        "english": 75
    }
}

add_grade(student, "science", 85)   
add_grade(student, "math", 95)      

print(student)

#---------------------------------------------------------------------------------------------------------------------------------

def sum_pairs(pairs):
    answer = []
    
    for a, b in pairs:
        answer.append(a + b)
    
    return answer


pairs = [(1,2), (3,4), (5,6)]
print(sum_pairs(pairs))

#---------------------------------------------------------------------------------------------------------------------------------


def mystery(lst):
  lst = lst[::-1]
  lst.append(100)
  return lst

numbers = [1,2,3]
result = mystery(numbers)
print(numbers)
print(result)

#output :
#[1,2,3]
#[3,2,1,100]

# here we have a list called num that has a value of [1,2,3], after we invoke it in the function mistery and assign the result to the variable result.After in the function we can see the first manipulation which will reverse our list and after and a new element inside 100. So the first thing we gonna have as an output is [1,2,3] our first list and after we will receive [3,2,1,100]the new transformed one.

#---------------------------------------------------------------------------------------------------------------------------------

def analyze(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    total = 0
    even_count = 0
    odd_count = 0
    
   
    for n in numbers:
   
        if n > maximum:
            maximum = n
        
    
        if n < minimum:
            minimum = n
        
      
        total += n
       
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    average = total / len(numbers)
    
    return {
        "max": maximum,
        "min": minimum,
        "average": average,
        "even_count": even_count,
        "odd_count": odd_count
    }

print(analyze([1,2,3,4]))