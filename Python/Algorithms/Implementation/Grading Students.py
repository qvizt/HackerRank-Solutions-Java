# Solution for Grading Students

def get_final_grade(grade):
    if grade > 37:
        remainder = grade % 5
        if remainder > 2:
            grade = grade + 5 - remainder

    return grade


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        grade = int(input())
        grade = get_final_grade(grade)
        print(grade)
