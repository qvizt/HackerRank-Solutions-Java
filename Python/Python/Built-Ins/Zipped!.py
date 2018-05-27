# Solution for Zipped!

if __name__ == '__main__':
    n, x = map(int, input().split())

    subject_scores = [list(map(float, input().split())) for i in range(x)]
    student_scores = zip(*subject_scores)
    for s in student_scores:
        print(sum(s) / len(s))
