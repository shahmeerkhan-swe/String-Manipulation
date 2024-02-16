# Khan_Shahmeer - CA06
# String manipulation in Python

# ass-06 actors.py

def create_actor():
    actor_list = ["andrei stephens",
                  "harry venables",
                  "phillipa blythe",
                  "yuan spield",
                  "sadiq elbahi",
                  "stephanie wynne",
                  "zeng ergan"]
    return (actor_list)


def actor_string(actor_list):
    actor_list_to_string = ', '.join(actor_list)
    return actor_list_to_string


def string_split(joined_string):
    name_string = joined_string.split()
    print(name_string)
    return name_string


def given_name_list(name_list):
    given_name = name_list[::2]
    print(given_name)
    return given_name


def family_name_list(name_list):
    family_name = name_list[1::2]
    print(family_name)
    return family_name


def family_3_char_list(family_char_list):
    global new_list
    new_list = []

    for i in family_char_list:
        new_list.append(i[:3])
    print(new_list)
    return new_list


def given_2_char_list(given_char_list):
    global new_list_2
    new_list_2 = []

    for i in given_char_list:
        new_list_2.append(i[:2])
    print(new_list_2)
    return new_list_2


def alien_list(alien_n_given, alien_n_family):
    alien_name_list = []

    for i in range(0,7):
        alien_first = alien_n_given[i]
        alien_last = alien_n_family[i]
        alien_name = alien_last + alien_first

        alien_name_list.append(alien_name)
    print(alien_name_list)

    return alien_name_list


def main():
    list_of_actors = create_actor()
    print("Actor names as one string: ")
    print(actor_string(list_of_actors))

    print("\nActor names as separate strings:")
    joined_string = actor_string(list_of_actors)
    name_list = string_split(joined_string)

    print("\nThe list of given names: ")
    given_char_list = given_name_list(name_list)

    print("\nThe list of family names: ")
    family_char_list = family_name_list(name_list)

    print("\n3 char list: ")
    alien_n_family = family_3_char_list(family_char_list)

    print("\n 2 char list: ")
    alien_n_given = given_2_char_list(given_char_list)

    print("\nList of alien names: ")
    new_list_3 = alien_list(alien_n_given, alien_n_family)


main()

