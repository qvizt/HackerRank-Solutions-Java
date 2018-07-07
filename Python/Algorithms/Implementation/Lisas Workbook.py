# Solution for Lisas Workbook


def count_special_problems(workbook, problems_per_page):
    count = 0
    page = 1

    for problems_per_chapter in workbook:
        # pages contains the information how many pages are required
        # for the current chapter. The sum of pages[0] and pages[1]
        # is the required amount of pages for a chapter.
        pages = divmod(problems_per_chapter, problems_per_page)

        start_problem_on_page = 1
        for i in range(pages[0]):
            if page in range(start_problem_on_page, start_problem_on_page + problems_per_page):
                count += 1
            page += 1
            start_problem_on_page += problems_per_page

        if pages[1]:
            if page in range(start_problem_on_page, start_problem_on_page + pages[1]):
                count += 1
            page += 1

    return count


def count_special_problems_v2(workbook, problems_per_page):
    count = 0
    page = 1

    for problems_per_chapter in workbook:
        start_problem_on_page = 1
        while problems_per_chapter > 0:
            problems_on_page = min(problems_per_page, problems_per_chapter)
            if page in range(start_problem_on_page, start_problem_on_page + problems_on_page):
                count += 1
            page += 1
            problems_per_chapter -= problems_on_page
            start_problem_on_page += problems_per_page

    return count


if __name__ == '__main__':
    chapters, problems_per_page = map(int, input().split())
    workbook = list(map(int, input().split()))

    result = count_special_problems(workbook, problems_per_page)
    print(result)
