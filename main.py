import requests

ingredient = input("Enter an ingredient you have: ")

app_id = "3299710b"
app_key = "274f2fe08f838701fe4481ed711e031c"
url = "https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}".format(ingredient, app_id,
                                                                                               app_key)


def recipe_search(ingredient):
    result = requests.get(url)

    data = result.json()
    return data["hits"]


def run():
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'] + "\n")
        print("Ingredients:")
        ingredient_list = recipe["ingredientLines"]
        for text in sorted(ingredient_list):
            print("- " + text)

        print(recipe['url'])
        print()

allergic = input("Do you have any allergies? yes/no ")

if allergic == "no":
    run()

else:
    allergy_list = []

    while True:
        allergic_to = input("What are you allergic to? ")
        allergy_list.append(allergic_to)

        more_allergies = input("Do you have more allergies? (yes/no) ")
        if more_allergies == "no":
            break

    # print(allergy_list)

    for allergy in allergy_list:
        url = url + "&excluded={}".format(allergy)
        # print(url)
        print()

    run()