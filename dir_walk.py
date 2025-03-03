"""
Run this code in an empty folder to create a directory structure with files on which exercises can be performed.
"""

import os, random
from datetime import datetime, timedelta

def create_structure() -> None:
    folders_name = './archives/guard_appl_{}'
    for i in range(1, 26):
        if not os.path.exists(folders_name.format(i)):
            os.makedirs(folders_name.format(i))
        for d in range(1, 60):
            open(folders_name.format(i) + '/{}_guard_appl_{}_d{}.tar.gz.enc'.format(
                random.randint(1111,9999), i, (datetime.now() - timedelta(days=d)).strftime('%Y-%m-%d')
                ), 'a').close()

def prettify_list(lst: list) -> None:
    return

def older_files(path: str, days: int) -> list:
    return []

def prettify_structure(files: dict) -> None:
    return

def move_files(path_f: str, path_t: str, days: int) -> None:
    return

def big_files(path: str, size: int) -> list:
    return []

def big_files_recursive(path: str, size: int) -> list:
    return []

def big_files_generator(path: str, size: int):
    return []

if __name__ == "__main__":
    create_structure()

    prettify_list([])
    
    older_files('./archives', 14)
    
    prettify_structure({})
    
    move_files('./archives', './archives_old', 14)
    
    big_files('C:/', 10)
    
    big_files_recursive('C:/', 10)

    big_files_generator('C:/', 10)

"""
In addition to those present, create as many suport functions needed
1. Exercise: Write function to print prettify list.
    fn name: prettify_list
    input: list
    output: None
    print:
        |- item1
        |- item2
        |- item3
        ...

2. Exercise: Write function to find files in ./archives older then 14 days. File name contains the write day in format 'YYYY-MM-DD' ("xxxx_guard_appl_x_d<date>.tar.gz.enc").
    fn name: older_files
    input: path <str>, days <int>
    output: list of files <list>

3. Exercise: Using previous functions print in a prettify way all files in ./archives older then 14 days.
    fn name: prettify_structure
    input: dictionary of files <dict>
    output: None
    print:
        folder1
            |- file1
            |- file2
            |- file3
        fodler2
            |- file1
            |- file2
            |- file3
        ...

4. Exercise: Write function to move files from ./archives older then 14 days to ./archives_old.
    fn name: move_files
    input: path_from <str>, path_to <str>, days <int>
    output: None

5. Exercise: Write function to find all files bigger then 10 MB in a path of your choice.
    fn name: big_files
    input: path <str>, size <int>
    output: list of files <list>

6. Exercise: Write the same function as above but using a recursive approach (compare both result and time execution). (https://realpython.com/python-recursion/)
    fn name: big_files_recursive
    input: path <str>, size <int>
    output: list of files <list>

7. Exercise: Write the same function as above but using a generator approach (compare both result and time execution). (https://wiki.python.org/moin/Generators)
    fn name: big_files_generator
    input: path <str>, size <int>
    output: generator of files <generator>
"""
