#https://www.hackerrank.com/challenges/alphabet-rangoli/problem
import string
alphabet=string.ascii_lowercase[:]

def print_rangoli(size):
    new_string = alphabet[:size]
    for i in range(1, size+1):       
        line = new_string[:-i:-1]+new_string[-i:-1]+new_string[-1]
        nl = '-'.join(line).center(size*4-3, '-')       
        print nl

    for i in reversed(range(1, size)):
        line = new_string[:-i:-1]+new_string[-i:-1]+new_string[-1]
        nl = '-'.join(line).center(size*4-3, '-')       
        print nl


if __name__ == '__main__':