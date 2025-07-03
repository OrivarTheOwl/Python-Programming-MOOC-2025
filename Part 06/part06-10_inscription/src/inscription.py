name = input("Whom should I sign this to: ")
filename = input("Where shall I save it: ")

sentence = f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"

with open(filename, "w") as new_file:
    new_file.write(sentence)