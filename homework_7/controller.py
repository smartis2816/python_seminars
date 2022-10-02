import input
import funcs_csv
import menu

def run():
    choice = input.choose_ext()
    if choice == 2:
        funcs_csv.csv_check()
        while (menu.menu_choice_csv(input.input_menu_csv())) != -1:
            continue
    else:
        while (menu.menu_choice_txt(input.input_menu_txt())) != -1:
            continue