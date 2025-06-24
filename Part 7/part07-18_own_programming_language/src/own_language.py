from string import ascii_lowercase, ascii_uppercase

def run(program: list):
    number_dict = {}
    numbers = []
    jump_locations = {}
    index = 0
    jump_index = 0

    for letter in ascii_uppercase:
        number_dict[letter] = 0

    for phrase in program:
        if " " not in phrase and phrase != "END":
            jump_locations[phrase.replace(":", "")] = jump_index
        jump_index += 1

    while index < len(program):
        command = program[index].split(" ")
        variable1 = ""
        variable2 = ""
        value = 0

        if command[0] == "PRINT":
            if command[1].isdigit():
                numbers.append(int(command[1]))
            else:
                numbers.append(number_dict[command[1]])

        elif command[0] == "MOV":
            variable1 = command[1]
            if command[2].isdigit():
                value = int(command[2])
            else:
                value = int(number_dict[command[2]])
            number_dict[variable1] = value
        
        elif command[0] == "ADD":
            variable1 = int((number_dict[command[1]]))
            if command[2].isdigit():
                value = int(command[2])
            else:
                value = int(number_dict[command[2]])
            variable1 += value
            number_dict[command[1]] = variable1

        elif command[0] == "SUB":
            variable1 = int((number_dict[command[1]]))
            if command[2].isdigit():
                value = int(command[2])
            else:
                value = int(number_dict[command[2]])
            variable1 -= value
            number_dict[command[1]] = variable1

        elif command[0] == "MUL":
            variable1 = int((number_dict[command[1]]))
            if command[2].isdigit():
                value = int(command[2])
            else:
                value = int(number_dict[command[2]])
            variable1 *= value
            number_dict[command[1]] = variable1

        elif command[0] == "JUMP":
            index = jump_locations[command[1]] - 1

        elif command[0] == "IF":
            condition = command[2]
            variable1 = int((number_dict[command[1]]))
            if command[3].isdigit():
                variable2 = int(command[3])
            else:
                variable2 = int((number_dict[command[3]]))

            if condition == "==":
                result = variable1 == variable2
            elif condition == "!=":
                result = variable1 != variable2
            elif condition == "<":
                result = variable1 < variable2
            elif condition == "<=":
                result = variable1 <= variable2
            elif condition == ">":
                result = variable1 > variable2
            elif condition == ">=":
                result = variable1 >= variable2

            if result:
                index = jump_locations[command[5]] - 1

        
        elif command[0] == "END":
            return numbers

        index += 1

    return numbers



if __name__ == "__main__":
    program = ['MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 'IF C == A JUMP virhe', 'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 'JUMP pass_by2', 'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 'ADD A 1', 'IF A <= N JUMP start']

    result = run(program)
    print(result)