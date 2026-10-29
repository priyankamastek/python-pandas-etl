# Iterators VS iterables
"""
Iterable
Example: list, strings, dictionaries, file Connection
An object with an associated iter() method
Apply iter() to an iterable creates an iterator

Iterator object =    iter()
Iterator
produces next value with next()

Summary - an iterable is an object that can return an iterator, 
while an iterator is an object that 
keeps state and produces the next value when you call next() on it.

word = "Da"

it = iter(word)

next(it)

next(it)

next(it) -> StopIteration Error

Splat operator
word = "hello"
it = iter(word)
print(*it) -> unpacks all elements  

Pythonistais = {'hugo': 'bowne-anderson', 'francis': 'catro'}
for key, value in pythonisatis.items():
   print(key, value)

   
file = open('file.txt')
it = iter(file)
print(next(it))
"""

"""
Suppose you are pulling data from file, database or API, and has very 
large data.

There can be too much data to hold in memory.

solution - load in chunks, perform operations on each, store the result, 
discard the chunk, then load the next chunk

pandas function: read_csv()
  - specify the chunk :  chunksize
  - The object created by read_csv is an iterable

  Iterating over data

"""