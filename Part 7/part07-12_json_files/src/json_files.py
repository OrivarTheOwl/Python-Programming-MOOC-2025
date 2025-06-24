import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
        
    people = json.loads(data)

    for person in people:
        print(f"{person['name']} {person['age']} years ({', '.join(person['hobbies'])})")


if __name__ == "__main__":
    print_persons("file1.json")