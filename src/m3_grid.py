import tkinter as tk

window = tk.Tk()
window.grid_rowconfigure(0, weight=1, minsize=50)
window.grid_columnconfigure(0, weight=1, minsize=50)
window.grid_columnconfigure(1, weight=1, minsize=50)
# I had trouble figuring this out, why did it require two different column configurations if they were in the same window?
framea = tk.Frame(master=window, bg="CadetBlue", padx=5, pady=5)
framea.grid(row=0, column=0, sticky="nesw")

labela = tk.Label(master=framea, text="Frame A")
labela.pack()

frameb = tk.Frame(master=window, bg="Dark Olive Green", padx=5, pady=5)
frameb.grid(row=0, column=1, sticky="nesw")

labelb = tk.Label(master=frameb, text="Frame B")
labelb.pack()


window.mainloop()


###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (5 pts)
#
#   Now, create two frames in your window.
#
#   Use the grid() method to place them in the window side by side to each
#   other. Both frames should have 5px of padding in all directions.
#
#   Use the configure methods to make these columns and row responsive in all
#   directions. Choose minimum sizes that make sense (no text should be cut
#   off) but the two columns should both have equal weight (so they remain the
#   same relative size to each other).
#
#   Also, place a label in each frame labeling them as Frame A and Frame B and
#   give them different background colors.
#
#   Use the pack() method simply put the label in each frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################