#https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    number = 0
    for i in string:
        iteration = 1
        if string.startswith(sub_string):
            number = number +1 
        string = string[iteration:]
        iteration = iteration+1            
    return (number)

if __name__ == '__main__':