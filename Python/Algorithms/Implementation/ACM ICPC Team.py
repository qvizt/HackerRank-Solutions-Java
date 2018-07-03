# Solution for ACM ICPC Team


def max_topics_nr_teams(data):
    max_topics = 0
    nr_teams = 0

    for i in range(0, len(data) - 1):
        for k in range(i + 1, len(data)):
            topics = 0

            for n in range(len(data[i])):
                if data[i][n] == '1' or data[k][n] == '1':
                    topics += 1

            if topics > max_topics:
                max_topics = topics
                nr_teams = 1
            elif topics == max_topics:
                nr_teams += 1

    return max_topics, nr_teams


if __name__ == '__main__':
    attendees, topics = map(int, input().split())
    attendee_data = []

    for _ in range(attendees):
        binary_string = input()
        attendee_data.append(binary_string)

    result = max_topics_nr_teams(attendee_data)
    print(result[0])
    print(result[1])
