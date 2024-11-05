import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App")

        self.original_image = None
        self.processed_image = None

        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=10)

        self.filter_var = tk.StringVar(value="blur")
        self.filter_menu = tk.OptionMenu(self.root, self.filter_var, "blur", "gaussian", "median")
        self.filter_menu.pack(pady=5)

        self.morphology_var = tk.StringVar(value="erode")
        self.morphology_menu = tk.OptionMenu(self.root, self.morphology_var, "erode", "dilate", "open", "close")
        self.morphology_menu.pack(pady=5)

        self.kernel_size_var = tk.StringVar(value="3")
        self.kernel_size_entry = tk.Entry(self.root, textvariable=self.kernel_size_var, width=5)
        self.kernel_size_entry.pack(pady=5)

        self.process_button = tk.Button(self.root, text="Process Image", command=self.process_image)
        self.process_button.pack(pady=10)

        self.original_label = tk.Label(self.root)
        self.original_label.pack(side=tk.LEFT, padx=20)

        self.processed_label = tk.Label(self.root)
        self.processed_label.pack(side=tk.RIGHT, padx=20)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.bmp")])
        if file_path:
            self.original_image = cv2.imread(file_path)
            self.display_image(self.original_image, self.original_label)

    def process_image(self):
        if self.original_image is None:
            messagebox.showerror("Error", "No image loaded")
            return

        img = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)

        filter_type = self.filter_var.get()
        if filter_type == "blur":
            img = cv2.blur(img, (5, 5))
        elif filter_type == "gaussian":
            img = cv2.GaussianBlur(img, (5, 5), 0)
        elif filter_type == "median":
            img = cv2.medianBlur(img, 5)

        morphology_type = self.morphology_var.get()
        kernel_size = int(self.kernel_size_var.get())
        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        if morphology_type == "erode":
            img = cv2.erode(img, kernel, iterations=1)
        elif morphology_type == "dilate":
            img = cv2.dilate(img, kernel, iterations=1)
        elif morphology_type == "open":
            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        elif morphology_type == "close":
            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

        self.processed_image = img
        self.display_image(self.processed_image, self.processed_label)

    def display_image(self, img, label):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()