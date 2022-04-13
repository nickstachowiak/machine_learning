''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

print('Question 1')
print('____________________________________________________')

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)

print("Even numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)

print("Odd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)

print('____________________________________________________')



''' 2)
find which days of the week have exactly 6 characters.
'''

print('Question 2')
print('____________________________________________________')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

weekdays2 = len(weekdays[0])
if len(weekdays[0]) == weekdays2:
    print([weekdays[0]])
if len(weekdays[1]) == weekdays2:
    print([weekdays[1]])
if len(weekdays[2]) == weekdays2:
    print([weekdays[2]])
if len(weekdays[3]) == weekdays2:
    print([weekdays[3]])
if len(weekdays[4]) == weekdays2:
    print([weekdays[4]])
if len(weekdays[5]) == weekdays2:
    print([weekdays[5]])
if len(weekdays[6]) == weekdays2:
    print([weekdays[6]])

print('____________________________________________________')







''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

print('Question 3')
print('____________________________________________________')

def remove_words(list1, remove_words):
    result = list(filter(lambda word: word not in remove_words, list1))
    return result
        
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_colors = ['orange','black']

print("Original list:")
print(colors)

print("Remove words:")
print(remove_colors)

print("After removing the specified words from the said list:")
print(remove_words(colors, remove_colors))

print('____________________________________________________')







''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

print('Question 4')
print('____________________________________________________')

def index(list1, list2):
    result = list(filter(lambda x: x not in list2, list1))
    return result

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8]

print("Original lists:")
print("list1:", list1)
print("list2:", list2)

print("Remove all elements from 'list1' present in 'list2:")
print(index(list1, list2))

print('____________________________________________________')




''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''

print('Question 5')
print('____________________________________________________')

def find_elements(str1, substring):
    result = list(filter(lambda x: substring in x, str1))
    return result

colors = ["red", "black", "white", "green", "orange"]
print("Original list:")
print(colors)

substring = "ack"
print("Substring to search:")
print(substring)
print("Elements of the said list that contain specific substring:")
print(find_elements(colors, substring))

substring = "abc"
print("Substring to search:")
print(substring)
print("Elements of the said list that contain specific substring:")
print(find_elements(colors, substring))

print('____________________________________________________')



''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

print('Question 6')
print('____________________________________________________')

def check_string(s):
    string = []
    if not any(x.isupper() for x in s):
        string.append('String should have 1 upper case character.')
    if not any(x.islower() for x in s):
        string.append('String should have 1 lower case character.')
    if not any(x.isdigit() for x in s):
        string.append('String should have 1 number.')
    if len(s) < 8:
        string.append('String length should be atleast 8.')    
    if not string:
        string.append('The string is valid.')
    return string
    
s = input("Input the string: ")
print(check_string(s))

print('____________________________________________________')










''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
print('Question 7')
print('____________________________________________________')

subject_score = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_score)

subject_score.sort(key = lambda x: x[1])
print("Sorting the List of Tuples:")
print(subject_score)
