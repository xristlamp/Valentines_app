import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def show_message(message):
    message_window = tk.Toplevel(root, bg='#FFC0CB')
    message_window.title("Message")
    label = tk.Label(message_window, text=message, bg='#FFC0CB')
    label.pack()

# Συνάρτηση για να εμφανίζει μήνυμα με το πάτημα του κάθε κουμπιού
def show_message_wrapper(message):
    return lambda: show_message(message)


def login():
    name = name_entry.get()
    surname = surname_entry.get()
    password = password_entry.get()
    if name == "Glykaki" and surname == "Demi" and password == "1102021":
        show_frame(selection_frame)
    else:
        messagebox.showerror("Login Failed", "ΕΒΑΛΕΣ ΛΑΘΟΣΣΣ ΚΩΔΙΚΟ???. \n Ονοματεπώνομο σε Λατινικούς χαρακτήρες")

def option_selected(option):
    if option == "Option 1":
        show_frame(category_frame_1)
    elif option == "Option 2":
        show_frame(category_frame_2)
    elif option == "Option 3":
        show_frame(category_frame_3)
    elif option == "Option 4":
        show_frame(category_frame_4)
    elif option == "Option 5":
        show_frame(category_frame_5)
    elif option == "Option 6":
        show_frame(category_frame_6)
    elif option == "Option 7":
        show_frame(category_frame_7)
    elif option == "Option 8":
        show_frame(category_frame_8)
    elif option == "Option 9":
        show_frame(category_frame_9)
    elif option == "Option 10":
        show_frame(category_frame_10)



def animate_gif(frame_number=0):
    frame = gif_frames[frame_number]
    gif_label.configure(image=frame)
    root.after(60, animate_gif, (frame_number+1) % len(gif_frames))  # 100ms delay, loop to start


# Function to handle the checklist selections in category_frame_6
def handle_checklist():
    selections = [var.get() for var in checklist_vars]
    # Example logic based on selections
    if selections == [1, 1, 0, 1, 1]:  # Example combination
        option_selected("Option 4").pack()
    else:
        option_selected("Option 5").pack()

# Setting up the main window
root = tk.Tk()
root.title("Application")

# Create a container frame to hold all other frames
container = tk.Frame(root)
container.pack(fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Initialize all frames to be the same size as the container
frames = [tk.Frame(container, bg='#FFC0CB') for _ in range(12)]
login_frame, selection_frame, category_frame_1, category_frame_2, category_frame_3, category_frame_4, category_frame_5, category_frame_6, category_frame_7, category_frame_8, category_frame_9, category_frame_10 = frames


for frame in frames:
    frame.grid(row=0, column=0, sticky="nsew")

# Attempt to load GIF frames with error handling to avoid TclError
gif_frames = []
max_frames = 100  # Limit the number of frames to avoid infinite loops
try:
    for index in range(max_frames):
        frame = PhotoImage(file='love.gif', format=f'gif -index {index}')
        gif_frames.append(frame)
except (EOFError, tk.TclError):  # Catching TclError in addition to EOFError
    pass  # No more frames to load or invalid frame index

if not gif_frames:
    raise ValueError("Failed to load any frames from the GIF.")

# Load the "sad.gif" and prepare its animation frames, with error handling to avoid TclError
sad_gif_frames = []
try:
    for index in range(max_frames):  # Reusing the max_frames variable from earlier
        frame = PhotoImage(file='sad.gif', format=f'gif -index {index}')
        sad_gif_frames.append(frame)
except (EOFError, tk.TclError):  # Catching potential errors
    pass  # No more frames to load or invalid frame index

if not sad_gif_frames:
    raise ValueError("Failed to load any frames from 'sad.gif'.")

def animate_sad_gif(frame_number=0):
    frame = sad_gif_frames[frame_number]
    sad_gif_label.configure(image=frame)
    category_frame_2.after(100, animate_sad_gif, (frame_number+1) % len(sad_gif_frames))  # Loop to start

# Add the "sad.gif" to category_frame_2
sad_gif_label = tk.Label(category_frame_2)
sad_gif_label.pack()  # Place this before or after the category buttons, depending on where you want the GIF to appear
# Selection Frame with GIF
gif_label = tk.Label(selection_frame, image=gif_frames[0])  # Start with the first frame
gif_label.pack()


# Load the "oui.gif" and prepare its animation frames
oui_gif_frames = []
try:
    for index in range(max_frames):  # Reuse the max_frames variable
        frame = PhotoImage(file='oui.gif', format=f'gif -index {index}')
        oui_gif_frames.append(frame)
except (EOFError, tk.TclError):  # Handle potential errors
    pass  # Stop if no more frames are available or an error occurs

if not oui_gif_frames:
    raise ValueError("Failed to load any frames from 'oui.gif'.")

# Function to animate "oui.gif"
def animate_oui_gif(frame_number=0):
    frame = oui_gif_frames[frame_number]
    oui_gif_label.configure(image=frame)
    category_frame_3.after(100, animate_oui_gif, (frame_number+1) % len(oui_gif_frames))  # Loop animation

# Add the "oui.gif" label to category_frame_3
oui_gif_label = tk.Label(category_frame_3)
oui_gif_label.pack()  # Adjust placement as needed


# Load the "food.gif" and prepare its animation frames
food_gif_frames = []
try:
    for index in range(max_frames):  # Reuse the max_frames variable
        frame = PhotoImage(file='food.gif', format=f'gif -index {index}')
        food_gif_frames.append(frame)
except (EOFError, tk.TclError):  # Handle potential errors
    pass  # Stop if no more frames are available or an error occurs

if not food_gif_frames:
    raise ValueError("Failed to load any frames from 'food.gif'.")

# Function to animate "food.gif"
def animate_food_gif(frame_number=0):
    frame = food_gif_frames[frame_number]
    # Determine which label to update based on the currently raised frame
    if current_frame == category_frame_8:
        food_gif_label_8.configure(image=frame)
        category_frame_8.after(100, animate_food_gif, (frame_number+1) % len(food_gif_frames))
    elif current_frame == category_frame_10:
        food_gif_label_10.configure(image=frame)
        category_frame_10.after(100, animate_food_gif, (frame_number+1) % len(food_gif_frames))

# Add the "food.gif" labels to category_frame_8 and category_frame_10
food_gif_label_8 = tk.Label(category_frame_8)
food_gif_label_8.pack()  # Adjust placement as needed
food_gif_label_10 = tk.Label(category_frame_10)
food_gif_label_10.pack()  # Adjust placement as needed

# Track the current frame being shown
current_frame = None

# Load the "drink.gif" and prepare its animation frames
drink_gif_frames = []
try:
    for index in range(max_frames):  # Reuse the max_frames variable
        frame = PhotoImage(file='drink.gif', format=f'gif -index {index}')
        drink_gif_frames.append(frame)
except (EOFError, tk.TclError):  # Handle potential errors
    pass  # Exit loop if no more frames or an error occurs

if not drink_gif_frames:
    raise ValueError("Failed to load any frames from 'drink.gif'.")

# Function to animate "drink.gif"
def animate_drink_gif(frame_number=0):
    frame = drink_gif_frames[frame_number]
    # Update the correct label based on the current frame
    if current_frame == category_frame_7:
        drink_gif_label_7.configure(image=frame)
        category_frame_7.after(100, animate_drink_gif, (frame_number+1) % len(drink_gif_frames))
    elif current_frame == category_frame_9:
        drink_gif_label_9.configure(image=frame)
        category_frame_9.after(100, animate_drink_gif, (frame_number+1) % len(drink_gif_frames))

# Add the "drink.gif" labels to category_frame_7 and category_frame_9
drink_gif_label_7 = tk.Label(category_frame_7)
drink_gif_label_7.pack()  # Adjust placement as needed
drink_gif_label_9 = tk.Label(category_frame_9)
drink_gif_label_9.pack()  # Adjust placement as needed

# Update the show_frame function to start "drink.gif" animation in the appropriate frame
def show_frame(frame):
    global current_frame
    current_frame = frame  # Update the current frame
    frame.tkraise()
    if frame == selection_frame:
        animate_gif()
    elif frame == category_frame_2:
        animate_sad_gif()
    elif frame == category_frame_3:
        animate_oui_gif()
    elif frame in [category_frame_8, category_frame_10]:
        animate_food_gif()
    elif frame in [category_frame_7, category_frame_9]:
        animate_drink_gif()  # Start animating "drink.gif" when category_frame_7 or category_frame_9 is raised


# Login Frame Setup
tk.Label(login_frame, text="Name:", bg='#FFC0CB').pack()
name_entry = tk.Entry(login_frame)
name_entry.pack()
tk.Label(login_frame, text="Surname:", bg='#FFC0CB').pack()
surname_entry = tk.Entry(login_frame)
surname_entry.pack()
tk.Label(login_frame, text="Password:", bg='#FFC0CB').pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()
tk.Button(login_frame, text="Login", command=login, bg='#FFC0CB', activebackground='#FFC0CB').pack()

# Selection Frame
tk.Label(selection_frame, text="Κυρία Δέμη, θα θέλατυε να με συνοδέψετε για βαλεντίνα μου,ώστε να ζήσεται την πιο όμορφη,γλυκία και κουλτουρίαρα γεμάτη αστεία βραδία μαζι μου;").pack()
tk.Button(selection_frame, text="ΝΑΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙ", command=lambda: option_selected("Option 1")).pack()
tk.Button(selection_frame, text="όχι..", command=lambda: option_selected("Option 2")).pack()
tk.Button(selection_frame, text="Back", command=lambda: show_frame(login_frame)).pack()


# Category Frame for Option 1
tk.Label(category_frame_1, text="Διάλεξε κυρία αναποφάσιστη:").pack()
tk.Button(category_frame_1, text="Σπίτι", command=show_message_wrapper("φόρα λίγα και ΕΛΆ")).pack()
tk.Button(category_frame_1, text="Πάτρα", command=lambda: option_selected("Option 4")).pack()
tk.Button(category_frame_1, text="Ναύπακτο", command=lambda: option_selected("Option 5")).pack()
tk.Button(category_frame_1, text="ΔΕ ΜΠΟΡΩΩ ΝΑ ΑΠΟΦΑΣΙΣΩΩ", command=lambda: option_selected("Option 6")).pack()
tk.Button(category_frame_1, text="Back", command=lambda: show_frame(selection_frame)).pack()

# Category Frame for Option 2
tk.Label(category_frame_2, text="Νομίζω ότι πατήσατε καταλάθως λάθος κουμπί. Ξανα ρωτάω:").pack()
tk.Button(category_frame_2, text="ΝΑΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙ", command=lambda: option_selected("Option 1")).pack()
tk.Button(category_frame_2, text="όχι", command=lambda: option_selected("Option 3")).pack()
tk.Button(category_frame_2, text="Back", command=lambda: show_frame(login_frame)).pack()

# Category Frame for Option 3
tk.Label(category_frame_3, text="Σίγουρα θέλατε να πατήσετε ΝΑΙΙΙΙ αλλά δε το ξέρετε:").pack()
tk.Button(category_frame_3, text="ΝΑΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙ", command=lambda: option_selected("Option 1")).pack()
tk.Button(category_frame_3, text="ΟΥΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙ", command=lambda: option_selected("Option 1")).pack()
tk.Button(category_frame_3, text="Back", command=lambda: show_frame(login_frame)).pack()

# Category Frame for Option 4 για πατρα
tk.Label(category_frame_4, text="Πάτρα;;; Πώς και ετσι;;;;;:").pack()
tk.Button(category_frame_4, text="Φαγητό", command=lambda: option_selected("Option 8")).pack()
tk.Button(category_frame_4, text="Ποτό", command=lambda: option_selected("Option 7")).pack()
tk.Button(category_frame_4, text="Και τα δυο",command=show_message_wrapper("Άρα Γλυκάκι ψάχνουμε για ολά τα μαγαζίαα της Πάτρας")).pack()
tk.Button(category_frame_4, text="Back", command=lambda: show_frame(login_frame)).pack()

# Category Frame for Option 5 για ναυπακτο
tk.Label(category_frame_5, text="Ναύπακτοοοοοοοο:").pack()
tk.Button(category_frame_5, text="Φαγητό", command=lambda: option_selected("Option 10")).pack()
tk.Button(category_frame_5, text="Ποτό", command=lambda: option_selected("Option 9")).pack()
tk.Button(category_frame_5, text="Και τα δυο", command=show_message_wrapper("Άρα Γλυκάκι ψάχνουμε για ολά τα μαγαζίαα της Ναυπάκτου")).pack()
tk.Button(category_frame_5, text="Back", command=lambda: show_frame(login_frame)).pack()

# Category Frame for Option 7 για πατρα ποτο 
tk.Label(category_frame_7, text="Για ποτάκι στη Πάτρα έχουμε τα παρακάτω:").pack()
tk.Button(category_frame_7, text="Κοκτείλ", command=show_message_wrapper("Άρα Γλυκάκι ξεκινάμε την αναζήτηση για Κοκτέιλ στη Πάτρα")).pack()
tk.Button(category_frame_7, text="Κρασί", command=show_message_wrapper("Άρα Γλυκάκι ξεκινάμε την αναζήτηση για κρασάκι στη Πάτρα")).pack()
tk.Button(category_frame_7, text="Back", command=lambda: show_frame(login_frame)).pack()

# Category Frame for Option 8 για πατρα φαγητο
tk.Label(category_frame_8, text="Φαγητό στη Πάτρα:").pack()
tk.Button(category_frame_8, text="Ταβέρνα (στυλ Ψαθόπυργο)", command=show_message_wrapper("Άρα μικρό γουυυρουνάκι ξεκινάμε την αναζήτηση για ταβερνούλα στη Πάτρα")).pack()
tk.Button(category_frame_8, text="Καλό εστιατόριο", command=show_message_wrapper("Άρα μικρό γουυυρουνάκι ξεκινάμε την αναζήτηση για καλό εστιατόριο στη Πάτρα")).pack()
tk.Button(category_frame_8, text="Back", command=lambda: show_frame(login_frame)).pack()


# Category Frame for Option 9 για ναυπακτο ποτο 
tk.Label(category_frame_9, text="Για ποτάκι στη Ναύπακτο έχουμε τα παρακάτω").pack()
tk.Button(category_frame_9, text="Κοκτείλ", command=show_message_wrapper("Άρα Γλυκάκι ξεκινάμε την αναζήτηση για Κοκτέιλ στη Ναύπατκο")).pack()
tk.Button(category_frame_9, text="Κρασί", command=show_message_wrapper("Άρα Γλυκάκι ξεκινάμε την αναζήτηση για κρασάκι στη Ναύπατκο")).pack()
tk.Button(category_frame_9, text="Back", command=lambda: show_frame(login_frame)).pack()

# Category Frame for Option 8 για ναυπακτο φαγητο
tk.Label(category_frame_10, text="Φαγητό στη Ναύπακτο:").pack()
tk.Button(category_frame_10, text="Ταβέρνα", command=show_message_wrapper("Άρα μικρό γουυυρουνάκι ξεκινάμε την αναζήτηση για ταβερνούλα στην Ναύπατκο")).pack()
tk.Button(category_frame_10, text="Καλό Εστιατόριο", command=show_message_wrapper("Άρα μικρό γουυυρουνάκι ξεκινάμε την αναζήτηση για καλό εστιατόριο στην Ναύπατκο")).pack()
tk.Button(category_frame_10, text="Back", command=lambda: show_frame(login_frame)).pack()

# Category Frame for Option 6 - Adding the checklist
checklist_options = ["Φαγητό", "Ποτό", "Θέα", "Χαλαρό", "Επίσημο"]
checklist_vars = [tk.IntVar() for _ in checklist_options]

# Category Frame for Option 6
tk.Label(category_frame_6, text="Δίαλεξε και θα αποφασίσω εγω για εσένα:").pack()
for option, var in zip(checklist_options, checklist_vars):
    tk.Checkbutton(category_frame_6, text=option, variable=var).pack(anchor=tk.W)
tk.Button(category_frame_6, text="Submit", command=handle_checklist).pack()
tk.Button(category_frame_5, text="Back", command=lambda: show_frame(login_frame)).pack()

# Start with the login frame
show_frame(login_frame)

# Start the GUI event loop
root.mainloop()
