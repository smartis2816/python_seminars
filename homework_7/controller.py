import input
import database
import formats

def run():
    choice = formats.choose_ext()
    if choice == 2:
        database.csv_check()
        database.add_info_csv(input.input_data())
    else:
        database.add_info_txt(input.input_data())