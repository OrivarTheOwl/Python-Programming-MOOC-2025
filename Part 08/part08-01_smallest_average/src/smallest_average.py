def smallest_average(person1: dict, person2: dict, person3: dict):
    
    smallest_result_sum = 100
    smallest_person = {}
    people = (person1, person2, person3)

    for person in people:
        person_sum = person["result1"] + person["result2"] + person["result3"]
        if person_sum < smallest_result_sum:
            smallest_result_sum = person_sum
            smallest_person = person

    return smallest_person
    


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))