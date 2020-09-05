Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=["sai","abc",1,5,8.9,[5,10,6]]
>>> print(list1)
['sai', 'abc', 1, 5, 8.9, [5, 10, 6]]
>>> list1.reverse()
>>> print(list1)
[[5, 10, 6], 8.9, 5, 1, 'abc', 'sai']
>>> list1.index("abc")
4
>>> list1.remove(5)
>>> print(list1)
[[5, 10, 6], 8.9, 1, 'abc', 'sai']
>>> list1.append("ball")
>>> list1.append(["cat","dog",56])
>>> print(list1)
[[5, 10, 6], 8.9, 1, 'abc', 'sai', 'ball', ['cat', 'dog', 56]]
>>> list2=["reshma","teacher","rain"]
>>> list3=[88,5,9,1,4]
>>> list2.sort()
>>> print(list2)
['rain', 'reshma', 'teacher']
>>> list3.sort()
>>> print(list3)
[1, 4, 5, 9, 88]
>>> dit={"name":"vijay","age":"47","profession":"actor","place":"chennai"}
>>> print(dit)
{'name': 'vijay', 'age': '47', 'profession': 'actor', 'place': 'chennai'}
>>> dit.pop("place")
'chennai'
>>> print(dit)
{'name': 'vijay', 'age': '47', 'profession': 'actor'}
>>> dit.items()
dict_items([('name', 'vijay'), ('age', '47'), ('profession', 'actor')])
>>> dit.get("name")
'vijay'
>>> dit.copy()
{'name': 'vijay', 'age': '47', 'profession': 'actor'}
>>> dit.clear()
>>> print(dit)
{}
>>> set1=("apple","ball","cat",23,78,56,70,43,34.6)
>>> print(set1)
('apple', 'ball', 'cat', 23, 78, 56, 70, 43, 34.6)
>>> set1.count("cat")
1
>>> set1.count(79)
0
>>> set1.index(43)
7
>>> set1.index("apple")
0
>>> flight={23,56,8.6,"milk","sugar"}
>>> print(flight)
{'milk', 'sugar', 8.6, 23, 56}
>>> flight1={"banana","kitkat","dance",67,98,44,"milk",56}
>>> print(flight1)
{98, 67, 'milk', 'banana', 'dance', 44, 56, 'kitkat'}
>>> flight.copy()
{'milk', 8.6, 23, 56, 'sugar'}
>>> flight.difference(flight1)
{23, 8.6, 'sugar'}
>>> flight.difference_update(flight1)
>>> print(flight)
{'sugar', 8.6, 23}
>>> flight.intersection(flight1)
set()
>>> flight={23,56,8.6,"milk","sugar","honey"}
>>> flight.intersection(flight1)
{56, 'milk'}
>>> flight.remove("honey")
>>> print(flight)
{'milk', 'sugar', 8.6, 23, 56}
>>> string1="Good Morning!Have a nice day"
>>> print(string1)
Good Morning!Have a nice day
>>> string1.capitalize()
'Good morning!have a nice day'
>>> string2="HELLOOO"
>>> string2.capitalize()
'Hellooo'
>>> string1.center(5)
'Good Morning!Have a nice day'
>>> string2.center(20)
'      HELLOOO       '
>>> string2.index('m')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    string2.index('m')
ValueError: substring not found
>>> string2.index('e')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    string2.index('e')
ValueError: substring not found
>>> string2.index("l")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    string2.index("l")
ValueError: substring not found
>>> string1.index("G")
0
>>> string1.count("o")
3
>>> string1.upper()
'GOOD MORNING!HAVE A NICE DAY'
>>> #Assignment-1[List,dictionary,tuple,set,string]
