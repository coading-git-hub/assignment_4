def mad_libs():
    print("Let\'s play Mad libs! fill in the blanks with your own words.")

    name = input("Give me a name: ")
    place = input("Give me a place: ")
    funny_obj = input("Give me a funny words: ")
    random_obj =input("Give me a random object: ")
    animal =input("Give me an animal name: ")
    action_verb = input("Give me an action verb: ")
    funny_exclamation = input("Give me a funny exclamation: ")

    story = f'''
    Once upon a time, ther was a person name {name} who lived in {place}. 
    One day, the foung a {funny_obj} {random_obj} that belong to to a {animal}.
    The {animal} was very upset and started to {action_verb} around.
    {name} could'nt help butblaugh and shouted "{funny_exclamation}!". '''

    print("\nHere is your Mad libs story: ")
    print (story)

if __name__ == "__main__":
    mad_libs()    
      