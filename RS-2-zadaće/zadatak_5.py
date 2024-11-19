#5. Vrati True ako je broj paran, inače vrati None:

"""def paran_broj(x):
if x % 2 == 0:
return True
else:
return None 
"""

paran_broj = lambda x: True if x % 2 == 0 else None

#test
print(paran_broj(4))  # Output: True
print(paran_broj(3))  # Output: None