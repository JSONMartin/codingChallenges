def groupingDishes(dishes):
    ingredients = {}
    for dish in dishes:
        for ingredient in dish[1:]:
            ingredients[ingredient] = ingredients[ingredient] + [dish[0]] if ingredient in ingredients else [dish[0]]

    results = sorted([[ingredient] + sorted(ingredients[ingredient]) for ingredient in ingredients if len(ingredients[ingredient]) >= 2])
    return results


""" TESTS """
dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
          ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
          ["Quesadilla", "Chicken", "Cheese", "Sauce"],
          ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

res = groupingDishes(dishes)  # => [["Cheese", "Quesadilla", "Sandwich"], ["Salad", "Salad", "Sandwich"], ["Sauce", "Pizza", "Quesadilla", "Salad"], ["Tomato", "Pizza", "Salad", "Sandwich"]]
# print(res)
