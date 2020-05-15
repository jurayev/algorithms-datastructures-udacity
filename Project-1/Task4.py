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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def show_telemarketers_numbers(calls, texts):
    outgoing_calls = set()  # Space complexity O(len(calls)) ~ O(n)
    incoming_and_texts = set()  # Space complexity O(2len(texts) + len(calls)) ~ O(3n)
    for call in calls: # Time complexity O(n)
        outgoing_calls.add(call[0])  # Set Add O(1)
        incoming_and_texts.add(call[1])  # Set Add O(1)
    for text in texts:  # Time complexity O(n)
        incoming_and_texts.add(text[0])  # Set Add O(1)
        incoming_and_texts.add(text[1])  # Set Add O(1)
    tele_numbers = outgoing_calls.difference(incoming_and_texts)  # O(len(incoming_and_texts))
    print("These numbers could be telemarketers: ")
    for number in sorted(tele_numbers):  # Time complexity for loop O(n). Time complexity for sort O(n log n)
        print(number)


show_telemarketers_numbers(calls, texts)
