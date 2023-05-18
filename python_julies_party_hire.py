#__________python3 term_two_asessment/julies_party_hire.py_________

import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox
root = tk.Tk()
# need to set boundry for user input

root.mainloop()
def append_details_one():
    all_user_info_list = []
    try:
        c_full_nme = str(cfn_user_entry.get())
    except ValueError:
        customer_full_name["text"] = f"Enter your name as a word"
        return 0
    try:
        c_r_number = int(r_n_entry.get())
    except ValueError:
        recipt_number["text"] = f"Enter a number"
        return 0
    try:
        c_item_hired = str(ih_user_entry.get())
    except ValueError:
        item_hired["text"] = f"Enter the name of item hired"
        return 0
    try:
        c_number_of_items_hired = int(n_o_i_hired.get())
    except ValueError:
        num_of_item_hired["text"] = f"Enter a number of items you want to hire"
        return 0
    if c_number_of_items_hired > 1 and c_number_of_items_hired < 500:
        #
        all_user_info_list.append(c_full_nme)
        all_user_info_list.append(c_r_number)
        all_user_info_list.append(c_item_hired)
        all_user_info_list.append(c_number_of_items_hired)
    else:
        num_of_item_hired["text"] = f"Number has to be between 1 and 500"
    print(all_user_info_list)
    user_info_r_one["text"] = f" {all_user_info_list[0]}: Reciept N.{all_user_info_list[1]} Equiptment:({all_user_info_list[2]} x{all_user_info_list[3]})"
    user_info_r_one.grid(row=7, column=1)
    delete_user_input_row_one.grid(row=7, column=0)

def clear_all_u_info():
    cfn_user_entry.delete(0, 'end')
    r_n_entry.delete(0, 'end')
    ih_user_entry.delete(0, 'end')
    n_o_i_hired.delete(0, 'end')



def d_lete_r_one():
    user_info_r_one.after(100, user_info_r_one.destroy())
    delete_user_input_row_one.after(100, delete_user_input_row_one.destroy())


clear_all = ttk.Button(root, text="Clear All", command=clear_all_u_info)

j_p_h_title = tk.Label(root, text="Julies Party Hire")
j_p_h_title.config(font="Times 20")


ent_dtail = tk.Label(root, text="Enter the following details:")

below_ent_dtail = tk.Label(root, text="")

customer_full_name = tk.Label(root, text="Customer full name:")
cfn_user_entry = ttk.Entry(root, width=30)

#empty label:
below_cfn_entry = tk.Label(root, text="")

recipt_number = tk.Label(root, text="Recipt number:")
r_n_entry = ttk.Entry(root, width=20)

item_hired = tk.Label(root, text="The item you hired:")
ih_user_entry = ttk.Entry(root, width=30)

#empty label:
below_ih_entry = tk.Label(root, text="")

num_of_item_hired = tk.Label(root, text="Number of items hired")
n_o_i_hired = ttk.Entry(root, width=20)

#button:1
append_the_details = ttk.Button(root, text="APPEND DETAILS", command=append_details_one)

below_appenddtails_blank = tk.Label(root, text="")

delete_user_input_row_one = ttk.Button(root, text="DELETE ROW", command=d_lete_r_one)

user_info_r_one = tk.Label(root, text="")

#____________Info_1____________#
j_p_h_title.grid(row=0, column=2)
ent_dtail.grid(row=1, column=0)

# empty label for spacing-------
below_ent_dtail.grid(row=2, column=0)
#-------------------------------

customer_full_name.grid(row=3, column=0)
cfn_user_entry.grid(row=3, column=1)

# empty label for spacing-------
below_cfn_entry.grid(row=4, column=0)
#-------------------------------

recipt_number.grid(row=5, column=0)
r_n_entry.grid(row=5, column=1)

item_hired.grid(row=2, column=3)
ih_user_entry.grid(row=2, column=4)

# empty label for spacing-------
below_ih_entry.grid(row=3, column=3)
#-------------------------------

num_of_item_hired.grid(row=4, column=3)
n_o_i_hired.grid(row=4, column=4)

append_the_details.grid(row=5, column=4)

clear_all.grid(row=6, column=3)

# empty label for spacing-------
below_appenddtails_blank.grid(row=6, column=0)
#-------------------------------

root.mainloop()