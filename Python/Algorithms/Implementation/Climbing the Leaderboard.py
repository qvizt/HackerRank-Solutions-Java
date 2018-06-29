# Solution for Climbing the Leaderboard
import bisect


def rankings(alice_scores, scores):
    result = []
    scores = set(scores)
    scores = list(scores)
    scores.sort()
    current_index = 0
    current_rank = len(scores)

    for a in alice_scores:
        if scores and not a >= scores[len(scores) - 1]:
            if a < scores[0]:
                result.append(len(scores) + 1)
            else:
                for i in range(current_index, len(scores) - 1):
                    score = scores[i]
                    if score <= a < scores[i + 1]:
                        result.append(current_rank)
                        current_index = i
                        break
                    else:
                        current_rank -= 1
        else:
            result.append(1)

    return result


if __name__ == '__main__':
    input()  # n not required
    scores = list(map(int, input().split()))

    input()  # m not required
    alice = list(map(int, input().split()))

    rankings = rankings(alice, scores)

    for rank in rankings:
        print(rank)
