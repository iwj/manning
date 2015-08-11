In [1]: phone = {}

In [2]: phone["John"] = "555-1234"

In [3]: print phone
{'John': '555-1234'}

In [4]: phone["Test"] = 123

In [5]: print phone
{'Test': 123, 'John': '555-1234'}

In [6]: phone["Mary"] = "555-6789"

In [7]: phone
Out[7]: {'John': '555-1234', 'Mary': '555-6789', 'Test': 123}

In [8]: print phone
{'Test': 123, 'John': '555-1234', 'Mary': '555-6789'}

In [9]: print phone["Mary"]
555-6789

In [10]: print type(phone["Mary"])
<type 'str'>

In [11]: type(phone["Mary"])
Out[11]: str

In [12]: phone.keys()
Out[12]: ['Test', 'John', 'Mary']

In [13]: phone.values()
Out[13]: [123, '555-1234', '555-6789']

In [14]: phone[True] = "测试布尔值作为键"

In [15]: phone
Out[15]:
{True: '\xe6\xb5\x8b\xe8\xaf\x95\xe5\xb8\x83\xe5\xb0\x94\xe5\x80\xbc\xe4\xbd\x9c\xe4\xb8\xba\xe9\x94\xae',
 'John': '555-1234',
 'Mary': '555-6789',
 'Test': 123}

In [16]: print phone
{'Test': 123, True: '\xe6\xb5\x8b\xe8\xaf\x95\xe5\xb8\x83\xe5\xb0\x94\xe5\x80\xbc\xe4\xbd\x9c\xe4\xb8\xba\xe9\x94\xae', 'John': '555-1234', 'Mary': '555-6789'}

In [17]: phone[True] = "bool cool!"

In [18]: print phone
{'Test': 123, True: 'bool cool!', 'John': '555-1234', 'Mary': '555-6789'}

In [19]: phone[("I", "Love", "Python")] = "cuple"

In [20]: print phone
{'Test': 123, True: 'bool cool!', 'John': '555-1234', 'Mary': '555-6789', ('I', 'Love', 'Python'): 'cuple'}

In [21]: phone[("I", "Love", "Python")] = "cuple"

In [22]: phone[("I", "Love", "Python")] = "cuple cool"

In [23]: print phone
{'Test': 123, True: 'bool cool!', 'John': '555-1234', 'Mary': '555-6789', ('I', 'Love', 'Python'): 'cuple cool'}

In [24]: phone[2015] = "int cool"

In [25]: phone[3.14] = "float cool"

In [26]: phone
Out[26]:
{True: 'bool cool!',
 3.14: 'float cool',
 2015: 'int cool',
 'John': '555-1234',
 'Mary': '555-6789',
 'Test': 123,
 ('I', 'Love', 'Python'): 'cuple cool'}

In [27]: phone.keys()
Out[27]: [True, 3.14, ('I', 'Love', 'Python'), 'Test', 'John', 'Mary', 2015]

In [28]: type(phone.keys())
Out[28]: list

In [29]: del phone["Test"]

In [30]: phone
Out[30]:
{True: 'bool cool!',
 3.14: 'float cool',
 2015: 'int cool',
 'John': '555-1234',
 'Mary': '555-6789',
 ('I', 'Love', 'Python'): 'cuple cool'}

In [31]: 3.14 in phone
Out[31]: True

In [32]: "方滨兴" in phone
Out[32]: False
