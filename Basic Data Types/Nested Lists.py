if __name__ == '__main__':
    student_list = list()
    scores = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        student_list.append([name, score])

    m = min(scores)
    scores = list(filter(lambda x: x != m, scores))
    m = min(scores)
    result = list()
    for l in student_list:
        if l[1] == m:
            result.append(l[0])
    result.sort()

    for l in result:
        print(l)
