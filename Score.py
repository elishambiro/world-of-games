def points_of_winning(difficulty):
    points = (difficulty * 3) + 5
    return points


def add_score(name, points):
    a_dictionary = {}
    a_file = open('templates/scores.txt', 'r')
    for line in a_file:
        key, value = line.split()
        a_dictionary[key] = int(value)
    if name in a_dictionary:
        a_dictionary[name] += points
    else:
        a_dictionary[name] = points
    a_file.close()

    a_file = open('templates/scores.txt', 'w')
    a_file.write("")
    a_file.close()

    a_dictionary = dict(sorted(a_dictionary.items(), key=lambda item: item[1], reverse=True))
    a_file = open('templates/scores.txt', 'a')
    for key, value in a_dictionary.items():
        add = key, str(value)
        add = " ".join(add)
        a_file.write(add)
        a_file.write("\n")

