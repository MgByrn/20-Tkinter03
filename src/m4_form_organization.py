###############################################################################
# DONE: 1. (5 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 18 and
#   paste it below.
#
#   Now, use the geometry managers we have learned about and reorganize/
#   reformat your fillable form. You must use more than just the pack() method,
#   but you can still use it if it is what you need in a certain spot.
#
#   You may need to add more frames and such to move things around effectively.
#
#   Feel free to be creative on how you want your form to look.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
import tkinter as tk

def submit_form():
    name = name_entry.get()
    address_line1 = address_line1_entry.get()
    address_line2 = address_line2_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_code_entry.get()
    phone_number = phone_number_entry.get()
    email = email_entry.get()
    print("Name:", name)
    print("Address Line 1:", address_line1)
    print("Address Line 2:", address_line2)
    print("City:", city)
    print("State:", state)
    print("Zip Code:", zip_code)
    print("Phone Number:", phone_number)
    print("Email Address:", email)

window = tk.Tk()
window.title("Form")
window.geometry("400x400")

form_frame = tk.Frame(window, bg="CadetBlue")
form_frame.place(relx=0.5, rely=0.4, anchor="center")

labels = ["Name:", "Address Line 1:", "Address Line 2:", "City:", "State:", "Zip Code:", "Phone Number:", "Email Address:"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(form_frame, text=label_text, bg="CadetBlue")
    label.grid(row=i, column=0, sticky="e", pady=5)

    entry = tk.Entry(form_frame)
    entry.grid(row=i, column=1, padx=(5, 5), pady=5, sticky="ew")
    entries.append(entry)

name_entry = entries[0]
address_line1_entry = entries[1]
address_line2_entry = entries[2]
city_entry = entries[3]
state_entry = entries[4]
zip_code_entry = entries[5]
phone_number_entry = entries[6]
email_entry = entries[7]

submit_button = tk.Button(window, text="Submit", command=submit_form, bg="CadetBlue", fg="black")
submit_button.place(relx=0.5, rely=0.9, anchor="center")

window.mainloop()
