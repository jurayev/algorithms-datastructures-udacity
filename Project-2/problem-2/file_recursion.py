import os

"""
File Recursion implementation
Design Approach is recursively traverse all subdirs under passed directory 

Complexity analysis:
Runtime O(n) for both best and worst cases, where n is the depth of file system tree under the tested path
Space O(n), where n is the number of files being searched for
"""
def find_files(suffix, path):

    def traverse_subdirs(path, index):
        paths = []
        dir_items = os.listdir(path)
        if len(dir_items) <= index:
            return []

        item = dir_items[index]
        next_item_path = os.path.join(path, item)
        if os.path.isfile(next_item_path):
            if next_item_path.endswith(suffix):
                paths.append(next_item_path)
        else:
            # if dir, traverse subdirs as well
            paths += traverse_subdirs(next_item_path, 0)
        # traverse next items at the same level
        paths += traverse_subdirs(path, index+1)

        return paths

    if not os.path.exists(path):
        return []

    return traverse_subdirs(path, 0)


def _test_find_c_files():
    expected_paths = ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
    actual_paths = find_files(suffix=".c", path="./testdir")
    assert sorted(expected_paths) == sorted(actual_paths)
    print("_test_find_c_files PASSED\n")


def _test_find_h_files():
    expected_paths = ['./testdir/subdir3/subsubdir1/b.h', './testdir/t1.h', './testdir/subdir5/a.h', './testdir/subdir1/a.h']
    actual_paths = find_files(suffix=".h", path="./testdir")
    assert sorted(expected_paths) == sorted(actual_paths)
    print("_test_find_h_files PASSED\n")


def _test_find_files_one_level_dir_tree():
    expected_paths = ['./testdir/subdir3/subsubdir1/b.c']
    actual_paths = find_files(suffix=".c", path="./testdir/subdir3/subsubdir1")
    assert expected_paths == actual_paths
    print("_test_find_files_one_level_dir_tree PASSED\n")


def _test_find_all_files():
    expected_paths = [
                      './testdir/subdir4/.gitkeep',
                      './testdir/subdir3/subsubdir1/b.h',
                      './testdir/subdir3/subsubdir1/b.c',
                      './testdir/t1.c',
                      './testdir/subdir2/.gitkeep',
                      './testdir/subdir5/a.h',
                      './testdir/subdir5/a.c',
                      './testdir/t1.h',
                      './testdir/subdir1/a.h',
                      './testdir/subdir1/a.c'
                      ]
    actual_paths = find_files(suffix="", path="./testdir")
    assert sorted(expected_paths) == sorted(actual_paths)
    print("_test_find_all_files PASSED\n")


def _test_no_files_found():
    actual_paths = find_files(suffix=".py", path="./testdir")
    assert [] == actual_paths
    print("_test_no_files_found PASSED\n")


def _test_find_files_invalid_path():
    actual_paths = find_files(suffix=".c", path="./invaliddir")
    assert [] == actual_paths
    print("_test_find_files_invalid_path PASSED\n")


print("-"*10, "BEGIN TESTING", "-"*10)
_test_find_c_files()
_test_find_h_files()
_test_find_files_one_level_dir_tree()
_test_find_all_files()
_test_no_files_found()
_test_find_files_invalid_path()
print("-"*10, "ALL TESTS PASSED", "-"*10)
