def create_tuple(x: int, y: int, z: int):
    smallest = min(x, y, z)
    biggest = max(x, y, z)
    summed = (x + y + z)
    
    sorted_tuple = (smallest, biggest, summed)

    return sorted_tuple




if __name__ == "__main__":
    print(create_tuple(5, 3, -1))