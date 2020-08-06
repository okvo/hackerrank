"""
https://www.hackerrank.com/challenges/python-mutations/problem
"""
def mutate_string(string, position, character):
    string_list = []
    for i in string:
        string_list.append(i)
    string_list[position] = character
    string_list = ''.join(string_list)    
    return string_list

if __name__ == '__main__':