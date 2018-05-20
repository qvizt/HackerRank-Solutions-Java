# Solution for Nested Lists


if __name__ == '__main__':

    student_grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grades.append([name, score])

    student_grades.sort(key=lambda x: (x[1], x[0]))

    lowest_grade = student_grades[0][1]
    second_lowest_grade = None

    for i in range(1, len(student_grades)):
        current = student_grades[i]
        if second_lowest_grade:
            if current[1] == second_lowest_grade:
                print(current[0])
            else:
                break
        elif current[1] > lowest_grade:
            second_lowest_grade = current[1]
            print(current[0])
