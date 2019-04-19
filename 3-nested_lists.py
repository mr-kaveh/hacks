#!/usr/bin/env python3.6
'''
    Finding The Second Minimum
    in a Two-dimensional List
'''
if __name__ == '__main__':
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    #students = sorted(students, key=lambda x: x[1])
    set_students = set([students[i][1] for i in range(len(students))])
    sorted_scores = list(sorted(set_students))
    score_sec_min = sorted_scores[1]
    output = [students[i][0] for i in range(len(students)) if students[i][1] == score_sec_min]
    print('\n'.join(sorted(output)))
