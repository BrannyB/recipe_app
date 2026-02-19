recipes = {
    "omelette": ["eggs", "milk", "cheese"],
    "PB&J": ["bread", "peanut butter", "jelly"],
    "toast": ["bread", "butter"],
    "mac and cheese": ["noodles", "cheese", "milk"],
    "salad": ["lettuce", "tomatoes", "cucumbers", "dressing"],
    "smoothie": ["fruit", "yogurt", "milk"],
    "pasta": ["noodles", "sauce", "cheese"],
    "grilled cheese": ["bread", "cheese", "butter"],
    "tacos": ["tortillas", "meat", "cheese", "lettuce", "salsa"],
    "pizza": ["dough", "sauce", "cheese"],
    "soup": ["broth", "vegetables", "meat"],
    "stir fry": ["vegetables", "meat", "sauce"],
    "curry": ["meat", "vegetables", "curry sauce"],
    "sandwich": ["bread", "meat", "cheese", "lettuce", "tomatoes"],
    "burrito": ["tortilla", "meat", "rice", "beans", "cheese", "salsa"],
    "pancakes": ["flour", "milk", "eggs", "syrup"],
    "waffles": ["flour", "milk", "eggs", "syrup"],
    "quiche": ["eggs", "milk", "cheese", "vegetables"],
    "frittata": ["eggs", "milk", "cheese", "vegetables"],
    "casserole": ["meat", "vegetables", "cheese", "sauce"],
    "lasagna": ["noodles", "meat", "sauce", "cheese"],
    "chili": ["meat", "beans", "tomatoes", "spices"],
}


user_ingredients: [str] = []

while True:
    print("1. Add an ingredient")
    print("2. View my ingredients")
    print("3. View all available recipes")
    print("4. Display recipes I can make")
    print("5. Exit")

    user_input: str = input("\n Choose an option: (1-5)")

    if user_input == "1":
        print("\nEnter ingredients one by one (type 'done' when finished):")

        while (item := input(">>> ").lower().strip()) != "done":
            if item and item not in user_ingredients:
                user_ingredients.append(item)
            elif item in user_ingredients:
                print(f"{item} is already in your ingredient list.")
            else:
                print("Please enter a valid ingredient or type 'done' to finish.")

    elif user_input == "2":
        print("\nMy Ingredients:")
        for ingredient in user_ingredients:
            print(f"- {ingredient}")

    elif user_input == "3":
        print("\nAvailable Recipes:")
        for recipe in recipes.keys():
            print(f"- {recipe}")

    elif user_input == "4":
        print("\nPossible Recipes with your ingredients:")
        for recipe, ingredients in recipes.items():
            if all(ingredient in user_ingredients for ingredient in ingredients):
                print(f"- {recipe}")

    elif user_input == "5":
        print("Goodbye!")
        break
