# Load file
from collections import defaultdict
from typing import List

in_file = open("data/day_21_input.txt", "r")
content = in_file.read()
foods = content.split("\n")
in_file.close()

def find_safe_ingredients(input_txt: List) -> int:
    allergen_ingredients = {}
    ingredient_counter = defaultdict(int)
    for line in input_txt:
        ingredients, allergens = line.split('(contains ')
        ingredients = set(ingredients.split())
        allergens = allergens.replace(')', '').split(' ')
        for allergen in allergens:
            if allergen in allergen_ingredients:
                allergen_ingredients[allergen].intersection_update(ingredients)
            else:
                allergen_ingredients[allergen] = ingredients.copy()
        for ingredient in ingredients:
            ingredient_counter[ingredient] += 1

    without_allergens = set(ingredient_counter.keys())
    for v in allergen_ingredients.values():
        for allergen in v:
            without_allergens.discard(allergen)

    allergen_candidates = set()
    for v in allergen_ingredients.values():
        allergen_candidates.update(v)

    sum_ingre = sum(ingredient_counter[ingredient] for ingredient in without_allergens)
    return sum_ingre, allergen_ingredients
	
def find_dangerous(allergen_ingredients: List) -> str:
    """Find true dangerous ingredients."""
    finished = False
    done = set()
    while not finished:
        finished = True
        for allergen, ingredients in allergen_ingredients.items():
            if len(ingredients) == 1:
                # Get only element of set without removing it.
                ingredient = next(iter(ingredients))
                if ingredient not in done:
                    done.add(ingredient)
                    for a, i in allergen_ingredients.items():
                        if a != allergen:
                            i.discard(ingredient)
            else:
                finished = False
    result = [(k, *v) for k, v in allergen_ingredients.items()]
    result.sort(key=lambda x: x[0])
    return ",".join(x[1] for x in result)