>>> # List example
>>> prime_numbers = [2, 3, 5, 7, 11, 14]
>>> # Tuple example
>>> perfect_squares = (1, 4, 9, 13, 22, 43, 11, 37)
>>> # Display lengths
>>> print("# Primes = ", len(prime_numbers))
# Primes =  6
>>> print("# Squares = ", len(perfect_squares))
# Squares =  8
>>> # Iterate over both sequences
>>> for p in prime_numbers:
...     print("Prime: ", p)
... 
Prime:  2
Prime:  3
Prime:  5
Prime:  7
Prime:  11
Prime:  14
>>> for n in perfect_squares:
...     print("Squares: ", n)
... 
Squares:  1
Squares:  4
Squares:  9
Squares:  13
Squares:  22
Squares:  43
Squares:  11
Squares:  37
>>> print("List Methods")
List Methods
>>> print(dir(prime_numbers))
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> print(80*"-")
--------------------------------------------------------------------------------
>>> print("Tuple methods")
Tuple methods
>>> import sys
>>> print(dir(sys))
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions']
>>> list_eg = [1,2,3,"a","b","c",True,3.14159]
>>> tuple_eg = (1,2,3,"a","b","c",True,3.14159)
>>> print("List size= ", sys.getsizeof(list_eg))
List size=  120
>>> print("List size= ", sys.getsizeof(tuple_eg))
List size=  104
>>> # the output is different because a list occupies more memory than a tuple
>>> # you can add data, remove data or change data in lists, but you cannot change a tuple at all
>>> #tuples are immutable, once made, they cannot be changed but they can be made more quickly than lists
>>> import timeit
>>> list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=(1000000)
>>> tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=(1000000)
>>>print("List time: ", list_test)
>>>print("Tuple time: ", tuple_test)
List time: 0.104858...
Tuple time: 0.014344...
# it takes much more time to make lists than tuples, so tuples are useful

>>> empty_tuple =()
>>> test1=("a")
>>> test2=("a", "b")
>>> test3=("a", "b", "c")
>>> print(empty_tuple)
()
>>> print(test1)
a
>>> print(test2)
('a', 'b')
>>> print(test3)
('a', 'b', 'c')
# tuple containing single element creates an output different from the others, it looks like a string not a tuple. test1 is a string, to make it a tuple you need to ad a "," to the end (test1=("a",) would create a tuple)

>>> testa=1,
>>> testb=1, 2
>>> testc=1, 2, 3
>>> print(testa)
(1,)
>>> print(testb)
(1, 2)
>>> print(testc(1, 2, 3)
# all of the above are tuples 

#using lists
>>> survey = (27, "Vietnam", True)
>>> age = survey[0]
>>> country = survey[1]
>>> knows_python = survey[2]
>>> print("Age =", age)
Age = 27
>>> print("Country =", country)
Country = Vietnam
>>> print("Knows Python?", knows_python)
Knows Python? True
>>> #we can also make it by using tuples
>>> survey2 = (21, "Switzerland", False)
>>> age, country, knows_python = survey2
>>> print("Age =", age)
Age = 21
>>> print("Country =", country)
Country = Switzerland
>>> print("Knows Python?", knows_python)
Knows Python? False
#using tuples is much more easier, takes up less space

>>> a, b, c = (1,2,3,4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 3)
>>> #causes a value error if numbers are not equal
