from helper.Enum_messages import EXIT_COMMAND
from kernel.settings import *
import json
 
# EXIT_COMMAND = ["exit", "q", "quit"]

# define three of my_list
sport_equipments_list = list()
vegetable_list = list()
drink_list = list()

# functions

EXITS = [EXIT_COMMAND.q.value, EXIT_COMMAND.quit.value, EXIT_COMMAND.exit.value]

def add_category(category_list, items):
    category_list.append(items)
    sum_ = 0
    for items in category_list:
        category_list.count(items)
        sum_ += 1
    print(f"total number list is : {sum_} , your  list is : {category_list}")


def remove_category_items(category_list, items):

    if items not in category_list:
        print('item does not exist')
    else:
        category_list.remove(items)
        print(f"{ items} deleted  successfully.")


def search_category(category_list, items):
    if items in category_list:
        print(f" item you searched is : { items}")
    else:
        print('this item does not exist into the sport_equipments list')


def show_lists(category_list):
    for item in category_list:
        print("-" * 20)
        print(item)



def show_all_lists(vegetable_list, drink_list, sport_equipments_list):
    print(f"vegetable list is : {sport_equipments_list} \n  drink list is : {vegetable_list} \n  list sport_equipments is : {drink_list}")


def show_help():
    print('enter  "Q" to exit . ')
    print('enter "search" to search into the lists .')


# loop
while True:
    username = input("please input username :")
    password = input("please input password :")
    try: 
        if len(password) < 8:
            raise ValueError("your password is too short")  
        with open("file.json", "r") as my_file:
            profile = {username : password}
            json.dump(profile, my_file, indent=3)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
        auth_logger.warning(f"{e}")

    question = input('What kind of products do you need? ? ( drink, sport_equipments, vegetable ):').casefold()
    auth_logger.debug(f'{username} choose {question}')

    if question in EXITS:
        show_all_lists(vegetable_list, drink_list, sport_equipments_list)
        break

    elif question == "help":
        show_help()
    
    elif question == 'sport_equipments':
        items = input('please enter your sport_equipments items: ')
        if items in sport_equipments_list:
            print('item is exist into the list .')
        else:
            add_category(sport_equipments_list, items)
        remove_items = input('Do you want delete any item from sport_equipments list ?( yes / no )')

        if remove_items == 'yes':
            remove_question = input('which item do you want to remove ?')
            remove_category_items(sport_equipments_list, remove_question)
            root_logger.debug(f'{username} remove his item {question}')
        else:
            continue

    elif question == 'vegetable':
        items = input('please enter your vegetable items: ')
        if items in vegetable_list:
            print('item is exist into the list .')

        else:
            add_category(vegetable_list, items)
        remove_items = input('Do you want delete any item from vegetable list ?( yes / no )')
        if remove_items == 'yes':
            remove_question = input('which item do you want to remove ?')
            remove_category_items(vegetable_list, remove_question)
            root_logger.debug(f'{username} remove his item {question}')

        else:
            continue

    elif question == 'drink':
        items = input('please enter your drink items: ')
        if items in drink_list:
            print('item is exist into the list .')

        else:
            add_category(drink_list, items)
        remove_items = input('Do you want delete any item from drink list ?( yes / no )')

        if remove_items == 'yes':
            remove_question = input('which item do you want to remove ?')
            remove_category_items(drink_list, remove_question)
            root_logger.debug(f'{username} remove his item {question}')
            
        else:
            continue
    elif question == 'show list':
        question = input('which category do you want to see ?( all / vegetables / drink / sport_equipments)')

        if question == 'sport_equipments':
            show_lists(sport_equipments_list)

        elif question == 'vegetable':
            show_lists(vegetable_list)

        elif question == 'drink':
            show_lists(drink_list)

        elif question == 'all':
            show_all_lists(vegetable_list, drink_list, sport_equipments_list)
            

    elif question == 'edit':
        edit_question = input('which category do you want to edit ? ')

        if edit_question == 'drink':
            item_to_edit = input('enter which item do you want edit with it ?')
            remove_category_items(drink_list, item_to_edit)
            item_to_edit_with = input('enter which item do you want edit it with?')
            add_category(drink_list, item_to_edit_with)

        elif edit_question == 'vegetable':
            item_to_edit = input('enter which item do you want edit with it ?')
            remove_category_items(vegetable_list, item_to_edit)
            item_to_edit_with = input('enter which item do you want edit  it with?')
            add_category(vegetable_list, item_to_edit_with)

        elif edit_question == 'sport_equipments':
            item_to_edit = input('enter which item do you want edit with it ?')
            remove_category_items(sport_equipments_list, item_to_edit)
            item_to_edit_with = input('enter which item do you want edit  it with?')
            add_category(sport_equipments_list, item_to_edit_with)

    elif question == 'search':
        search_question = input('which category do you want to search ?')
        if search_question == 'sport_equipments':
            search_item = input('please enter your intended item :')
            search_category(sport_equipments_list, search_item)

        elif search_question == 'vegetable':
            search_item = input('please enter your intended item:')
            search_category(vegetable_list, search_item)

        elif search_question == 'drink':
            search_item = input('please enter your intended item :')
            search_category(drink_list, search_item)
