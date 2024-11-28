import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Function to organize files into different folders
def organize_files(directory):
    if not os.path.exists(directory):
        messagebox.showerror("Error", "The directory does not exist!")
        return

    # Detect the operating system using os.name
    is_windows = os.name == 'nt'

    # Define file categories and corresponding file extensions
    file_types = {
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audios': ['.mp3', '.wav', '.aac', '.flac'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
        'Misc': []
    }

    # Create folders for each file category if they don't already exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate over the files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Determine the file extension
        file_extension = os.path.splitext(file_name)[1].lower()

        # Find the appropriate category for the file
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                # Move the file to the corresponding folder
                destination = os.path.join(directory, folder, file_name)
                
                # Check if file already exists at the destination
                if not os.path.exists(destination):
                    if is_windows:
                        os.system(f'move "{file_path}" "{destination}"')
                    else:
                        os.system(f'mv "{file_path}" "{destination}"')
                moved = True
                break
        
        # If no matching category is found, move to the 'Misc' folder
        if not moved:
            misc_destination = os.path.join(directory, 'Misc', file_name)
            if not os.path.exists(misc_destination):
                if is_windows:
                    os.system(f'move "{file_path}" "{misc_destination}"')
                else:
                    os.system(f'mv "{file_path}" "{misc_destination}"')

    messagebox.showinfo("Success", "Files have been organized!")

# Create the main window
root = tk.Tk()
root.title("File Organizer")
root.geometry("500x300")  # Set a larger window size for a professional look

# Define a modern gradient background color
bg_color = "#34495e"  # Dark teal background
highlight_color = "#16a085"  # Light teal accent

# Define button and entry colors
button_color = "#1abc9c"  # Soft teal for buttons
button_hover_color = "#16a085"  # Darker shade for hover effect
entry_bg_color = "#ffffff"  # Dark gray background for entries
entry_fg_color = "#000000"  # Light gray text color for entry fields

# Function to browse and select folder
def browse_folder():
    folder_selected = filedialog.askdirectory()  # Open dialog to select folder
    if folder_selected:
        entry.delete(0, tk.END)  # Clear previous text
        entry.insert(0, folder_selected)  # Insert the selected folder path

# Function to be called when the submit button is clicked
def buttonCall():
    address = entry.get()  # Get text from the entry box
    if address:
        organize_files(address)  # Call the file organization function
    else:
        messagebox.showerror("Error", "No directory path entered!")

# Configure the window with a background color
root.config(bg=bg_color)

# Label for user input
label = tk.Label(root, text="Please Select Directory:", font=("Helvetica Neue", 15), padx=10, pady=5, bg=bg_color, fg=entry_fg_color)
label.pack(pady=20)  # Add padding around the label

# Entry (input field) where user can type or paste the directory path
entry = tk.Entry(root, width=40, font=("Helvetica Neue", 12), borderwidth=2, relief="flat", bg=entry_bg_color, fg=entry_fg_color)
entry.pack(pady=10)  # Add padding around the entry field

# Browse button to select the folder
browse_button = tk.Button(root, text="Browse Folder", command=browse_folder, font=("Helvetica Neue", 12), padx=10, pady=5, bg=button_color, fg="#ffffff", activebackground=button_hover_color, relief="flat")
browse_button.pack(pady=10)  # Add padding around the browse button

# Submit button to trigger the file organization
submit_button = tk.Button(root, text="Organize Files", command=buttonCall, font=("Helvetica Neue", 12), padx=10, pady=5, bg=button_color, fg="#ffffff", activebackground=button_hover_color, relief="flat")
submit_button.pack(pady=20)  # Add padding around the submit button

# Start the GUI event loop
root.mainloop()
