import os

"""
This is my first Python code
In this code, I will try to use Python to manipulate vary data type and handle the code.
"""

OS_WIN = "nt"
OS_UNIX = "posix"
CMD_CLEAN_WIN = "cls"
CMD_CLEAN_UNIX = "clear"


def data_manipulation():
    print(f"\tData Manipulation Start...")  # \t will leave 8 spaces
    exec_lab1()
    exec_lab2()
    exec_lab3()
    exec_lab4()
    print(f"\tData Manipulation Start...End!")


def exec_lab4():
    '''
    Here is the note I copied from ChatGPT, the difference between List & Tuple and the considerations. 
    In Python, both lists and tuples are used to store a collection of items. However, there are some key differences between the two:
      1. Mutability: Lists are mutable, which means that you can add, remove, or change items in a list. Tuples, on the other hand, are immutable, which means that you cannot change the items once they are created.
      2. Syntax: Lists are defined using square brackets [], while tuples are defined using parentheses ().
      3. Use cases: Lists are generally used for collections of related items that need to be changed or manipulated, while tuples are typically used for collections of related items that will not be changed.
    Here are some situations where you might choose to use a tuple instead of a list:
      1. When you want to ensure that the data in your collection cannot be modified accidentally.
      2. When you want to create a collection that can be used as a key in a dictionary (because dictionaries require immutable keys).
      3. When you want to return multiple values from a function in a way that can't be easily modified outside of the function.
      4. When you want to optimize memory usage and performance, since tuples are smaller and faster than lists.
    Overall, the choice between using a list or a tuple will depend on your specific use case and the requirements of your program.    
    '''
    print(f"\tLab 4: data structure manipulation...")
    print(f"\t in this demo, the program will illustrate how to use List & Tuple.")
    var_list = [12, 60, 15, 70, 90]
    var_tuple = (12, 60, 15, 70, 90)
    var_len_z = len(var_list)
    # remember you need put asterisk in front of variable, then add a comma after list variable to remove braces.
    print(f"\t here we have a list:{*var_list,}, length={var_len_z}")
    var_list[2] = 99
    print(
        f"\t you can update any one of them by index from 0. e.g., var_z[2]=99, the result will be:{*var_list,}")
    print(
        f"\t you also can use slice way to get a sub list by specified range, e.g., var_z[2:4]={*var_list[2:4],}")
    var_list[1:3] = [88, 77]
    print(
        f"\t you also can update a part of list by using silce way. For example, we can set var_z[1:3]=[88,77], then we will get a new list like:{*var_list,} ")
    var_list = var_list + [100, 17]
    print(
        f"\t if you want to add more elements at the tail of array, look this example => var_z=var_z+[100,120]. The reulst will be:{*var_list,}")
    var_list.sort()
    print(
        f"\t last, you can use .sort() to sort your list. The result will be:{*var_list,}")
    print(
        f"\t at begining, we initiated a Tuple which value is the same with list:{*var_tuple,}")
    print(
        f"\t you can sort Tuple by sorted(), here is an example: {*sorted(var_tuple),}")

    try:
        print(
            f"\t if you try to update the Tuple like this: var_tuple[0] = 99, you will...")
        var_tuple[0] = 99
    except TypeError as e:
        print(f"\t oops! you got an error:{e}")

    '''
    # Set, Dictionary
    # The dictionary in Python is similar with the properties in Java. However, there are some differences between them:
        (1) Data types: In Java, Properties can only store String key-value pairs, whereas in Python, dictionaries can store key-value pairs of any data type.
        (2) Serialization: Properties in Java can be easily serialized to a file or stream, whereas Python dictionaries do not have built-in serialization capabilities. However, Python provides a module called pickle that can be used to serialize Python objects including dictionaries.
        (3) Syntax: The syntax for accessing elements in a dictionary in Python is simpler and more concise than accessing properties in Java. In Python, you can access a value from a dictionary by using the key in square brackets: my_dict['key']. In Java, you need to use the getProperty() method to access a value from a Properties object: myProperties.getProperty("key").
        (4) Ordering: Properties in Java are ordered, whereas dictionaries in Python are unordered. However, starting from Python 3.7, dictionaries are guaranteed to maintain insertion order.
        (5) Default values: In Java, Properties provide a way to specify default values for missing keys by setting the default property. In Python, you can use the get() method to specify a default value for missing keys.    
    '''

    var_set1 = {1, 2, 3, 4}
    var_set2 = {3, 4, 5, 6}
    print(f"\t assume we have two sets: {var_set1}, {var_set2}")
    print(f"\t the result of intersection is: {var_set1 & var_set2}")
    print(f"\t the result of union is: {var_set1 | var_set2}")
    print(f"\t the result of difference is: {var_set1 - var_set2}")
    print(f"\t the result of symmetric difference is: {var_set1 ^ var_set2}")

    # Use set function to split a string into a set. Be aware this function is case sensitive.
    var_str = "An apple"
    var_set3 = set(var_str)
    print(
        f"\t given a string and set the value is: {var_str}, the result of using set function is: {var_set3}")
    # you also can use key word: 'in' to determine the given value exist in the set or not.
    print(f"\t does x in the set:{var_set3} ? {'x' in var_set3}")

    var_dic = {"name": "John", "age": 30, "city": "New York"}
    print(f"\t given a dictionary and print the value is: {var_dic}")
    print(f"\t print the value of key:name is: {var_dic['name']}")
    print(f"\t print the value of key:age is: {var_dic['age']}")
    # add new key:sex into dictionary:var_dic
    var_dic["sex"] = "Male"
    print(f"\t add a new key:sex and give the value is 'Male' {var_dic}")
    # update key:age to age_x
    var_dic['first_name'] = var_dic.pop('name')
    print(
        f"\t rename the key:name as first_name and show the result is: {var_dic}")
    # delete key:citys
    del var_dic['city']
    print(f"\t delete the key:city and show the result is: {var_dic}")

    print(f"\tLab 4: data structure manipulation...DONE!")


def exec_lab3():
    print(f"\tLab 3: string manipulation...")

    # x=x+1 equal with x+=1
    # in Python, the value of string can use single quote or double quote. e.g., "test" or 'test'
    # if you want to put a value of string into variable and it over a line, you can use three of single quote or double quote to block it.
    var_y = ''' this is a test
    for putting the value of string into different lines in the code.
    '''
    var_y = "Hello"+"World"
    print(f"\t use symbol:+ to concatenate strings. e.g., Hello+World={var_y}")
    var_y = var_y*3
    print(
        f"\t you also can use symbol:* to repeat the string. e.g., Hello*={var_y}")

    var_y = "HANDLE-CHARACTER"
    print(f"\t remember, the index of string in Python starts from 0.")
    print(
        f"\t let's use a string and handle it by using array. Given the value of str1={var_y}")
    print(f"\t print(str1[1:4])={var_y[1:4]}")  # slice case
    print(f"\t print(str1[1:])={var_y[1:]}")  # slice case
    print(f"\t print(str1[:4])={var_y[:4]}")  # slice case
    print(f"\tLab 3: string manipulation...DONE!\n")


def exec_lab2():
    print(f"\tLab 2: numeric manipulation...")
    # the name of variable must start with letter, but you don't need to declare the type of variable.
    var_x = 3
    # the value can be updated by different type
    var_x = True
    var_x = "Hello"

    print(
        f"\t arithmetic of power can be represent two asterisk '**', e.g., 3**3={3**3}")
    print(f"\t use // to get quotient. e.g., 9//2={9//2}")
    print(f"\t use % to get quotient. e.g., 9%2={9%2}")
    print(f"\tLab 2: numeric manipulation...DONE!\n")


def exec_lab1():
    print(f"\tLab 1: put the value in your code directly...")
    123
    123.45
    "this is test"
    (1, 2, 3)  # Tuple
    [4, 5, 6]  # List
    {7, 8, 9}  # Set
    {"a": "apple", "b": "banana", "c": "car"}  # Dictionary
    print(f"\t in this function, we give the value but didn't assign it to corresponding variable, the program can be ran without errors.")
    print(f"\t when program runs, you won't see anything from standard output since we didn't print it.")
    print(f"\tLab 1: put the value in your code directly...DONE!\n")


def loop_handling():
    var_counter = 0
    print(f"\tLoop Handling Start...")
    print(
        f"\t case1: you can give a list as an interator in Python, it will get each of elements one by one. e.g., for x in [4,1,2]")
    # It's different from Java code since Java code only can assign an iterator which is an integer type.
    for var_element in [4, 1, 2]:  # you can assign any type in List.
        print(f"\t  loop:{var_counter}, element={var_element}")
        var_counter += 1

    var_counter = 0
    print(f"\t case2: you can give a string as an interator in Python, it will get every character one by one. e.g., for c in \"Hello\"")
    for var_element in "Hello":
        print(f"\t  loop:{var_counter}, element={var_element}")
        var_counter += 1

    var_counter = 0
    print(f"\t case3: you also can use keyword: range to represent consecutive numbers. e.g., giving the rang(3), the result will be:")
    for var_element in range(3):
        print(f"\t  loop:{var_counter}, element={var_element}")
        var_counter += 1

    var_counter = 0
    print(f"\t case4: slicing also can be used with range, here is an example: rang(3,6), the result will be:")
    for var_element in range(3, 6):
        print(f"\t  loop:{var_counter}, element={var_element}")
        var_counter += 1

    # Imagine that the condition checking in the looping always exists. Thus you also can put the keyword: else with loop handling for particular work when it is going to the end.
    # Python also supports 'break' / 'continue' in the loop, but they are the same with other languages, so I won't put demo in here.
    var_counter = 0
    var_sum = 0
    print(f"\t case5:  print the sum from adding 1 to 10 by using 'else' to handle the loop.")
    for var_element in range(1, 11):
        var_sum += var_element
        var_counter += 1
    else:  # be aware if you use break in the loop, the else block won't be executed either.
        print(
            f"\t  we only print the result when loop end:{var_counter}, var_sum={var_sum}")
    print(f"\tLoop Handling Start...End!")


def func_with_default_value(arg1="Hello Word"):
    # We specify a particular default value for argument, if program calls the method without giving argument, it will print: "Hello Word"
    print(f"\t the argument method received is: \"{arg1}\"")


def func_with_multi_args(arg1=9, arg2=3):
    # In this function, you can see the order of argument can be changed from requester.
    # The Python will set default value to argument if you didn't pass all arguments when calling.
    print(f"\t the arg1={arg1}, arg2={arg2}, arg1/arg2={arg1/arg2}")


def func_with_packed_args(*args):
    # In Python, placing an asterisk (*) in front of an argument in a function definition has a specific meaning.
    # It is used to indicate that the argument should accept a variable number of positional arguments, often referred to as "packing" or "unpacking" arguments.
    # When you use an asterisk before a parameter name in a function definition, it allows the function to accept any number of positional arguments, which are then packed into a tuple.
    val_sum = 0
    print(
        f"\t in the function, it receives {len(args)} of the elements:{*args,}. ")
    # print(
    #    f"\t in the function, it receives the elements: {', '.join(str(arg) for arg in args)}")
    for element in args:
        try:
            val_sum = val_sum + int(element)
        except Exception:
            print(f"\t  element: '{element}' is invalid number, bypass.")
    print(f"\t the sum of this calling is: {val_sum}")


def func_with_unpacked_args(a, b, c):
    # Here is the usage of unpacking. I personally think it's not common and resilient since the length of arguments is fixed.
    # Compare with function: func_with_packed_args, you will see the rigidity.
    val_sum = 0
    print(
        f"\t in the function, it receives {a}, {b}, {c} three arguments.")
    if isinstance(a, int):
        val_sum += a
    else:
        print(f"\t  element: '{a}' is invalid number, bypass.")
    if isinstance(b, int):
        val_sum += b
    else:
        print(f"\t  element: '{b}' is invalid number, bypass.")
    if isinstance(c, int):
        val_sum += c
    else:
        print(f"\t  element: '{c}' is invalid number, bypass.")
    print(f"\t the sum of this calling is: {val_sum}")


def function_handling():
    print(f"\tFunction Handling Start...")
    func_with_default_value()
    func_with_default_value("Happy Python Programmer")
    print(f"\tcalling the function without specifying the arguments. default value arg1=9, arg2=3")
    func_with_multi_args()
    print(f"\tcalling the function by specifying the arguments.")
    func_with_multi_args(4, 2)

    # the order of argument can be changed by calling with specified argument name.
    print(f"\tcalling the function by specifying the arguments and the name of the arguments.")
    func_with_multi_args(arg2=4, arg1=2)
    print(f"\tcalling the function by specifying the partial arguments.")
    func_with_multi_args(arg2=4)

    # be aware you have to assign multiple arguments instead of assigning a List or Tuple since the function will package all arguments as Tuple.
    print(f"\tdemostrate the concept of packing arguments by using asterisk* in function arguments.")
    func_with_packed_args(1, 3, 5, "test", 7, 9, "a")

    var_tuple = [1, "a", 3]
    var_len_z = len(var_tuple)
    print(f"\t here we have a Tuple:{*var_tuple,}, length={var_len_z}")
    func_with_unpacked_args(*var_tuple)

    print(f"\tdemostrate the concept of unpacking arguments by using fixed arguments in function.")
    var_tuple = [1, 2, 3, 4]
    try:
        func_with_unpacked_args(*var_tuple)
    except TypeError as tpe:
        print(
            f"\t if you give much or less arguments, it throws exception. {{error message: {tpe}}}")
    print(f"\tFunction Handling Start...End!")


# determine the OS and execute the command of screen cleaning respectively.
def clean_screen(os_name):
    if os_name == OS_WIN:
        os.system(CMD_CLEAN_WIN)
    elif os_name == OS_UNIX:
        os.system(CMD_CLEAN_UNIX)


# Main Function
if __name__ == "__main__":
    # determine and execute from main function
    # be aware the function must to be declare before using
    while True:
        clean_screen(os.name)
        print("MAIN FUNCTION")
        print("  1.Demostrate how to manipulate data in Python.")
        print("  2.Demostrate how to handle loop in Python.")
        print("  3.Demostrate how to use function resilient.")

        # ask user input from keyboard.
        var_opt = input(
            "\nPlease input the number of function you want to run: ")

        try:
            var_opt = int(var_opt)
            break
        except ValueError:
            input("Invalid input. Please enter a valid integer.")

    if var_opt == 1:
        data_manipulation()
    if var_opt == 2:
        loop_handling()
    if var_opt == 3:
        function_handling()
