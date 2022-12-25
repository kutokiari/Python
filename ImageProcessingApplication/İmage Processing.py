import numpy as np
import cv2
import tkinter as tk
import tkinter.font as font
from tkinter import filedialog


#Creating and customizing the design of our GUI
root = tk.Tk()
root.title("Photo Filtering")
root.geometry("968x724")
canvas = tk.Canvas(root , height = 724 , width = 968 , bg = "#343434")
canvas.pack()
my_font = font.Font(family='Futura', size=12)
frame = tk.Frame(root , bg = "#676767")
frame.place(relwidth = 0.45 , relheight = 0.25 , relx = 0.25 , rely = 0.02)


# Open an image file and return the image as a NumPy array
def open_image():
  file_path = filedialog.askopenfilename()
  image = cv2.imread(file_path)
  return image

#Open the image file and store the returned image in a variable
image = open_image()


# Applying a grayscale filter, saving the output image and displaying the image
def grayscaled_image(image):
  gray_photo = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  cv2.imwrite("C:/Users/enisb/OneDrive/Desktop/Code/grayscale_version.png", gray_photo)
  return gray_photo

# # Applying a blurring filter, saving the output image and displaying the image
def blurred_image(image):
  blur_photo = cv2.GaussianBlur(image, (15, 15), 0)
  cv2.imwrite("C:/Users/enisb/OneDrive/Desktop/Code/blur_version.png", blur_photo)
  return blur_photo

# Applying a sharpening filter, saving the output image and displaying the image
def sharpened_image(image):
  fltr = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
  sharpen_photo = cv2.filter2D(image, -1, fltr)
  cv2.imwrite("C:/Users/enisb/OneDrive/Desktop/Code/sharpen_version.png", sharpen_photo)
  return sharpen_photo

# Applying a negative filter, saving the output image and displaying the image
def negative_image(image):
  negative_photo = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  colored_negative = abs(255-negative_photo)
  cv2.imwrite("C:/Users/enisb/OneDrive/Desktop/Code/negative_version.png" , negative_photo)
  return negative_photo


#Creating 4 buttons for each filte
rgb2gray_button = tk.Button(root , text = "Grayscale" , padx = 48, pady = 12 , fg = "white" , bg = "#343434" , command = lambda: grayscaled_image(image))
rgb2gray_button['font'] = my_font
rgb2gray_button.pack(side = "top")
rgb2gray_button.place(x = 270 , y = 40)

sharp_button = tk.Button(root , text = "Sharpening" , padx = 39, pady = 12 , fg = "white" , bg = "#343434" , command = lambda: sharpened_image(image))
sharp_button['font'] = my_font
sharp_button.pack(side = "top")
sharp_button.place(x = 480 , y = 40)

negative_button = tk.Button(root , text = "Negative" , padx = 52, pady = 12 , fg = "white" , bg = "#343434" , command = lambda: negative_image(image))
negative_button['font'] = my_font
negative_button.pack(side = "top")
negative_button.place(x = 270 , y = 120)

blur_button = tk.Button(root , text = "Blurring" , padx = 52, pady = 12 , fg = "white" , bg = "#343434" , command = lambda: blurred_image(image))
blur_button['font'] = my_font
blur_button.pack(side = "top")
blur_button.place(x = 480 , y = 120)

root.protocol("WM_DELETE_WINDOW", root.destroy)
root.mainloop()

