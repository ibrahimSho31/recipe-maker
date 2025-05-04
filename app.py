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

def edit_recipe_gui():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a recipe to edit.")
        return

    index = selected[0]
    recipe = manager.recipes[index]

    # Prompt for new values (pre-fill with current values)
    new_name = simpledialog.askstring("Edit Recipe Name", "Enter the new recipe name:", initialvalue=recipe.name)
    if not new_name:
        return

    new_ingredients_input = simpledialog.askstring("Edit Ingredients", "Enter ingredients (comma-separated):", initialvalue=", ".join(recipe.ingredients))
    if not new_ingredients_input:
        return
    new_ingredients = [ing.strip() for ing in new_ingredients_input.split(",")]

    new_instructions = []
    messagebox.showinfo("Edit Instructions", "Enter each instruction step one by one. Type 'end' to finish.")
    while True:
        step = simpledialog.askstring("Instruction Step", "Enter instruction step (or type 'end' to finish):")
        if step is None or step.lower() == 'end':
            break
        new_instructions.append(step.strip())

    # Update the recipe object
    recipe.name = new_name
    recipe.ingredients = new_ingredients
    recipe.instructions = new_instructions

    update_recipe_list()
    messagebox.showinfo("Success", f"Recipe '{new_name}' updated successfully!")


def update_recipe_list():
    listbox.delete(0, tk.END) 
    for recipe in manager.recipes:
        listbox.insert(tk.END, recipe.name)

# Main GUI window
root = tk.Tk()
root.title("SIAF Recipe Manager")
root.geometry("500x400")
# root is the main window of the Tkinter application. It serves as the container for all other widgets.


frame = tk.Frame(root)
frame.pack(pady=10)
# frame is a container widget that can hold other widgets. It helps in organizing the layout of the GUI.

add_button = tk.Button(frame, text="Add Recipe", command=add_recipe_gui, width=10)
add_button.grid(row=0, column=0, padx=10)

display_button = tk.Button(frame, text="Display Recipe", command=display_recipe_gui, width=10)
display_button.grid(row=0, column=1, padx=10)

edit_button = tk.Button(frame, text="Edit Recipe", command=edit_recipe_gui, width=10)
edit_button.grid(row=0, column=2, padx=10)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=20)

quit_button = tk.Button(root, text="Quit", command=root.destroy, width=10)
quit_button.pack(pady=10)

root.mainloop()

# The .mainloop() method is the main event loop of the Tkinter application. It keeps the window open and waits for user interaction. When the user interacts with the GUI (like clicking buttons), the corresponding functions are called to handle those events.