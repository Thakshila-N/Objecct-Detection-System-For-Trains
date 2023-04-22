import tkinter as tk
import subprocess

from PIL import Image, ImageFilter, ImageTk

class NavigationBar:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("PixelScope")

        # Load background image
        bg_image = Image.open("J:/IT2019100/OpenCV/img/bg_image.jpg")
        bg_image = bg_image.resize((600, 400), Image.ANTIALIAS)

        # Convert background image to RGBA mode if it's not already
        if bg_image.mode != "RGBA":
            bg_image = bg_image.convert("RGBA")

        # Apply blur filter to the image
        bg_image = bg_image.filter(ImageFilter.BLUR)

        # Create a transparent overlay image with desired opacity (0.5 for 50% opacity)
        overlay = Image.new("RGBA", bg_image.size, (0, 0, 0, 158))  # 128 for 50% opacity

        # Convert the blended image to PhotoImage
        self.bg_photo = ImageTk.PhotoImage(Image.alpha_composite(bg_image, overlay))

        # Create background label
        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create Menu Bar
        menubar = tk.Menu(self.root)

        # Create Home Menu
        menubar.add_command(label="Home", command=self.show_welcome)

        # Create File Menu
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Object Detection", command=self.open_main)

        # Add Menu Bar to the Root Window
        self.root.config(menu=menubar)

        # Create a frame to hold the welcome label
        welcome_frame = tk.Frame(self.root, bg=self.root.cget("bg"), bd=0, highlightthickness=0)  # Set border thickness to 0
        welcome_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create the welcome label with a transparent background and no border
        self.welcome_label = tk.Label(welcome_frame, text="Welcome to PixelScope", font=("Satisfy", 24), fg="black", bg=welcome_frame["bg"], highlightthickness=0, bd=0)
        self.welcome_label.pack()

    # Function to open main.py
    def open_main(self):
        subprocess.call(["python", "main.py"])

    # Function to show welcome message
    def show_welcome(self):
        self.welcome_label.lift()  # Bring existing label to top of stacking order


if __name__ == "__main__":
    root = tk.Tk()
    nb = NavigationBar(root)
    root.mainloop()
