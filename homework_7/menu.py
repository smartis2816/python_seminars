import input
import funcs_csv as f_csv
import funcs_txt as f_txt

def menu_choice_csv(input_menu):
    choice = input_menu
    match choice:
        case '1':
            return f_csv.add_contact(input.input_contact())
        case '2':
            return f_csv.find_contact(input.name_contact())
        case '3':
            return f_csv.delete_contact(input.name_contact())
        case '4':
            return f_csv.find_all()
        case '5':
            return -1

def menu_choice_txt(input_menu):
    choice = input_menu
    match choice:
        case '1':
            return f_txt.add_contact(input.input_contact())
        case '2':
            return f_txt.find_contact(input.name_contact())
        case '3':
            return f_txt.find_all()
        case '4':
            return -1


