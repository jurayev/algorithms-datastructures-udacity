"""
Complexities:

Runtime O(n log n): 2 sort() executions with O(n log n) each, while iteration with O(n+n)
Space O(1)

"""
def min_platforms(arrivals, departures):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    arrivals.sort()
    departures.sort()
    min_required_platfotms = 1
    required_platforms = 1
    i = 1
    j = 0
    while j < len(departures) and i < len(arrivals):
        if departures[j] > arrivals[i]:
            i += 1
            required_platforms = (i - j)
            min_required_platfotms = max(min_required_platfotms, required_platforms)
        else:
            j += 1
            required_platforms -= 1
    return min_required_platfotms


def _test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    print(f"required platforms: {output}")
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

_test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
_test_function(test_case)