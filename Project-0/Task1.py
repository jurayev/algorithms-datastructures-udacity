"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def show_distinct_numbers(texts, calls):
    numbers = set()  # Space complexity O(n1 + n2)
    for record in texts:  # List Loop O(n1)
        numbers.add(record[0])  # Set Add O(1), List Get O(1)
        numbers.add(record[1])  # Set Add O(1), List Get O(1)
    for record in calls:  # List Loop O(n2)
        numbers.add(record[0])  # Set Add O(1), List Get O(1)
        numbers.add(record[1])  # Set Add O(1), List Get O(1)
    print(f"There are {len(numbers)} different telephone numbers in the records.")  # Set len operation O(1)


show_distinct_numbers(texts, calls)
