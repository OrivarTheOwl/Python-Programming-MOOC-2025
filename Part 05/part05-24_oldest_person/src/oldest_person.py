def oldest_person(people: list):
    oldest_name = people[0][0]
    oldest_age = people[0][1]
    for person in people:
        if person[1] < oldest_age:
            oldest_name = person[0]
            oldest_age = person[1]

    return oldest_name


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))