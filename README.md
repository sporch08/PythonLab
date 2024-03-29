# PythonLab
- This is a practice place for newbies like me to note how to write Python Language.

# Introduction
- [HelloWorld.py: The practice as a beginner.](https://github.com/sporch08/PythonLab/blob/main/HelloWorld.py)
- [OpenDataHandsOn.py: The practice of accessing TW open data platform](https://github.com/sporch08/PythonLab/blob/main/OpenDataHandsOn.py)

# Notes for HelloWorld.py
## About Data Type
### The difference between List & Tuple (from ChatGPT)
- In Python, both lists and tuples are used to store a collection of items. However, there are some key differences between the two:
  1. Mutability: Lists are mutable, which means that you can add, remove, or change items in a list. Tuples, on the other hand, are immutable, which means that you cannot change the items once they are created.
  2. Syntax: Lists are defined using square brackets [], while tuples are defined using parentheses ().
  3. Use cases: Lists are generally used for collections of related items that need to be changed or manipulated, while tuples are typically used for collections of related items that will not be changed.
- Here are some situations where you might choose to use a tuple instead of a list:
  1. When you want to ensure that the data in your collection cannot be modified accidentally.
  2. When you want to create a collection that can be used as a key in a dictionary (because dictionaries require immutable keys).
  3. When you want to return multiple values from a function in a way that can't be easily modified outside of the function.
  4. When you want to optimize memory usage and performance, since tuples are smaller and faster than lists.
- Overall, the choice between using a list or a tuple will depend on your specific use case and the requirements of your program.    

### The difference between Java's properties and Python's dictionary
- The dictionary in Python is similar with the properties in Java. However, there are some differences between them:
  1. Data types: In Java, Properties can only store String key-value pairs, whereas in Python, dictionaries can store key-value pairs of any data type.
  2. Serialization: Properties in Java can be easily serialized to a file or stream, whereas Python dictionaries do not have built-in serialization capabilities. However, Python provides a module called pickle that can be used to serialize Python objects including dictionaries.
  3. Syntax: The syntax for accessing elements in a dictionary in Python is simpler and more concise than accessing properties in Java. In Python, you can access a value from a dictionary by using the key in square brackets: my_dict['key']. In Java, you need to use the getProperty() method to access a value from a Properties object: myProperties.getProperty("key").
  4. Ordering: Properties in Java are ordered, whereas dictionaries in Python are unordered. However, starting from Python 3.7, dictionaries are guaranteed to maintain insertion order.
  5. Default values: In Java, Properties provide a way to specify default values for missing keys by setting the default property. In Python, you can use the get() method to specify a default value for missing keys.    

## About File Access
### How to pretty the JSON file when I dump content?
- You can check from [official document](https://docs.python.org/3/library/json.html) to specify indent=4 when you're going to dump the content. It means the content will indent by four spaces.
### The impact if updating JSON file without using file.truncate() method 
1. New data is longer than the previous data: If the new data is longer than the previous data, but you don't truncate the file, the remaining content from the previous data will not be overwritten. It will still remain in the file after the end of the new data. This can result in a mixture of old and new data in the file.
2. New data is shorter than the previous data: If the new data is shorter than the previous data, but you don't truncate the file, the extra content from the previous data will still remain in the file after the end of the new data. This can result in leftover content from the previous data that is no longer valid or relevant.

## About Random and Statistics Methods
### Will I get the same result no matter I use random.random() or random.uniform(0.0, 1.0)?
- Most of the time, the result will be "No differences found between the distributions," indicating that the distributions are similar. However, there is still a small possibility that the result will be "Differences exist between the distributions." This occurs due to the internal algorithms used by the functions, which may produce subtle variations in the distribution, even when given the same conditions.
- It's important to note that these differences, if they occur, are typically very subtle and may not have practical significance for most use cases. The functions random.random() and random.uniform(0.0, 1.0) are both designed to provide a uniform distribution within the range (0, 1), and in most cases, they behave similarly.

# Notes for OpenDataHandsOn.py
## The instructions of accessing EPA API
- [EPA API Documentation](https://data.epa.gov.tw/paradigm)
## Troubleshooting on sort a list by multiple keys (accending then descending) 
 - [Basic Introduction](https://officeguide.cc/python-sort-sorted-tutorial-examples/)
 - [From Stakeoverflow](https://stackoverflow.com/questions/51252687/set-ascending-descending-for-each-column-when-sorting-by-multiple-columns)


## Miscellaneous
### A proper comment style of Python code
- Comments that are separated by a blank line should be used to indicate different sections within a function. For example, you may have a comment describing the purpose of the function, followed by a blank line, followed by comments describing different parts of the function's implementation.
- However, if you have a comment that directly precedes a function definition and there are no blank lines between them, the comment is considered part of the function's documentation, and the two blank lines guideline does not apply. In this case, the comment serves as a docstring, which provides a concise description of what the function does.


# Reference
1. [Main Material: cwpeng-course on Youtube](https://www.youtube.com/watch?v=wqRlKVRUV_k&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk)
2. [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)
3. [Format String-PEP 498 – Literal String Interpolation](https://peps.python.org/pep-0498/)
   - [related with input/output](https://docs.python.org/3/tutorial/inputoutput.html)
4. [Comparson of File Open Mode](https://ghost831105.medium.com/python%E5%AD%B8%E7%BF%92%E6%97%A5%E8%AA%8C-%E6%AA%94%E6%A1%88%E8%AE%80%E5%8F%96-%E5%AF%AB%E5%85%A5-%E6%A8%A1%E5%BC%8F%E6%AF%94%E8%BC%83-r-a-w-caac9e1aef72)
5. [Taiwan goverment open data portal](https://data.gov.tw/)
    - [API instructions](https://drive.google.com/file/d/13kPG4SJ_4IQI2mVBK_-i422U41BUb-d5/view)

