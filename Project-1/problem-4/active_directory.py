class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


"""
For this problem I am using recursion to traverse the active directory hierarchy. Base approach is to check membership of
users list, if no user found check membership in other sub groups.
Complexity analysis:
~ Runtime O(nm), assuming 'n' is the number of groups and 'm' is the number of groups each group has.
~ Space (1), constant space complexity as no additional memory is used
"""
def is_user_in_group(user, group):
    if not user or not group:
        return None
    if user in group.get_users():
        return True
    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True
    return False


def build_active_directory_helper():
    #software sub groups lvl 3
    windows = Group("windows")
    windows.add_user("user_1")
    netware = Group("netware")
    unix = Group("unix")

    # server support groups lvl 2
    hardware = Group("hardware")
    software = Group("software")
    software.add_group(windows)
    software.add_group(netware)
    software.add_group(unix)

    # desktop support groups lvl 2
    tier_1 = Group("tier_1")
    tier_2 = Group("tier_2")
    tier_2.add_user("user_1")
    tier_3 = Group("tier_3")

    # IT department groups lvl 1
    server_support = Group("server_support")
    server_support.add_group(hardware)
    server_support.add_group(software)
    desktop_support = Group("desktop_support")
    desktop_support.add_group(tier_1)
    desktop_support.add_group(tier_2)
    desktop_support.add_group(tier_3)

    # IT department
    it_group = Group("it_group")
    it_group.add_group(desktop_support)
    it_group.add_group(server_support)
    it_group.add_user("admin")
    return it_group, desktop_support, software, unix

def _test_user_present_in_it_department():
    it_department = build_active_directory_helper()[0]
    is_found = is_user_in_group("user_1", it_department)
    assert is_found
    print("_test_user_present_in_it_department PASSED\n")

def _test_user_present_in_desktop_support_group():
    desktop_support = build_active_directory_helper()[1]
    is_found = is_user_in_group("user_1", desktop_support)
    assert is_found
    print("_test_user_present_in_desktop_support_group PASSED\n")

def _test_user_present_in_software_group():
    software = build_active_directory_helper()[2]
    is_found = is_user_in_group("user_1", software)
    assert is_found
    print("_test_user_present_in_software_group PASSED\n")

def _test_user_not_present_in_unix_group():
    unix = build_active_directory_helper()[3]
    is_found = is_user_in_group("user_1", unix)
    assert not is_found
    print("_test_user_not_present_in_unix_group PASSED\n")

def _test_user_not_present_in_it_department():
    it_department = build_active_directory_helper()[0]
    is_found = is_user_in_group("non_user", it_department)
    assert not is_found
    print("_test_user_not_present_in_it_department PASSED\n")

def _test_invalid_user():
    it_department = build_active_directory_helper()[0]
    is_found = is_user_in_group(None, it_department)
    assert not is_found
    print("_test_invalid_user PASSED\n")

def _test_invalid_group():
    is_found = is_user_in_group("admin", None)
    assert not is_found
    print("_test_invalid_group PASSED\n")


print("-"*10, "BEGIN TESTING", "-"*10)
_test_user_present_in_it_department()
_test_user_present_in_desktop_support_group()
_test_user_present_in_software_group()
_test_user_not_present_in_unix_group()
_test_user_not_present_in_it_department()
_test_invalid_user()
_test_invalid_group()
print("-"*10, "ALL TESTS PASSED", "-"*10)