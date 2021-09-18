import os
import subprocess


# USING OS & (unix based) COMM modules
os.system("bash -c 'echo COMMON:'")
os.system("bash -c 'comm -12 <(sort resources/file1.txt) <(sort resources/file2.txt)'")
os.system("bash -c 'echo FILE1 - FILE2:'")
os.system("bash -c 'comm -23 <(sort resources/file1.txt) <(sort resources/file2.txt)'")
os.system("bash -c 'echo FILE2 - FILE1:'")
os.system("bash -c 'comm -13 <(sort resources/file1.txt) <(sort resources/file2.txt)'")


# USING SUBPROCESS & (unix based) COMM modules
subprocess.call(['bash', '-c',
                 'comm -12 <(sort "$1") <(sort "$2") >"$3"', '_',
                 'resources/file1.txt', 'resources/file2.txt', 'resources/common.txt'])

subprocess.call(['bash', '-c',
                 'comm -23 <(sort "$1") <(sort "$2") >"$3"', '_',
                 'resources/file1.txt', 'resources/file2.txt', 'resources/file1_file2.txt'])

subprocess.call(['bash', '-c',
                 'comm -13 <(sort "$1") <(sort "$2") >"$3"', '_',
                 'resources/file1.txt', 'resources/file2.txt', 'resources/file2_file1.txt'])


# Pure Python Implementations
def diff(file1, file2):
    """
    Compares two file and prints common lines, file1 - file2 and file2 - file1
    :param file1:
    :param file2:
    :return:
    """
    with open(file1) as f1, open(file2) as f2:
        lines1 = set(map(str.rstrip, f1))
        lines2 = set(map(str.rstrip, f2))
        print('COMMON:', lines1.intersection(lines2))
        print('F1-F2:', lines1.difference(lines2))
        print('F2-F1:', lines2.difference(lines1))


f1 = 'resources/file1.txt'
f2 = 'resources/file2.txt'
diff(f1, f2)
