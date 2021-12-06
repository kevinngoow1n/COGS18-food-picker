import random

def get_input():
    """Grabs the user's inputs.
    
    Parameters
    ----------
    N/A
    
    Returns
    -------
    msg : string
        String containing the message the user wants to send to the chatbot.
    
    """
    
    msg = input('\n🍔: ')
    
    return msg


def integer():
    """Asks the user for a numerical input.
    
    Parameters
    ----------
    N/A
    
    Returns
    -------
    number : int
        Inetger containing the number the user inputs.
    """
    
    input_value = True
    
    while input_value:
        check_int = get_input()
        try:
            number = int(round(float(check_int)))
            if number > 0 and number <= 10:
                input_value = False
                return number
            else:
                print("\n🍕: please input a number from 1 to 10")
        except:
            print("\n🍕: please input a number from 1 to 10")
            
            
def input_checker_no(category_list):
    """Checks to see if the input is within a list with a "no" option.
    
    Parameters
    ----------
    category_list : list
        A list with individual strings to be looked at.
        
    Returns
    -------
    i : string
        String found within category_list.
    "none" : string
        String containing the term "none"
    """
    
    checked = False
    deny = ["no", "none", "nope", "nada", "nah", "na"]
    
    while not checked:
        input_value = str(get_input().lower())
        for i in category_list:
            for j in deny:
                    if i in input_value:
                        checked = True
                        return i
                    elif j in input_value:
                        checked = True
                        return "skip"
        print("\n🍕: please select one of these options " + str(category_list) + " or none")

        
def input_checker(category_list):
    """Checks to see if the input is within a list.
    
    Parameters
    ----------
    category_list : list
        A list with individual strings to be looked at.
        
    Returns
    -------
    i : string
        String found within category_list.
    """
    
    checked = False
    
    while not checked:
        input_value = str(get_input().lower())
        for i in category_list:
                    if i in input_value:
                        checked = True
                        return i
        print("\n🍕: please select one of these options " + str(category_list))
        
        
def food_list(category_dict, input_str, prev_food):
    """Subsetting from a list.
    
    Parameters
    ----------
    category_dict : dictionary
        A dictionary with keys and values which will be selected based on keys.
    input_str : string
        The key to be used in the category_dict.
    prev_food : list
        A list of food created from a previous question.
        
    Returns
    -------
    new_food : list
        A list of food gathered from prev_food and filtered out of the dictionary.
    """
    
    new_food = []
    
    if input_str == "skip":
        new_food = prev_food
        return new_food
    else:
        for i in category_dict:
            if i in input_str:
                food_list = category_dict[i]
                for j in food_list:
                    if j in prev_food:
                        new_food.append(j)
                return new_food

        
def welcome():
    """Basic introduction, getting to know user.
    
    Parameters
    ----------
    N/A
    
    Returns
    -------
    name : string
        String with name of the user.
    """
    
    print("🍕: Huh? Oh, sorry, I was just eating this amazing dish "
    "from McDonald's called a McChicken 🐣! Have you ever had it "
    "before? It is truly amazing! I was planning to go get some more "
    "did you want some? Oh...you came to me to look for some food? "
    "Umm... I think I can help you with that. Ok, let's get started, "
    "answer a few questions and I can help pick something to eat for you!")
    print("\n🍕: First off, what is your name?")
    name = str(get_input().capitalize())
    return name


def boba():
    """Asks the user of they prefer food or boba.
    
    Parameters
    ----------
    N/A
    
    Returns
    -------
    online : bool
        True or False value depending on whether user picked boba or food.
    """
    
    print("\n🍕: Be honest, are you craving food or would boba satisfy the need?")
    boba_list = ["boba", "food"]
    boba_value = input_checker(boba_list)
    
    if 'boba' in boba_value:
        print("\n🍕: go get boba then lol 🧋")
        online = False
        return online
    elif 'food' in boba_value:
        print("\n🍕: ok, let's start ✅")
        online = True
        return online
    
    
def continent():
    """Asks user which continent they would like to go to and selects the food based off that selection.
    
    Parameters
    ----------
    N/A
    
    Returns
    -------
    continent_food : list
        A list of food from their selected continent input.
    """
    
    food = {"north_america_australia" : ["pizza", "hot dogs", "burgers", 
                                         "steak", "fried chicken", "pancakes", 
                                         "waffles", "eggs benedict", "barbecue", 
                                         "mac and cheese", "sandwiches", "clam chowder", 
                                         "salad", "french fries", "french toast", 
                                         "all american breakfast", "poutine", "corn dogs", 
                                         "cereal", "avocado toast", "wings"],
            "europe" : ["pasta", "calzone", "pizza", "crossiant", "fondue", "risotto", 
                        "gyros", "goulash", "pierogi", "pastries", "paella", 
                        "fish and chips"],
            "asia" : ["pad thai", "pho", "pad see ew", "chicken satay", "ramen", 
                      "fried rice", "chow mein", "dumplings", "katsu", "curry", "sushi", 
                      "teriyaki chicken", "bibimbap", "kimbap", "yakitori", "japanese bbq", 
                      "korean bbq", "chinese takeout", "dim sum", "hot pot", "biriyani", 
                      "butter chicken", "naan", "dosa", "poke", "spam musubi"],
            "south_america" : ["tacos", "burritos", "tortas", "mole", "empanadas", 
                               "tamales", "chimichanga", "enchiladas", "quesadillas", 
                               "tostadas", "nachos"],
            "africa" : ["chicken or beef stew", "fish or chicken curry", 
                        "suuqaar with rice/pasta", "sambusa", "nafaqa", "bajiya", 
                        "chapati", "fufu"]}
    print("\n🍕: If you could go to any continent in the world, "
          "where would you like to go to?")
    continent_list = ["north america", "australia", "europe", "asia", "south america", "africa"]
    continent_value = input_checker(continent_list)
    
    if "north america" in continent_value or "australia" in continent_value:
        key = "north_america_australia" 
        continent_food = food[key]
        return continent_food
    elif "europe" in continent_value:
        key = "europe"
        continent_food = food[key]
        return continent_food
    elif "asia" in continent_value:
        key = "asia"
        continent_food = food[key]
        return continent_food
    elif "south america" in continent_value:
        key = "south_america"
        continent_food = food[key]
        return continent_food
    elif "africa" in continent_value:
        key = "africa" 
        continent_food = food[key]
        return continent_food

    
def hungry(continent_food):
    """Asks users to rate how hungry they are on a scale of 1 to 10 with 1 being not hungry and 10 being extremely hungry.
    
    Parameters
    ----------
    continent_food : list
        List of food from a previous question that is to be further narrowed down.
        
    Returns
    -------
    hungry_food : list
        List of food subsetted off continent_food after user input of a number from 1 to 10.
    """
    
    print("\n🍕: On a scale of 1 to 10 with 1 being not hungry and 10 being ravaging, "
          "how hungry are you?")
    hungry_food = []
    high_hungry = ["pizza", "hot dogs", "burgers", "fried chicken", 
                   "sandwiches", "clam chowder", "salad", "french fries", 
                   "poutine", "corn dogs", "cereal", "avocado toast", 
                   "crossiant", "gyros", "pastries", "poke", "spam musubi", 
                   "fried rice", "chow mein", "dumplings", "kimbap", 
                   "chinese takeout", "naan", "dosa", "tacos", "burritos", 
                   "tortas", "mole", "empanadas", "tamales", "chimichanga", 
                   "enchiladas", "quesadillas", "tostadas", "nachos", 
                   "sambusa", "bajiya", "fufu", "pierogi"]
    hungry_value = integer()
    
    if hungry_value > 0 and hungry_value <= 5:
        hungry_food = continent_food
        return hungry_food 
    elif hungry_value > 5 and hungry_value < 11:
        for i in high_hungry:
            if i in continent_food:
                hungry_food.append(i) 
        return hungry_food 

    
def price(hungry_food):
    """Asks users to rate how much they would spend on their food on a scale of 1 to 10 with 1 being low and 10 being high.
    
    Parameters
    ----------
    hungry_food : list
        List of food from a previous question that is to be further narrowed down.
        
    Returns
    -------
    price_food : list
        List of food subsetted off hungry_food after user input of a number from 1 to 10.
    """
    
    print("\n🍕: On a scale of 1 to 10 with 1 being the lowest and "
          "10 being the highest, how much would you be willing to spend on your food today?")
    price_food = []
    low_price = ["pizza", "hot dogs", "burgers", "fried chicken”, “sandwiches", 
                 "salad", "french fries", "poutine", "corn dogs", 
                 "cereal", "crossiant", "gyros", "pastries", 
                 "poke", "spam musubi", "fried rice", "chow mein", "dumplings", 
                 "kimbap", "chinese takeout", "naan", "dosa", "tacos", "burritos", 
                 "tortas", "mole", "empanadas", "tamales", "chimichanga", 
                 "enchiladas", "quesadillas", "tostadas", "nachos", "sambusa", 
                 "bajiya", "fufu", "pierogi", "mac and cheese"]
    price_value = integer()
    
    if price_value > 0 and price_value <= 5:
        for i in low_price:
            if i in hungry_food:
                price_food.append(i)
        return price_food
    elif price_value > 5 and price_value < 11:
        price_food = hungry_food
        return price_food

    
def diet(price_food):
    """Asks the user if they are on any diet at the moment.
    
    Parameters
    ----------
    price_food : list
        List of food from a previous question that is to be further narrowed down.
        
    Returns
    -------
    diet_food : list
        List of food subsetted off price_food after user input of a diet or none.
    """
    
    print("\n🍕: Are you following any diets? If yes, which one? "
          "keto, paleo, vegetarian, vegan, mediterranean")
    diet_dict = {"keto" : ["clam chowder", "salad", "french fries", "poutine", "poke", 
                           "spam musubi", "dumplings", "kimbap", "mole", "empanadas", 
                           "tamales", "chimichanga", "enchiladas", "sambusa", 
                           "bajiya", "fufu", "pierogi", "mac and cheese", "steak", 
                           "pancakes", "waffles", "eggs benedict", "barbecue", 
                           "french toast", "all american breakfast", "wings", 
                           "fondue", "fish and chips", "chicken satay", "katsu", 
                           "curry", "sushi", "teriyaki chicken", "bibimbap", "yakitori", 
                           "japanese bbq", "korean bbq", "dim sum", "hot pot", 
                           "butter chicken", "chicken or beef stew", "fish or chicken curry"],
                 "paleo" : ["salad", "french fries", "poke", "dumplings", "kimbap", 
                            "mole", "fufu", "steak", "wings", "fish and chips", 
                            "chicken satay", "katsu", "curry", "sushi", "bibimbap", 
                            "yakitori", "japanese bbq", "korean bbq", "dim sum", 
                            "hot pot", "butter chicken", "chicken or beef stew", 
                            "fish or chicken curry"],
                 "vegetarian" : ["pizza", "sandwiches", "salad", "french fries", "poutine", 
                                 "cereal", "avocado toast", "crossiant", "pastries", "fried rice", 
                                 "chow mein", "dumplings", "kimbap",  "naan", "dosa", "burritos", 
                                 "tortas", "mole", "empanadas", "chimichanga", "enchiladas", 
                                 "quesadillas", "tostadas", "nachos", "sambusa", "bajiya", 
                                 "fufu", "pierogi", "mac and cheese", "pancakes", "waffles", 
                                 "eggs benedict", "french toast", "pasta", "calzone", "fondue", 
                                 "risotto", "pad thai", "pad see ew", "ramen", "curry", 
                                 "bibimbap", "hot pot", "biriyani"],
                 "vegan" : ["sandwiches", "salad", "french fries", "cereal", "avocado toast", 
                            "crossiant", "pastries", "kimbap",  "naan", "dosa", "mole", 
                            "tostadas", "sambusa", "bajiya", "fufu", "pierogi", "pasta", 
                            "risotto", "pad thai", "ramen", "curry", "bibimbap", "biriyani"],
                 "mediterranean" : ["salad", "french fries", "cereal", "poke", "spam musubi", 
                                    "dumplings", "kimbap", "mole", "bajiya", "fufu", 
                                    "eggs benedict", "wings", "goulash",  "fish and chips", 
                                    "chicken satay", "curry", "sushi", "bibimbap", "dim sum", 
                                    "hot pot", "biriyani", "butter chicken", "chicken or beef stew", 
                                    "fish or chicken curry", "suuqaar with rice/pasta"]}
    diet_list = list(diet_dict.keys())
    diet_value = input_checker_no(diet_list)
    diet_food = food_list(diet_dict, diet_value, price_food)
    return diet_food


def allergy(diet_food):
    """Asks the user if they have any food allergies.
    
    Parameters
    ----------
    diet_food : list
        List of food from a previous question that is to be further narrowed down.
        
    Returns
    -------
    allergy_food : list
        List of food subsetted off diet_food after user input of an allergy or none.
    """
    
    print("\n🍕: Do you have any food-related allergies? "
          "milk, eggs, nuts, soy, wheat, fish, shellfish")
    allergy_dict = {
        "milk" : ["hot dogs", "burgers", "fried chicken", "sandwiches", 
                  "salad", "french fries", "corn dogs", "cereal", 
                  "avocado toast", "crossiant", "gyros", "pastries", 
                  "poke", "spam musubi", "fried rice", "chow mein", 
                  "dumplings", "kimbap", "chinese takeout", "naan", 
                  "dosa", "tacos", "burritos", "tortas", "mole", 
                  "empanadas", "tostadas", "sambusa", "bajiya", "fufu", 
                  "pierogi”, “steak", "eggs benedict", "barbecue", 
                  "french toast", "all american breakfast", "wings", 
                  "pasta", "risotto", "goulash", "paella", "fish and chips", 
                  "pad thai", "pho", "pad see ew", "chicken satay", "ramen", 
                  "katsu", "curry", "sushi", "teriyaki chicken", "bibimbap", 
                  "yakitori", "japanese bbq", "korean bbq", "dim sum", 
                  "hot pot", "biriyani", "butter chicken", 
                  "chicken or beef stew", "fish or chicken curry",
                  "suuqaar with rice/pasta"],
        "egg" : ["pizza", "hot dogs", "burgers", "sandwiches", "clam chowder", 
                 "salad", "french fries", "poutine", "corn dogs", "cereal", 
                 "avocado toast", "crossiant", "gyros", "poke", "spam musubi", 
                 "fried rice", "dumplings", "kimbap", "chinese takeout", "naan", 
                 "dosa", "tacos", "burritos", "tortas", "mole", "empanadas", 
                 "tamales", "chimichanga", "enchiladas", "quesadillas", "tostadas", 
                 "nachos", "sambusa", "bajiya", "fufu", "pierogi", "mac and cheese", 
                 "steak", "barbecue", "french toast", "wings”, ”pasta", "calzone", 
                 "fondue", "risotto", "goulash", "paella", "fish and chips", "pho", 
                 "chicken satay", "ramen", "curry", "sushi", "teriyaki chicken", 
                 "bibimbap", "yakitori", "japanese bbq", "korean bbq", "dim sum", 
                 "hot pot", "biriyani", "butter chicken", "chicken or beef stew", 
                 "fish or chicken curry", "suuqaar with rice/pasta"],
        "nut" : ["pizza", "hot dogs", "burgers", "fried chicken”, “sandwiches", 
                 "clam chowder", "salad", "french fries", "poutine", "corn dogs", 
                 "cereal", "avocado toast", "crossiant", "gyros", "pastries", 
                 "poke", "spam musubi", "fried rice", "chow mein", "dumplings", 
                 "kimbap", "chinese takeout", "naan", "dosa", "tacos", 
                 "burritos", "tortas", "mole", "empanadas", "tamales", 
                 "chimichanga", "enchiladas", "quesadillas", "tostadas", 
                 "nachos", "sambusa", "fufu", "pierogi", "mac and cheese", 
                 "steak", "pancakes", "waffles", "eggs benedict", "barbecue", 
                 "french toast", "all american breakfast", "wings", "pasta", 
                 "calzone", "fondue", "risotto", "goulash", "paella", 
                 "fish and chips", "pho", "pad see ew", "ramen", "katsu", 
                 "curry", "sushi", "teriyaki chicken", "bibimbap", "yakitori", 
                 "japanese bbq", "korean bbq", "dim sum", "hot pot", "biriyani", 
                 "butter chicken", "chicken or beef stew", "fish or chicken curry", 
                 "suuqaar with rice/pasta"],
        "soy" : ["pizza", "hot dogs", "burgers", "fried chicken”, “sandwiches", 
                 "clam chowder", "salad", "french fries", "poutine", "corn dogs", 
                 "cereal", "avocado toast", "crossiant", "gyros", "pastries", 
                 "poke", "spam musubi", "fried rice", "chow mein", "dumplings", 
                 "kimbap", "chinese takeout", "naan", "dosa", "tacos", "burritos", 
                 "tortas", "mole", "empanadas", "tamales", "chimichanga", "enchiladas", 
                 "quesadillas", "tostadas", "nachos", "sambusa", "bajiya", "fufu", 
                 "pierogi", "mac and cheese", "steak", "pancakes", "waffles", 
                 "eggs benedict", "barbecue", "french toast", "all american breakfast", 
                 "wings”, ”pasta", "calzone", "fondue", "risotto", "goulash", "paella", 
                 "fish and chips", "pad thai", "pho", "pad see ew", "chicken satay", 
                 "ramen", "katsu", "curry", "sushi", "teriyaki chicken", "bibimbap", 
                 "yakitori", "japanese bbq", "korean bbq", "dim sum", "hot pot", 
                 "biriyani", "butter chicken", "chicken or beef stew", 
                 "fish or chicken curry", "suuqaar with rice/pasta"],
        "wheat" : ["fried chicken”, “sandwiches", "clam chowder", "salad", 
                   "french fries", "poutine", "corn dogs", "cereal", "avocado toast", 
                   "gyros", "pastries", "poke", "spam musubi", "fried rice", 
                   "chow mein", "dumplings", "kimbap", "chinese takeout", "tacos", 
                   "burritos", "mole", "tamales", "chimichanga", "enchiladas", 
                   "quesadillas", "tostadas", "nachos", "bajiya", "fufu", "pierogi", 
                   "mac and cheese”, “steak", "pancakes", "waffles", "eggs benedict", 
                   "barbecue", "french toast", "all american breakfast", "wings", 
                   "calzone", "fondue", "risotto", "goulash", "paella", "fish and chips", 
                   "pad thai", "pho", "pad see ew", "chicken satay", "ramen", "katsu", 
                   "curry", "sushi", "teriyaki chicken", "bibimbap", "yakitori", 
                   "japanese bbq", "korean bbq", "dim sum", "hot pot", "biriyani", 
                   "butter chicken", "chicken or beef stew", "fish or chicken curry", 
                   "suuqaar with rice/pasta"],
        "fish" : ["pizza", "hot dogs", "burgers", "fried chicken”, “sandwiches", 
                  "clam chowder", "salad", "french fries", "poutine", "corn dogs", 
                  "cereal", "avocado toast", "crossiant", "gyros", "pastries", "spam musubi",
                  "fried rice", "chow mein", "dumplings", "kimbap", "chinese takeout", 
                  "naan", "dosa", "tacos", "burritos", "tortas", "mole", "empanadas", 
                  "tamales", "chimichanga", "enchiladas", "quesadillas", "tostadas", 
                  "nachos", "sambusa", "bajiya", "fufu", "pierogi", "mac and cheese", 
                  "steak", "pancakes", "waffles", "eggs benedict", "barbecue", 
                  "french toast", "all american breakfast", "wings", "pasta", "calzone", 
                  "fondue", "risotto", "goulash", "pad thai", "pho", "pad see ew", 
                  "chicken satay", "ramen", "katsu", "curry", "sushi", 
                  "teriyaki chicken", "bibimbap", "yakitori", "japanese bbq", "korean bbq", 
                  "dim sum", "hot pot", "biriyani", "butter chicken", "chicken or beef stew", 
                  "suuqaar with rice/pasta"],
        "shellfish" : ["pizza", "hot dogs", "burgers", "fried chicken”, “sandwiches", 
                       "salad", "french fries", "poutine", "corn dogs", "cereal", 
                       "avocado toast", "crossiant", "gyros", "pastries", "poke", 
                       "spam musubi", "fried rice", "chow mein", "dumplings", 
                       "kimbap", "chinese takeout", "naan", "dosa", "tacos", 
                       "burritos", "tortas", "mole", "empanadas", "tamales", 
                       "chimichanga", "enchiladas", "quesadillas", "tostadas", 
                       "nachos", "sambusa", "bajiya", "fufu", "pierogi", 
                       "mac and cheese”, “steak", "pancakes", "waffles", 
                       "eggs benedict", "barbecue", "french toast", 
                       "all american breakfast", "wings”, ”pasta", "calzone", 
                       "fondue", "risotto", "goulash", "fish and chips", "pad thai", 
                       "pho", "pad see ew", "chicken satay", "ramen", "katsu", "curry", 
                       "sushi", "teriyaki chicken", "bibimbap", "yakitori", "japanese bbq", 
                       "korean bbq", "dim sum", "hot pot", "biriyani", "butter chicken", 
                       "chicken or beef stew", "fish or chicken curry", 
                       "suuqaar with rice/pasta"]}
    allergy_list = list(allergy_dict.keys())
    allergy_value = input_checker_no(allergy_list)
    allergy_food = food_list(allergy_dict, allergy_value, diet_food)
    return allergy_food


def spicy(allergy_food):
    """Asks the user what level of spice they prefer.
    
    Parameters
    ----------
    allergy_food : list
        List of food from a previous question that is to be further narrowed down.
        
    Returns
    -------
    spicy_food : list or string
        List of food subsetted off allergy_food after user input of levcel of spiciness or an empty string if list is empty.
    """
    
    print("\n🍕: How spicy are you? - sorry, I meant how spicy can you handle? "
          "mild, medium, spicy, nuclear")
    spicy_dict = {"mild" : ["pizza", "hot dogs", "burgers", "fried chicken", "sandwiches", 
                            "salad", "french fries", "poutine", "corn dogs", "avocado toast", 
                            "croissant", "gyros", "pastries", "poke", "spam musubi", 
                            "fried rice", "chow mein", "dumplings", "kimbap", 
                            "chinese takeout", "naan", "dosa", "tacos", "burritos", "tortas", 
                            "mole", "empanadas", "tamales", "chimichanga", "enchiladas", 
                            "quesadillas", "tostadas", "nachos", "sambusa", "bajiya", "fufu", 
                            "pierogi", "mac and cheese", "steak", "eggs benedict", "barbecue", 
                            "all american breakfast", "wings”, ”pasta", "calzone", "fondue", 
                            "risotto", "goulash", "paella", "fish and chips", "pad thai", "pho", 
                            "pad see ew", "chicken satay", "ramen", "katsu", "curry", "sushi", 
                            "teriyaki chicken", "bibimbap", "yakitori", "japanese bbq", 
                            "korean bbq", "dim sum", "hot pot", "biryani", "butter chicken", 
                            "chicken or beef stew", "fish or chicken curry", 
                            "suuqaar with rice/pasta"],
                  "medium" : ["pizza", "hot dogs", "burgers", "fried chicken", "sandwiches", 
                              "salad", "french fries", "poutine", "corn dogs", "avocado toast", 
                              "croissant", "gyros", "pastries", "poke", "spam musubi", 
                              "fried rice", "chow mein", "dumplings", "kimbap", 
                              "chinese takeout", "naan", "dosa", "tacos", "burritos", "tortas", 
                              "mole", "empanadas", "tamales", "chimichanga", "enchiladas", 
                              "quesadillas", "tostadas", "nachos", "sambusa", "bajiya", "fufu", 
                              "pierogi", "eggs benedict", "barbecue", "all american breakfast", 
                              "wings", "pasta", "calzone", "fondue", "risotto", "goulash", "paella", 
                              "fish and chips", "pad thai", "pho", "pad see ew", "chicken satay", 
                              "ramen", "katsu", "curry", "sushi", "teriyaki chicken", "bibimbap", 
                              "yakitori", "japanese bbq", "korean bbq", "dim sum", "hot pot", 
                              "biryani", "butter chicken", "chicken or beef stew", 
                              "fish or chicken curry", "suuqaar with rice/pasta"],
                  "spicy" : ["pizza", "hot dogs", "burgers", "fried chicken”, “sandwiches", 
                             "salad", "french fries", "poutine", "corn dogs", "cereal", 
                             "avocado toast", "croissant", "gyros", "poke", "spam musubi", 
                             "fried rice", "chow mein", "dumplings", "kimbap", "chinese takeout", 
                             "naan", "dosa", "tacos", "burritos", "tortas", "mole", "empanadas", 
                             "tamales", "chimichanga", "enchiladas", "quesadillas", "tostadas", 
                             "nachos", "sambusa", "bajiya", "fufu", "pierogi", "eggs benedict", 
                             "barbecue", "all american breakfast", "wings”, ”pasta", "calzone", 
                             "fondue", "risotto", "goulash", "paella", "fish and chips", 
                             "pad thai", "pho", "pad see ew", "chicken satay", "ramen", "katsu", 
                             "curry", "sushi", "teriyaki chicken", "bibimbap", "yakitori", 
                             "japanese bbq", "korean bbq", "dim sum", "hot pot", "biryani", 
                             "butter chicken", "chicken or beef stew", "fish or chicken curry", 
                             "suuqaar with rice/pasta"],
                  "nuclear" : ["hot dogs", "burgers", "fried chicken", "sandwiches", "corn dogs", 
                               "avocado toast", "croissant", "gyros", "poke", "spam musubi", 
                               "fried rice", "chow mein", "dumplings", "kimbap", "chinese takeout", 
                               "naan", "dosa", "tacos", "burritos", "tortas", "mole", "empanadas", 
                               "tamales", "chimichanga", "enchiladas", "quesadillas", "tostadas", 
                               "nachos", "sambusa", "bajiya", "fufu", "pierogi", "barbecue", 
                               "all american breakfast", "wings", "pasta", "calzone", "fondue", 
                               "risotto", "goulash", "paella", "fish and chips", "pad thai", "pho", 
                               "pad see ew", "chicken satay", "ramen", "katsu", "curry", 
                               "teriyaki chicken", "bibimbap", "yakitori", "japanese bbq", 
                               "korean bbq", "dim sum", "hot pot", "biryani", "butter chicken", 
                               "chicken or beef stew", "fish or chicken curry", 
                               "suuqaar with rice/pasta"]}
    spicy_list = list(spicy_dict.keys())
    spicy_value = input_checker(spicy_list)
    
    if len(allergy_food) == 0:
        spicy_food = ''
        return spicy_food
    else:
        spicy_food = food_list(spicy_dict, spicy_value, allergy_food)
        return spicy_food
    
    
def pick_food():
    """Randomly picks an item from the list.
      
    Parameters
    ----------
    N/A
        
    Returns
    -------
    diet_food : list
        List of food subsetted off price_food after user input of a diet or none
    """
    
    name = welcome()
    print("\n🍕: Hi "+ name + ", nice to meet you! 👋")

    online = boba()
    
    if not online:
        return
    else:
        continent_list = continent()
        print("\n🍕: amazing! 😁")
        
        hungry_list = hungry(continent_list)
        print("\n🍕: hmm...🤔 noted")

        price_list = price(hungry_list)
        print("\n🍕: honestly, right now, I'm in the same mood 💸")
            
        diet_list = diet(price_list)
        print("\n🍕: noted! 📝")
                
        allergy_list = allergy(diet_list)
        print("\n🍕: if you can't see it you can't be allergic to it right?? haha just kidding 😱")
            
        spicy_list = spicy(allergy_list)
        print("\n🍕: ooh ok I see you 🌶")

        if type(spicy_list) == list:
            print("\n🍕: hey " + name + " so after extensive research "
                  "and processing 🧑‍💻👩‍💻, we suggest that you get " + random.choice(spicy_list) + ".")
        else: 
            print("\n🍕: umm, you are too picky for our systems at the moment, maybe try water?? 🧊")