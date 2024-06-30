from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import ttk, filedialog, messagebox

# Function to display image dimensions
def display_image_dimensions(image):
    width, height = image.size
    return f"Current Image has Width(x): {width}, and Height(y): {height}"

def validate_fields():
    # Check if any Entry or Combobox is empty
    for entry in entries:
        if not entry.get().strip():
            messagebox.showwarning("Validation Error", "All fields are required!")
            return False

    for combobox in comboboxes:
        if not combobox.get().strip():
            messagebox.showwarning("Validation Error", "All fields are required!")
            return False

    # If all fields are filled
    return True

def submit_form():
    if validate_fields():
        # Proceed with form submission (e.g., save data, etc.)
        if current_image_path:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                image.save(save_path)
                print(f"Image saved successfully at {save_path}")
                messagebox.showinfo("Success", f"Image saved successfully at {save_path}")
        else:
            messagebox.showerror("Error", "No image uploaded!")

def upload_image():
    global wm_image_tk, watermark_image, img_info_label, current_image_path
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])

    if file_path:
        # Load and display the new image
        new_image = Image.open(file_path)
        new_image.thumbnail((800, 600))  # Thumbnail size adjustment
        wm_image_tk = ImageTk.PhotoImage(new_image)

        # Update the image label
        watermark_image.config(image=wm_image_tk)

        current_image_path = file_path

        # Update the image dimensions label
        img_info_label.config(text=display_image_dimensions(new_image))

def preview_image():
    if not current_image_path:
        messagebox.showerror("Error", "No image uploaded!")
        return

    if not validate_fields():
        return

    # Get all inputs
    text = text_field.get()
    color = color_field.get().strip()
    font_tk = font_field.get().strip()
    size = int(size_field.get())
    angle = int(angle_field.get())
    pos_x = int(position_X_field.get())
    pos_y = int(position_Y_field.get())

    # Load the image and create a draw object
    image = Image.open(current_image_path)
    draw = ImageDraw.Draw(image)

    # Load the font
    try:
        font = ImageFont.truetype(font_tk, size)
    except IOError:
        messagebox.showerror("Font Error", f"Font file '{font_tk}' not found!")
        return

    # Add the text to the image
    draw.text((pos_x, pos_y), text, fill=color, font=font, anchor="mm")

    # Rotate the image to apply the angle (if needed)
    image = image.rotate(angle, expand=1)

    # Show the preview
    preview_window = Toplevel()
    preview_window.title("Preview")
    preview_image_tk = ImageTk.PhotoImage(image)
    preview_label = Label(preview_window, image=preview_image_tk)
    preview_label.image = preview_image_tk
    preview_label.pack()


def save_picture():
    if validate_fields():
        # Proceed with form submission (e.g., save data, etc.)
        if current_image_path:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                # Get all inputs
                text = text_field.get()
                color = color_field.get().strip()
                font_tk = font_field.get().strip()
                size = int(size_field.get())
                angle = int(angle_field.get())
                pos_x = int(position_X_field.get())
                pos_y = int(position_Y_field.get())

                # Load the image and create a draw object
                image = Image.open(current_image_path)
                draw = ImageDraw.Draw(image)

                # Load the font
                try:
                    font = ImageFont.truetype(font_tk, size)
                except IOError:
                    messagebox.showerror("Font Error", f"Font file '{font_tk}' not found!")
                    return

                # Add the text to the image
                draw.text((pos_x, pos_y), text, fill=color, font=font, anchor="mm")

                # Rotate the image to apply the angle (if needed)
                image = image.rotate(angle, expand=1)
                image.save(save_path)
                print(f"Image saved successfully at {save_path}")
                messagebox.showinfo("Success", f"Image saved successfully at {save_path}")
        else:
            messagebox.showerror("Error", "No image uploaded!")


# Create the main application window
window = Tk()
window.config(height=800, width=1000, padx=20, pady=20, bg='black')
window.title('Image WaterMark App')
current_image_path = None

# Create a frame for the image
image_frame = Frame(window, bg='black')
image_frame.grid(row=0, column=0, padx=10, pady=10)

# Create a frame for the controls
control_frame = Frame(window, bg='black')
control_frame.grid(row=0, column=1, padx=20, pady=10, sticky='n')

# Create an empty label widget to display the image
watermark_image = Label(image_frame, bg='black')
watermark_image.grid(row=0, column=0)

# Create a label for the watermark text
label_fonts = ("Verdana", 14)

wm_label = Label(control_frame,
                 text='Create Your Water Mark',
                 bg='black',
                 fg='orange',
                 font=label_fonts
                 )
wm_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

# Create a label for the image dimensions
img_info_label = Label(control_frame,
                       text='No image uploaded yet',
                       bg='black',
                       fg='orange',
                       font=("Verdana", 12))
img_info_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

# Create an upload button
upload_button = Button(image_frame,
                       text='Upload Image',
                       bg='black',
                       fg='orange',
                       font=label_fonts,
                       activeforeground='black',
                       activebackground='lightblue',
                       command=upload_image
                       )
upload_button.grid(row=1, column=0, pady=(10, 5))

# Create text area
entries = []
comboboxes = []

text_label = Label(control_frame,
                   text='Text:',
                   bg='black',
                   fg='orange',
                   font=label_fonts
                   )
text_label.grid(row=3, column=0, pady=(10, 5), sticky='nw')

text_field = Entry(control_frame,
                   font=("Verdana", 14)
                   )
text_field.grid(row=3, column=0, pady=(10, 5))
entries.append(text_field)

# Create color area
color_label = Label(control_frame,
                    text='Color:',
                    bg='black',
                    fg='orange',
                    font=label_fonts
                    )
color_label.grid(row=4, column=0, pady=(10, 5), sticky='nw')

color_field = ttk.Combobox(control_frame,
                           font=("Verdana", 14)
                           )
color_field['values'] = ('White', 'Black', 'Red', 'Yellow', 'Blue')
color_field.grid(row=4, column=0, pady=(10, 5))
comboboxes.append(color_field)

# Create font area
font_label = Label(control_frame,
                   text='Fonts:',
                   bg='black',
                   fg='orange',
                   font=label_fonts
                   )
font_label.grid(row=5, column=0, pady=(10, 5), sticky='nw')

font_field = ttk.Combobox(control_frame,
                          font=("Verdana", 14)
                          )
font_field['values'] = (
    'arial.ttf',
    'times.ttf',
    'cour.ttf',
    'verdana.ttf',
    'georgia.ttf',
    'comic.ttf',
    'segoeui.ttf'
)
font_field.grid(row=5, column=0, pady=(10, 5))
comboboxes.append(font_field)

# Create size area
size_label = Label(control_frame,
                   text='Size:',
                   bg='black',
                   fg='orange',
                   font=label_fonts
                   )
size_label.grid(row=6, column=0, pady=(10, 5), sticky='nw')

size_field = Entry(control_frame,
                   font=("Verdana", 14)
                   )
size_field.grid(row=6, column=0, pady=(10, 5))
entries.append(size_field)

# Create angle area
angle_label = Label(control_frame,
                    text='Angle:',
                    bg='black',
                    fg='orange',
                    font=label_fonts
                    )
angle_label.grid(row=7, column=0, pady=(10, 5), sticky='nw')

angle_field = Entry(control_frame,
                    font=("Verdana", 14)
                    )
angle_field.grid(row=7, column=0, pady=(10, 5))
entries.append(angle_field)

# Create position X area
position_X_label = Label(control_frame,
                         text='Position X:',
                         bg='black',
                         fg='orange',
                         font=label_fonts
                         )
position_X_label.grid(row=8, column=0, pady=(10, 5), sticky='nw')

position_X_field = Entry(control_frame,
                         font=("Verdana", 14)
                         )
position_X_field.grid(row=8, column=0, pady=(10, 5))
entries.append(position_X_field)

# Create position Y area
position_Y_label = Label(control_frame,
                         text='Position Y:',
                         bg='black',
                         fg='orange',
                         font=label_fonts
                         )
position_Y_label.grid(row=9, column=0, pady=(10, 5), sticky='nw')

position_Y_field = Entry(control_frame,
                         font=("Verdana", 14)
                         )
position_Y_field.grid(row=9, column=0, pady=(10, 5))
entries.append(position_Y_field)

# Create preview button
preview_button = Button(control_frame,
                        text='Preview Image',
                        bg='black',
                        fg='orange',
                        font=label_fonts,
                        activeforeground='black',
                        activebackground='lightblue',
                        command=preview_image
                        )
preview_button.grid(row=10, column=0, pady=(10, 10))

# Create save image button
save_button = Button(control_frame,
                     text='Save Image',
                     bg='black',
                     fg='orange',
                     font=label_fonts,
                     activeforeground='black',
                     activebackground='lightblue',
                     command=save_picture
                     )
save_button.grid(row=11, column=0, pady=(10, 10))

window.mainloop()
