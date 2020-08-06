"""
https://www.hackerrank.com/challenges/python-lists/problem
"""

if __name__ == '__main__':
    my_list = []
    N = int(raw_input())
    for i in range (1, N+1):
        command  = raw_input()
        if command.startswith('append'):
            command = command.split()
            my_list.append(int(command[-1]))
        elif command.startswith('insert'):
            command = command.split()
            my_list.insert(int(command[-2]), int(command[-1]));
        elif command == 'reverse':
            my_list.reverse()
        elif command.startswith('remove'):
            my_list.remove(int(command[-1]))
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            my_list.pop(-1)
        else:    #print
            print (my_list)
