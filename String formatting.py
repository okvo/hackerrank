#https://www.hackerrank.com/challenges/python-string-formatting/problem
def print_formatted(number):
    # your code goes here
    n_width = int(len(bin(n)[2:]))
    for i in range(1, n+1):
        print '{:>{w}}'.format(i, w = n_width), '{:>{w}}'.format(oct(i)[1:], w = n_width), '{:>{w}}'.format(hex(i)[2:].upper(), w = n_width), '{:>{w}}'.format(bin(i)[2:], w = n_width)

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)