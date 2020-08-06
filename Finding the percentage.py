"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] 
for a list of students. Print the average of the marks array for the student name provided, 
showing 2 places after the decimal.
"""
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    a = (sum(student_marks[query_name])/3)
    print (format(a, '.2f'))
