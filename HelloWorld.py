import mypackage
import random
import json
import os

"""
This is my first Python code
In this code, I will try to use Python to manipulate vary data type and handle the code.
"""


def data_manipulation():
    print(f"\tData Manipulation Start...")  # \t will leave 8 spaces
    exec_lab1()
    exec_lab2()
    exec_lab3()
    exec_lab4()
    print(f"\tData Manipulation Start...End!")


def exec_lab4():
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


def demo_file_accessing():
    print(f"\tFile Accessing...Start")
    do_file_access_case1()
    do_file_access_case2()
    do_file_access_case3()
    do_file_access_case4()
    do_file_access_case5()
    print(f"\t in addition, Python also provides method: configparser.ConfigParser() to get the corresponding value from ini file. Please check from internet.")
    print(f"\tFile Accessing...End!")


def do_file_access_case5():
    from datetime import datetime
    input("\t case 5, now try to modify the content we created before, you can check the file first, then press any key...")
    with open("test.json", "r+") as file:
        data = json.load(file)
        data["modified_date"] = datetime.fromtimestamp(
            os.path.getmtime(os.path.basename(__file__))).strftime("%Y-%m-%d %H:%M:%S")
        data["file_size_byte"] = os.path.getsize(
            os.path.basename(__file__))
        # Move the file pointer to the beginning of the file
        file.seek(0)

        json.dump(data, file, indent=4)

        # Truncate any remaining content
        file.truncate()
    print(f"\t case 5, now try to modify the content we created before...Done!")


def do_file_access_case4():
    print(f"\t case 4, now try to access file as JSON format.")
    data = {"file_name": "", "modified_date": "", "file_size_byte": 0}
    try:
        with open("test.json", mode="w", encoding="utf-8") as file:
            data["file_name"] = os.path.basename(__file__)
            json.dump(data, file, indent=4)
    except Exception as e:
        # raise in here represents throw exception to outer function handle.
        raise
    print(f"\t case 4, now try to access file as JSON format...Done! You can check it from file.")


def do_file_access_case3():
    print(f"\t case 3, in particular cases, you may need to read the file line by line, that's say we put 3 numbers: 8, 6, 3 in each line of file: 'readline.txt' and want to get the sum.")
    sum, counter = 0, 0
    with open("readline.txt", mode="w", encoding="utf-8") as file:
        file.write("8\n6\n3")
    with open("readline.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            sum = sum+int(line)
            counter = counter+1
    print(f"\t case 3, after read file {counter} lines, the sum is: {sum}")


def do_file_access_case2():
    print(f"\t case 2, now we try to read content from file we created before, and print the content...")
    with open("test.txt", mode="r", encoding="utf-8") as file:
        print(
            f"\t case 2, now we try to read content from file we created before, and print the content...Done! the content is: '{file.read()}'")


def do_file_access_case1():
    print(f"\t case 1, try to create a file named:'test.txt', and write a line:'hello world!'...")
    # For the detailed information about OpenTextMode, please check README.md
    # Recommend specify encodeing="utf-8" as default to avoid encoding issue occurs.
    with open("test.txt", mode="w", encoding="utf-8") as file:
        file.write("hello world!")
    print(f"\t case 1, try to create a file named:'test.txt', and write a line:'hello world!'...Done!")


def demo_random_and_statistics():
    print(f"\tRandom&Statistics...Start")
    do_random_choice()
    print(
        f"\t try to use funcion:random.sample([1, 5, 6, 10, 20], 3) five times, let's see what will be happen! ")
    for x in range(5):
        var_result = random.sample([1, 5, 6, 10, 20], 3)
        print(f"\t  round:{x+1}, the result is: {var_result}")

    var_result = [1, 5, 8, 20]
    random.shuffle(var_result)
    print(
        f"\t try to use funcion:random.shuffle([1, 5, 8, 20]), the result is: {var_result}")

    print(f"\t try to use function: random.random() to get the random number between 0.0 ~ 1.0.")
    for x in range(5):
        data = random.random()  # the data type of return value is float.
        print(f"\t  round: {x+1}, result is: {data}")

    print(f"\t try to use function: random.uniform(1.0, 10.0) to get the random number between 1.0 ~ 10.0.")
    for x in range(5):
        # the data type of return value is float.
        data = random.uniform(1.0, 10.0)
        print(f"\t  round: {x+1}, result is: {data}")

    print(f"\t try to use function: random.normalvariate(100, 10) to get the random number which follows standard deviation between 90 ~ 110.")
    for x in range(5):
        # it doesn't mean the number you get from random.normalvariate(100,10) will between 90 ~ 110 exactly, sometimes the return value will out of sigma.
        data = random.normalvariate(100, 10)
        print(f"\t  round: {x+1}, result is: {data}")

    print(f"\tRandom&Statistics...End!")


def do_random_choice():
    var_counter = 0
    for var_counter in range(5):
        var_result = random.choice([1, 5, 6, 10, 20])

        if (var_counter > 0):
            var_result_str = var_result_str + ", " + str(var_result)
        else:
            var_result_str = str(var_result)
        var_counter += 1

    print(
        f"\t try to use funcion:random.choice([1,5,6,10,20] five times, and the result is: {{{var_result_str}}}")


# Main Function
if __name__ == "__main__":
    # determine and execute from main function
    # be aware the function must to be declare before using
    while True:
        mypackage.common.clean_screen()
        print("MAIN FUNCTION")
        print("  [1]. Demostrate how to manipulate data in Python.")
        print("  [2]. Demostrate how to handle loop in Python.")
        print("  [3]. Demostrate how to use function resilient.")
        print("  [4]. Demostrate how to access data from file.")
        print("  [5]. Demostrate random and statistics module.")
        print("  [X]. Exit")

        # ask user input from keyboard.
        var_opt = input(
            "\nPlease input the number of function you want to run: ")

        if var_opt.upper() == "X":
            print("\nSee You!\n")
            break

        try:
            var_opt = int(var_opt)
        except ValueError:
            input("Invalid input. Please enter a valid integer.")

        try:
            if var_opt == 1:
                data_manipulation()
            if var_opt == 2:
                loop_handling()
            if var_opt == 3:
                function_handling()
            if var_opt == 4:
                demo_file_accessing()
            if var_opt == 5:
                demo_random_and_statistics()
            var_opt = input("\nPress any key to go back to main function...")
        except Exception as e:
            print(f"\tOops! We got errors! {{error message: {e}}}")
            var_opt = input("\nPress any key to go back to main function...")
