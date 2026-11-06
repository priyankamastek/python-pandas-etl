"""

Suppose you are pulling data from file, database or API, and has very 
large data.

There can be too much data to hold in memory

solution - load in chunks, perform operations on each, store the result, discard the chunk,
then load the next chunk

pandas function: read_csv()
  - specify the chunk :   chunksize
  The object created by read_csv is an iterable

  Iterating over data
  import pandas as pd
   result = []
   for chunk in pd.read_csv('data.csv', chunksize=1000):
      result.append(sum(chunk['x']))
   total = sum(result)
   print(total)

Iterating over data     
   import pandas as pd
   total = 0
   for chunk in pd.read_csv('data.csv', chunksize=1000):
     total+= sum(chunk['x'])
   print total  
"""

"""
Scenario: Sometimes, the data we have to process reaches a size 
that is too much for a computer's memory to handle. 
This is a common problem faced by data scientists. 

A solution to this is to process an entire data source chunk by chunk, 
instead of a single go all at once.

In this exercise, you will do just that.
 You will process a large csv file of Twitter data in the same way 
 that you processed 'tweets.csv

 The pandas package has been imported as pd and the file 'tweets.csv' 
 is in your current directory for your use.

 # Initialize an empty dictionary: counts_dict


# Iterate over the file chunk by chunk
for ____ in ____:

    # Iterate over the column in DataFrame
    for ____ in ____:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)

"""


"""
solution:

# Initialize an empty dictionary: counts_dict
counts_dict = {}
# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv', chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)
"""

"""
import pandas as pd

# Initialize dictionary
counts_dict = {}

# Read file in chunks
for chunk in pd.read_csv("tweets.csv", chunksize=10):

    # Iterate through values in the lang column
    for lang in chunk["lang"]:

        if lang in counts_dict:
            counts_dict[lang] += 1
        else:
            counts_dict[lang] = 1

print(counts_dict)

Using value_counts() on each chunk: pandas series value_count()

import pandas as pd

counts_dict = {}

for chunk in pd.read_csv("tweets.csv", chunksize=10):

    chunk_counts = chunk["lang"].value_counts()

    for lang, count in chunk_counts.items():
        counts_dict[lang] = counts_dict.get(lang, 0) + count

print(counts_dict)


"""