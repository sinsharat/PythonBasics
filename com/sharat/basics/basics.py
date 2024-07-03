import copy
from random import random
import uuid

i = 7
j = 3.23
k = -3.5322
n = -98
s = "abc"
boolean = True
print(i, ", ", j, ", ", k, ", ", n, ", ", s, ", ", boolean)

addition = j + k
subtraction = i - n
multiplication = i * j
division = n / i
exponent = i ** j
floor = n // k
modulo = i % j
print(addition, ", ", subtraction, ", ", multiplication, ", ", division, ", ", exponent, ", ", floor, ", ", modulo)
assignment_operators = 8

assignment_operators += 9
print("addition_assignment: ", assignment_operators)
assignment_operators -= 3
print("subtraction_assignment: ", assignment_operators)
assignment_operators *= 6
print("multiplication_assignment: ", assignment_operators)
assignment_operators /= 2
print("division_assignment: ", assignment_operators)
assignment_operators **= 2
print("power_assignment: ", assignment_operators)
assignment_operators //= 9
print("floor_assignment: ", assignment_operators)
assignment_operators %= 23
print("modulo_assignment: ", assignment_operators)
# slice of a string character
slice_string = "apple"[2]
print(slice_string)
# slice of string range till 2
slice_string = "apple"[:2]
print(slice_string)
# slice of string range from 2
slice_string = "apple"[2:]
print(slice_string)
# slice of string range from 1 (inclusive) to 4 (exclusive)
slice_string = "apple"[1:4]
print(slice_string)
# string concat
concat_string = "I am" + " " + "awesome"
print(concat_string)
# find data type of data
print(type(concat_string))
print(type(modulo))
print(type(i))
# convert to string
print(type(str(division)))
# escape sequences
print("This are \" \t \n \" \' escape sequences")
# print inverted triangle
print(" ******* \n  *****  \n   ***   \n\t*\t")

# Take input from a user
name = input("What is your name?")
if name:
    print("Welcome", name, "!")
else:
    print("You did not enter a name")

# truthy and false values
print(bool(0))  # prints false
print(bool(0.0))  # prints false
print(bool(""))  # prints false
print(bool(3))  # prints true
print(bool(7.0))  # prints true
print(bool("Abd"))  # prints true

# convert string to int and float
string_num = 78
print(type(int(string_num)), int(string_num))
print(type(float(string_num)), float(string_num))


# functions
# functions signature end with : and separated by two new lines before and after the function
def multiply(num1, num2):
    return num1 * num2


def multiply_with_default(num1=7, num2=9):
    return num1 * num2


def multiply_and_print(num1, num2):
    print(num1 * num2)


def multiply_and_return_big_small_or_negative(num1, num2):
    result = num1 * num2
    if result < 0:
        return "negative"
    else:
        if result > 100:
            return "big number"
        elif result == 100:
            return "century"
        else:
            return "small number"


def print_random_numbers_in_loop():
    counter = 0
    while counter < 10:
        print(random())
        counter += 1


def print_random_numbers_using_for_loop():
    for num in range(10):
        print(random())


def print_random_numbers_using_for_loop2():
    for num in range(10, 20):
        print(num)


def print_random_numbers_using_for_loop_with_step_increment():
    for num in range(10, 20, 2):
        print(num)


def print_characters_of_word():
    word = "for_loop"
    for letter in word:
        print(letter)


# function calls
print(multiply(8, 7))
print(multiply_with_default(3, 5))
print(multiply_with_default())
multiply_and_print(7, 3)
print(multiply_and_return_big_small_or_negative(10, 10))
# using import library random
print(uuid.uuid4())
# using random function directly from random import random
print(random())

# loop examples
print(print_random_numbers_in_loop())
print(print_random_numbers_using_for_loop())
print(print_random_numbers_using_for_loop2())
print(print_random_numbers_using_for_loop_with_step_increment())
print(print_characters_of_word())

# string methods
string_letters = "The quick brown fox"
string_num = "123456"
print(string_letters.lower())  # converts to lower case
print(string_letters.upper())  # converts to upper case
print(string_letters.title())  # converts to title case (All first letter of word is capital)
string_letters = string_letters.replace("The", "A")  # replace a word/letter with another word/letter
print(string_letters)
string_letters = string_letters.join(["jumped", "over"])  # join two or more strings
string_letters = string_letters.join("the lazy dog.")  # join two strings
print(string_letters)
print(string_letters.split())  # splits a string into an array using space
print(string_letters.split(" "))  # splits a string into an array using delimiter
print(string_letters.islower())  # checks whether all letters are lower case
print(string_letters.upper().isupper())  # checks whether all letters are upper case
print(string_letters.isalpha())  # checks whether the string has alphanumeric
print(string_letters.isalnum())  # checks whether the string is alphanumeric
print(string_num.isdecimal())  # checks whether the string has only numbers
print(string_letters.isspace())  # checks if the string has only spaces
print(string_letters.istitle())  # checks whether string has title case
print(string_letters.startswith("A"))  # checks whether the string starts with given letter/word
print(string_letters.endswith("fox"))  # checks whether the string starts with given letter/word
print(len(string_letters))  # prints the length of the string
print("abc".rjust(15, "*"))  # fills with characters defined for the remaining length on the right side
print("abc".ljust(15, "*"))  # fills with characters defined for the remaining length on the left side
print("abc".center(15, "*"))  # fills with characters defined for the remaining length on the both sides
print("   abc   ".strip())  # removes spaces from both sides of a string
print("   abc   ".lstrip())  # removes spaces from left sides of a string
print("   abc   ".rstrip())  # removes spaces from right sides of a string
print("My {} is {}.".format("name", "sharat"))  # string format example

# list
list_example1 = [1, 2, 3, 4, 5]
list_example2 = ["apple", "boy", "cat", "dog"]
list_example3 = [["vegetables", "fruits"], ["toys"], ["dresses", "shoes"]]
list_example4 = ["abc", 1, 3.98]
print(1 in list_example1)  # in condition
print("cat" in list_example2)  # in condition
print(["vegetables", "fruits"] in list_example3)  # in condition
print(9 not in list_example1)  # not in condition
print("donkey" not in list_example2)  # not in condition
print(["toys"] not in list_example3)  # not in condition
print(list_example2[0])  # print first item in the list
print(list_example3[2][1])  # access item in a list of list
print(list_example2[3][0])  # access a list item character
print(list_example2[-1])  # access a list item from last index
# list slicing
print(list_example2[:2])  # sliced list less than index 2
print(list_example2[1:])  # sliced list from index 1
print(list_example2[1:3])  # slice index from index 1 and less than index 3
# adding items to the list
list_example2.append("zebra")  # add elements to the end of the list
print(list_example2)
list_example2.insert(1, "monkey")  # add elements at a specified index
print(list_example2)
# reassigning list items
list_example2[3] = "puppy"  # re-assign value at index 3
print(list_example2)
list_example3[1] = ["toys", "board games"]  # re-assign value to a list at a given index
print(list_example3)
list_example1[2:5] = [7, 8, 9]  # re-assign a slice of list with given values i.e. index 2,3,4 get reassigned
print(list_example1)
list_example1[len(list_example1):] = [10, 11, 12]  # add new values added to the end of list
print(list_example1)
list_example1[3:4] = [list_example1[3], 7, 77, 777]  # add new values added to the list from specified index
print(list_example1)
# del and list methods
del list_example1[0]  # delete first element from list_example1
print(list_example1)
list_example2.remove("boy")  # delete element by name
print(list_example3.pop())  # removes last element from the list and also removed item is returned
print(list_example3.pop(0))  # removes the specified index element from the list and also removed item is returned
# sort items in the list
list_example1.sort()  # sort numbers in ascending order
print(list_example1)
list_example1.sort(reverse=True)  # sort numbers in descending order
print(list_example1)
list_example2.sort()  # sort words in ASCII ascending order
print(list_example2)
list_example2.sort(reverse=True)  # sort words in descending order
print(list_example2)
list_example2.append("Snake")
list_example2.sort()
print(list_example2)
# sorts capital letters first followed by small letters in ascending
# noinspection PyTypeChecker
list_example2.sort(key=str.lower)
print(list_example2)
# noinspection PyTypeChecker
list_example2 = sorted(list_example2, key=str.lower)
print(list_example2)
# find index of an item in the list
print(list_example2.index("Snake"))  # find index number of the item in the list
# copy items rather than reference
list_example5 = copy.deepcopy(list_example2)
list_example5[1] = "girl"
print(list_example5)
print(list_example2)  # modified list in list_example5 does not affect list_example2

# dictionaries
console = {"sony": "playstation", "microsoft": "xbox"}
print([console["sony"]])  # prints value of abc
birth_years = {1985: "sharat", 1987: "shweta", 2017: "shivanshika"}
print(birth_years)  # prints entire dictionary
print(birth_years[1985])  # prints value of key 1985 in birth_years dictionary
# get method prints value of key in birth_years dictionary else the other value passed
print(birth_years.get(2017, "2017 key not found"))
print(birth_years.get(1984, "1984 key not found"))
print(birth_years.keys())  # prints all keys in birth_years dictionary
print(birth_years.values())  # prints all values in birth_years dictionary

# iterate over dictionary keys
print("Iterating over keys")
for birth_year in birth_years.keys():
    print(birth_year, ":", birth_years[birth_year])

# iterate over each item in dictionary
print("Iterating over items slice")
for birth_year_item in birth_years.items():
    print(birth_year_item[0], ":", birth_year_item[1])

# iterate over each item in dictionary
print("Iterating over items using key value")
for key, value in birth_years.items():
    print(key, ":", value)

# add values to dictionary
birth_years[1957] = "Devendra"
print(birth_years)
# get length of dictionary
print(len(birth_years))  # get length of the dictionary
# build dictionary using fromKeys
birth_years.fromkeys([1960], "Sarita")
print(birth_years)
sample_dic = {}.fromkeys("abc", "everlasting")
print(sample_dic)
sample_dic2 = {}.fromkeys(["abc", "def"], "alpha")
print(sample_dic2)
# dictionary pop removes the key value pair specified returning its value
print(sample_dic2.pop("abc"))
# dictionary popitem removes the last item from the dictionary returning the item
print(sample_dic)
print(sample_dic.popitem())
print(sample_dic)
# clear method removes all items in the dictionary
sample_dic.clear()
print(sample_dic)
# copy
sample_dic3 = sample_dic2.copy()
sample_dic3["stu"] = "xyz"
print(sample_dic2)
print(sample_dic3)
# update
sample_dic3.update({"stu": "rst"})  # updates the record on sample_dic3
print(sample_dic3)
sample_dic3.update({"lmn": "pqr"})  # adds an entry of it doesn't exist
print(sample_dic3)
# setdefault method
sample_dic.setdefault("Lenovo", "Think_pad")  # value updated with default value since it does not exists in sample_dic
print(sample_dic)
sample_dic.setdefault("Lenovo", "ThinkPad")  # value not updated with default value as the key already exists
print(sample_dic)
# create dictionary with dict function
empty = dict()  # creates empty dictionary
print(empty)
filled_dic = dict(microsoft="xbox", sony="playstation")
print(filled_dic)
filled_num_dic = dict(a=1, b=3)
print(filled_num_dic)

# tuples
tuple1 = ("abc", "def", "hij")
print(tuple1)
tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple2)
tuple3 = ("abc", True, 1)
print(tuple3)
tuple4 = tuple(["abc", "def", "hij"])  # creates tuple abc, def, hij
print(tuple4)
tuple5 = tuple("abcd")  # creates tuple with values a, b, c, d
print(tuple5)
tuple6 = (1, 2, 3, (4, 5, 6), (1, 2, 9), 1, 2, 3, 7)  # tuple having nested tuple
print(tuple6)
# slicing tuples
print(tuple1[:2])  # prints tuples at index till 2nd (excluded) index
print(tuple1[1:])  # prints tuples from index 1
print(tuple1[1:2])  # prints tuples from index 1 till 2nd index (excluded)
# tuple slicing with steps
print(tuple2[::3])  # stride length of 3 i.e. step of 3 starting from index 0
print(tuple2[1::2])  # stride length of 2 i.e. step of 2 starting from index 1
print(tuple2[7::-1])  # stride length of -1 i.e. step of -1 starting from index 7
print(tuple2[8::-2])  # stride length of -2 i.e. step of -2 starting from index 8
# tuple size in bytes
print(tuple2.__sizeof__())  # tuples occupy less size than lists
# tuple iteration
for element in tuple2:
    print(element)

count = 0
while count < len(tuple1):
    print(tuple1[count])
    count += 1

# tuple methods
print(tuple6[2])  # print item in a tuple
print(tuple6[3])  # print item in a tuple which is another tuple
print(tuple6[3][1])  # access item for a tuple within a tuple
print(tuple6.count(1))  # counts number of 1s in the tuple and not items inside another tuple
print(tuple6.index(7))  # prints index of 7 in the tuple, if not found error is thrown
print(tuple6.index(2))  # prints the first index of 2 where it is found
print(1 in tuple6)  # prints whether 1 is present in tuple 6
print(11 not in tuple6)  # prints whether 11 is not present in tuple 6

# sets
set1 = {1, 2, 3, 4}  # set is declared using curly braces
print(set1)
set2 = {"xyz", "abc", "stu", "abc"}  # duplicates added are excluded from the set
print(set2)
set3 = set({})  # create empty set
print(set3)
set4 = set(range(2, 12, 2))  # set creation using range starting from 2 till 12 (excluding) with a step of 2
print(set4)
print(6 in set4)  # prints whether 6 is present in set4
print(11 not in set4)  # prints whether 11 is not present in set4
# set methods
set4.add(12)  # adds 12 to the existing set4
print(set4)
set4.remove(12)  # removes 12 from the set4 # trying to remove non-existent item throws error
print(set4)
set4.discard(12)  # removes 12 from the set4 # trying to remove non-existent item has no effect on the set
print(set4)
set2.clear()  # clears all the elements from the set
print(set2)
set5 = set4.copy()  # creates a copy of the set items and not the reference
print(set5 is set4)  # prints false
print(set4)  # prints set4 items
print(set5)  # prints set5 items
set6 = {1, 2, 3, 4}
set7 = set4.intersection(set6)  # intersection finds common items
print(set7)
set7 = set4 & set6  # another way to find common items
print(set7)
set8 = set4.difference(set6)  # removes common elements present in set6 from set 4
print(set8)
set8 = set4 - set6  # removes common elements present in set6 from set 4
print(set8)
