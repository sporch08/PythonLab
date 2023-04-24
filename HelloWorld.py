import os

"""
This is my first Python code
In this code, I will try to use Python to manipulate vary data type.
Reference: (1) https://www.youtube.com/watch?v=wqRlKVRUV_k&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk
           (2) f-string https://peps.python.org/pep-0498/
"""
OS_WIN = "nt"
OS_UNIX = "posix"

def dataManipulation():
    print (f"\tData Manipulation Start...") #\t will leave 8 spaces
    print (f"\tLab 1: put the value in your code directly...")
    123
    123.45
    "this is test"
    (1, 2, 3)
    [4, 5, 6]
    {7, 8, 9} 
    {"a": "apple", "b": "banana", "c": "car"}
    print(f"\t in this function, we give the value but didn't assign it to corresponding variable, the program can be ran without errors.")
    print(f"\t when program runs, you won't see anything from standard output since we didn't print it.")
    print (f"\tLab 1: put the value in your code directly...DONE!\n")
    
    print (f"\tLab 2: numeric manipulation...")
    # the name of variable must start with letter, but you don't need to declare the type of variable.
    var_x = 3
    # the value can be updated by different type
    var_x = True
    var_x = "Hello"
    
    print(f"\t arithmetic of power can be represent two asterisk '**', e.g., 3**3={3**3}");
    print(f"\t use // to get quotient. e.g., 9//2={9//2}");
    print(f"\t use % to get quotient. e.g., 9%2={9%2}");
    print (f"\tLab 2: numeric manipulation...DONE!\n")
    print (f"\tLab 3: string manipulation...")
    
    # x=x+1 equal with x+=1
    # in Python, the value of string can use single quote or double quote. e.g., "test" or 'test'
    # if you want to put a value of string into variable and it over a line, you can use three of single quote or double quote to block it.
    var_y = ''' this is a test
    for putting the value of string into different lines in the code.
    '''
    var_y = "Hello"+"World"
    print(f"\t use symbol:+ to concatenate strings. e.g., Hello+World={var_y}");
    var_y=var_y*3
    print(f"\t you also can use symbol:* to repeat the string. e.g., Hello*={var_y}");
    
    var_y = "HANDLE-CHARACTER"
    print (f"\t remember, the index of string in Python starts from 0.")
    print (f"\t let's use a string and handle it by using array. Given the value of str1={var_y}");
    print (f"\t print(str1[1:4])={var_y[1:4]}"); # slice case
    print (f"\t print(str1[1:])={var_y[1:]}"); # slice case
    print (f"\t print(str1[:4])={var_y[:4]}"); # slice case
    print (f"\tLab 3: string manipulation...DONE!\n")
   
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
    print (f"\tLab 4: data structure manipulation...")
    print (f"\t in this demo, the program will illustrate how to use List & Tuple.");
    var_list = [12, 60, 15, 70, 90];
    var_tuple = (12, 60, 15, 70, 90);
    var_len_z = len(var_list)
    print (f"\t here we have a list:{*var_list,}, length={var_len_z}") # remember you need put asterisk in front of variable, then add a comma after list variable to remove braces.
    var_list[2]=99
    print (f"\t you can update any one of them by index from 0. e.g., var_z[2]=99, the result will be:{*var_list,}")
    print (f"\t you also can use slice way to get a sub list by specified range, e.g., var_z[2:4]={*var_list[2:4],}")
    var_list[1:3]=[88,77]
    print (f"\t you also can update a part of list by using silce way. For example, we can set var_z[1:3]=[88,77], then we will get a new list like:{*var_list,} ")
    var_list = var_list + [100,17]
    print (f"\t if you want to add more elements at the tail of array, look this example => var_z=var_z+[100,120]. The reulst will be:{*var_list,}")
    var_list.sort()
    print (f"\t last, you can use .sort() to sort your list. The result will be:{*var_list,}")    
    print (f"\t at begining, we initiated a Tuple which value is the same with list:{*var_tuple,}")
    print (f"\t you can sort Tuple by sorted(), here is an example: {*sorted(var_tuple),}")
    
    try:
        print (f"\t if you try to update the Tuple like this: var_tuple[0] = 99, you will...")
        var_tuple[0] = 99
    except TypeError as e:
        print (f"\t oops! you got an error:{e}")
    print (f"\tLab 4: data structure manipulation...DONE!")
    print (f"\tData Manipulation Start...End!")


# determine and execute from main function
# be aware the function must to be declare before using
if __name__ == "__main__":    
    if os.name == OS_WIN:
        os.system('cls')
    elif os.name == OS_UNIX:
        os.system('clear')    
    
    print ("==MAIN FUNCTION==")
    dataManipulation()
    print ("==PROGRAM END==\n\n")

