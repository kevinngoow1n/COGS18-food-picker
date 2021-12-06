from functions import get_input, integer, food_list, pick_food
import random

def test_get_input():
    """test for the get_input function
    some code sourced from https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call"""
    
    # Test to see if function can be called
    assert callable(get_input)

    
    # Test to see if there is an input
    class Test_Get_Input():
        
        def get_input_name():
            functions.input = lambda: "Ken"
            output == functions.get_input()
            assert output == 'Ken'
    
    
def test_integer():
    """test for the integer function
    some code sourced from https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call"""
    
    # Test to see if function can be called
    assert callable(integer)
    
    # Test to see if there is an input
    class Test_Integer():
        
        def get_integer_name():
            functions.input = lambda: "7"
            output == functions.get_input()
            assert output == '7'
    
    
def test_food_list():
    """test for the food_list function"""
    category_dict = {"keto" : ["clam chowder", "salad", "french fries", "poutine", "poke", 
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
    prev_food = ["pad thai", "pho", "pad see ew", "chicken satay", "ramen", 
                      "fried rice", "chow mein", "dumplings", "katsu", "curry", "sushi", 
                      "teriyaki chicken", "bibimbap", "kimbap", "yakitori", "japanese bbq", 
                      "korean bbq", "chinese takeout", "dim sum", "hot pot", "biriyani", 
                      "butter chicken", "naan", "dosa", "poke", "spam musubi"]
    
    # Test to see if function can be called
    assert callable(food_list)
    
    # Test to see if a list is returned
    assert type(food_list(category_dict, "keto", prev_food)) == list
    
    # Test to see if the correct list is returned
    assert food_list(category_dict, "keto", prev_food) == ['poke', 'spam musubi',
                                                           'dumplings', 'kimbap', 'chicken satay', 'katsu', 'curry',
                                                           'sushi', 'teriyaki chicken', 'bibimbap', 'yakitori',
                                                           'japanese bbq', 'korean bbq', 'dim sum', 'hot pot',
                                                           'butter chicken']
    # Test to see if the correct list is returned
    assert food_list(category_dict, "skip", prev_food) == prev_food
   
    
def test_pick_food():
    """test for the pick_food function"""
    
    # Test to see if function can be called
    assert callable(pick_food)
    
    
def combine_all_functions():
    """add all of the functions together to run them"""
    
    test_get_input()
    test_integer()
    test_food_list()
    test_pick_food()