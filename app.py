import tkinter as tk
from tkinter import messagebox, simpledialog


# self is the instance of the class we're working with
class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def find_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                return recipe
        return None

# Initialize manager
manager = RecipeManager()

# GUI Functions
def add_recipe_gui():
    name = simpledialog.askstring("Recipe Name", "Enter the recipe name:")
    if not name:
        return

    ingredients_input = simpledialog.askstring("Ingredients", "Enter ingredients (comma-separated):")
    if not ingredients_input:
        return
    ingredients = [ing.strip() for ing in ingredients_input.split(",")]

    instructions_list = []
    messagebox.showinfo("Instructions", "Enter each instruction step one by one. Type 'end' to finish.")
    while True:
        step = simpledialog.askstring("Instruction Step", "Enter instruction step (or type 'end' to finish):")
        if step is None or step.lower() == 'end':
            break
        instructions_list.append(step.strip())

    recipe = Recipe(name, ingredients, instructions_list)
    manager.add_recipe(recipe)
    update_recipe_list()
    messagebox.showinfo("Success", f"Recipe '{name}' added successfully!")


def display_recipe_gui():
    selected = listbox.curselection() 
    # Get the selected recipe from the list
    if not selected:
        messagebox.showerror("Error", "Please select a recipe to display.")
        return

    index = selected[0]
    recipe = manager.recipes[index]

    info = f"Recipe: {recipe.name}\n\nIngredients:\n"
    for ing in recipe.ingredients:
        info += f"- {ing}\n"
    
    info += "\nInstructions:\n"
    for idx, step in enumerate(recipe.instructions, 1):
        info += f"{idx}. {step}\n"

    messagebox.showinfo("Recipe Details", info)


def update_recipe_list():
    listbox.delete(0, tk.END) 
    for recipe in manager.recipes:
        listbox.insert(tk.END, recipe.name)


def landing_page():
    landing = tk.Tk()
    landing.title("Landing Page")
    landing.geometry("500x700")
    landing.configure(bg='#1B3916')

    middle_text = tk.Label(landing, text="CREATE, SAVE, FIND YOUR NEXT MEAL RECIPE", font=("Times", 16), bg="#1B3916")
    middle_text.place(relx=0.5, rely=0.4, anchor='center')

    continue_button = tk.Button(
        landing,
        text="Click to start",
        font=("Times", 14),
        bg="white",
        height=2,
        width=20,
        command=lambda: [landing.destroy()]
    )
    continue_button.place(relx=0.5, rely=0.5, anchor='center')

    bottom_text = tk.Label(landing, text="Brought to you by SIAF", font=("Times", 12), bg="#1B3916")
    bottom_text.place(relx=0.5, rely=0.8, anchor='center')
    
    landing.mainloop()

if __name__ == "__main__":
    landing_page()


# Main GUI window
root = tk.Tk()
root.title("SIAF Recipe Manager")
root.geometry("500x600")
root.configure(bg='#1B3916')

# root is the main window of the Tkinter application. It serves as the container for all other widgets.


top_text = tk.Label(root, text="Recipe names:", font=("Times", 16), bg="#1B3916", fg="white", width=50)
top_text.place(relx=0.1, rely=0.1, anchor='w') 

# frame is a container widget that can hold other widgets. It helps in organizing the layout of the GUI.

listbox = tk.Listbox(root, width=50, bg='white', fg="green", height=15)
listbox.place(relx=0.5, rely=0.4, anchor='center')

frame = tk.Frame(root)
frame.pack(pady=1)
frame.place(relx=0.5, rely=0.7, anchor='center')

add_button = tk.Button(
    frame, 
    text="Add Recipe", 
    command=add_recipe_gui, 
    width=23,
    height=2,
    font=("Times", 14)
    )
add_button.grid(row=0, column=0)

display_button = tk.Button(
    frame, 
    text="Display Recipe", 
    command=display_recipe_gui, 
    width=23,
    height=2,
    font=("Times", 14),
    )
display_button.grid(row=0, column=1)


quit_button = tk.Button(
    root, 
    text="Quit app", 
    font=("Times", 14),
    command=root.destroy, 
    width=51,
    height=2,
    bg="white",
    )
quit_button.place(relx=0.5, rely=0.8, anchor='center')

root.mainloop()


# The .mainloop() method is the main event loop of the Tkinter application. It keeps the window open and waits for user interaction. When the user interacts with the GUI (like clicking buttons), the corresponding functions are called to handle those events.