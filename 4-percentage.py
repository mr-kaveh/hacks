#!/usr/bin/env python
'''
    Calculates The Average
    Of Scores, correct to
    two decimal places
'''
if __name__ == '__main__':
    n = int(input())
    sum = 0.00
    student_marks, output = {}, {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        student_marks[name] = scores
        for i in range(len(scores)):
            sum = sum + float(scores[i])
        output[name] = sum / len(scores)
        sum = 0.00
    query_name = input()
    print('%.2f' % output[query_name])

