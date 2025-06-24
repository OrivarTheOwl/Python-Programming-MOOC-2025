def conversion(filename):
    recipes = {}
    all_recipes_list = []
    num_of_recipes = 1

    with open (filename) as new_file:
        for line in new_file:
            line = line.strip()
            all_recipes_list.append(line)

    for word in all_recipes_list:
        if word == "":
            num_of_recipes += 1

    while num_of_recipes > 0:
        index = 0
        name = all_recipes_list[0]
        recipes[name] = []

        for word in all_recipes_list[1:]:
            if word == "":
                index += 2
                all_recipes_list = all_recipes_list[index:]
                break
            recipes[name].append(word)
            index += 1

        num_of_recipes -= 1
    return recipes



def search_by_name(filename: str, search_term:str):
    recipes = conversion(filename)

    search_hits = []

    for key in recipes:
        if search_term.lower() in key.lower():
            search_hits.append(key)
    
    return search_hits



def search_by_time(filename: str, prep_time: int):
    recipes = conversion(filename)

    search_hits = []

    for key in recipes:
        if int(recipes[key][0]) <= prep_time:
            search_hits.append(f"{key}, preparation time {int(recipes[key][0])} min")
    
    return search_hits
    



def search_by_ingredient(filename: str, ingredient: str):
    recipes = conversion(filename)

    has_ingredient = []
    search_hits = []

    for key in recipes:
        for value in recipes[key]:
            if ingredient in value:
                has_ingredient.append(key)

    for key in has_ingredient:
        search_hits.append(f"{key}, preparation time {int(recipes[key][0])} min")
    
    return search_hits



if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)