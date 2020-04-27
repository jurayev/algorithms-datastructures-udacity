"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def show_number_spent_longest_time(calls):
    numbers = {}  # Space complexity O(2n) ~ O(n)
    for record in calls:  # List Loop O(n)
        numbers[record[0]] = numbers.get(record[0], 0) + int(record[3])  # Dict Store O(1), Dict Get O(1), List Index O(1*3)
        numbers[record[1]] = numbers.get(record[1], 0) + int(record[3])  # Dict Store O(1), Dict Get O(1), List Index O(1*3)
    longest = max(numbers, key=numbers.get)  # Max Dict O(n)
    print(f"{longest} spent the longest time, {numbers[longest]} seconds, on the phone during September 2016.")  # Dict Get is O(1)


show_number_spent_longest_time(calls)

