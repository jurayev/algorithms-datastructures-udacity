"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from collections import Counter
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def show_codes_called_in_bangalore(calls):
    codes = get_area_codes(calls)  # Time O(n) Space O(n)
    unique_codes = sorted(set(codes))  # Type casting to set O(n) + Sort O(n log n). Space O(n)
    print("The numbers called by people in Bangalore have codes:")
    for record in unique_codes:  # O(n) for the worst case
        print(record)

    print_percentage_from_to_bangalore(codes)  # Time O(n) Space O(n)


def print_percentage_from_to_bangalore(codes):
    # Counter is a subclass of Dict and requires order of O(n) to traverse all elements of iterable input. Space used O(n)
    counted_codes_per_area = Counter(codes)  # O(n)
    total_codes = len(codes)  # O(1)
    total_codes_bangalore = counted_codes_per_area['(080)']  # Dict get Time complexity O(1), Space (1)
    percent = total_codes_bangalore * 100 / total_codes  # float of max 4 bytes Space O(1)
    print(f"{percent:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


def get_area_codes(calls):
    codes = []  # Space complexity O(n)
    for record in calls:  # List loop O(n)
        if record[0].startswith("(080)"):
            code = extract_code(record[1])  # extract_code: O(1)
            codes.append(code)  # List append O(1)
    return codes


def extract_code(record):
    if record.startswith("("):
        ind = record.index(")")
        return record[:ind+1]
    return record[:4]


show_codes_called_in_bangalore(calls)
