"""
https://www.hackerrank.com/challenges/nested-list/problem
"""

if __name__ == '__main__':
    records = []
    list_of_scores = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        records.append([name, score])
    for l in records:
        list_of_scores.append(l[-1])
    
    list_of_scores = sorted(list_of_scores)
    
    set_of_scores = set(list_of_scores)
    list_of_scores = list(set_of_scores)

    lowest_score = list_of_scores[1]
    list_of_students = []
    for i in records:
        if i[-1] == lowest_score:
            list_of_students.append (i[0])
    for student in sorted(list_of_students):
        print (student)
