# Solution for Breaking the Records

def get_min_max_records_change(scores):
    """Computes how often a score changes the record for min and max points. The
    result is returned as tuple in the form (min points changes, max points changes)."""
    min_changes = 0
    max_changes = 0
    min_score = scores[0]
    max_score = scores[0]

    for i in range(1, len(scores)):
        score = scores[i]

        if score < min_score:
            min_changes += 1
            min_score = score
        elif score > max_score:
            max_changes += 1
            max_score = score

    return min_changes, max_changes


if __name__ == '__main__':
    input()  # number of games not required
    scores = list(map(int, input().split()))

    min_changes, max_changes = get_min_max_records_change(scores)

    print(max_changes, min_changes)
