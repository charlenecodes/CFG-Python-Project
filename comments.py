import requests

ingredient = input("Enter an ingredient you have: ")

app_id = "3299710b"
app_key = "274f2fe08f838701fe4481ed711e031c"
url = "https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}".format(ingredient, app_id,
                                                                                               app_key)


def recipe_search(ingredient):
    result = requests.get(url)

    data = result.json()  # converts it into a dictionary then you can print ## or pprint to make it nicer
    return data["hits"]  # everything falls under hits, which is used in the following function run()


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
        print()  # works the same as print("\n")

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

    # the whole chunk from allergy_list = [] creates a list from the user input, break stops the cycle
    # print(allergy_list) checks if it does what you need, unnecessary for the final code cuz you don't want that to show

    for allergy in allergy_list:
        url = url + "&excluded={}".format(allergy)
        # print(url) checks if it does what you need, unnecessary for the final code cuz you don't want that to show
        print()

    run()