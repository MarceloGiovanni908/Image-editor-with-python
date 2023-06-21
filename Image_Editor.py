import tkinter as tk
from tkinter.constants import ANCHOR
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
from tkinter import filedialog
from tkinter import ttk
import cv2
import numpy as np

#heydar 
def yellowButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_BGR2RGB)
    opencvImage[:, :, 0] = 20
    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    displayImage(outputImage)

def cyanButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_BGR2RGB)
    opencvImage[:, :, 0] = 0  # Set blue channel to 0
    global outputImage
    outputImage = Image.fromarray(opencvImage)
    displayImage(outputImage)

def pinkButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_BGR2RGB)
    opencvImage[:, :, 0] = 255  # Mengatur komponen warna biru menjadi 255 (maksimum)
    opencvImage[:, :, 2] = 255  # Mengatur komponen warna merah menjadi 255 (maksimum)
    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    displayImage(outputImage)

def blueButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_BGR2RGB)
    opencvImage[:, :, 0] = 255
    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    displayImage(outputImage)
#sekar
def displayImage(displayImage):
    imageToDisplay = displayImage.resize((800,500), Image.ANTIALIAS)
    imageToDisplay = ImageTk.PhotoImage(imageToDisplay)
    showWindow.config(image=imageToDisplay)
    showWindow.photo_ref = imageToDisplay
    showWindow.pack()

def importButton_callback():
    global originalImage
    filename = filedialog.askopenfilename()
    originalImage = Image.open(filename)
    displayImage(originalImage)

def saveButton_callback():
    savefile = filedialog.asksaveasfile(defaultextension=".jpg")
    outputImage.save(savefile)

def closeButton_callback():
    window.destroy()
#nicholas
def brightness_callback(brightness_pos):
    brightness_pos = float(brightness_pos)
    print(brightness_pos)
    global outputImage
    enhancer = ImageEnhance.Brightness(originalImage)
    outputImage = enhancer.enhance(brightness_pos)
    displayImage(outputImage)

def contrast_callback(contrast_pos):
    contrast_pos = float(contrast_pos)
    print(contrast_pos)
    global outputImage
    enhancer = ImageEnhance.Contrast(originalImage)
    outputImage = enhancer.enhance(contrast_pos)
    displayImage(outputImage)

def color_callback(color_pos):
    color_pos = float(color_pos)
    print(color_pos)
    global outputImage
    enhancer = ImageEnhance.Color(originalImage)
    outputImage = enhancer.enhance(color_pos)
    displayImage(outputImage)

def sepiaButton_callback():
    opencvImage = np.array(originalImage)
    R = opencvImage[:, :, 2]  # Red channel
    G = opencvImage[:, :, 1]  # Green channel
    B = opencvImage[:, :, 0]  # Blue channel

    R_sepia = (R * 0.393 + G * 0.769 + B * 0.189)
    G_sepia = (R * 0.349 + G * 0.686 + B * 0.168)
    B_sepia = (R * 0.272 + G * 0.534 + B * 0.131)

    # Ensure values are within valid range
    R_sepia = np.clip(R_sepia, 0, 255)
    G_sepia = np.clip(G_sepia, 0, 255)
    B_sepia = np.clip(B_sepia, 0, 255)

    opencvImage[:, :, 2] = R_sepia
    opencvImage[:, :, 1] = G_sepia
    opencvImage[:, :, 0] = B_sepia

    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    displayImage(outputImage)

#kode untuk membentuk GUI pada aplikasi
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.title("IMAGE EDITOR KELOMPOK 2")
window['background'] = '#000000'
window.geometry(f'{screen_width}x{screen_height}')

# Create Frames
Frame1 = tk.Frame(window, height=100, bg="#000000")
Frame1.pack(anchor=tk.NW, fill=tk.X)

Frame2 = tk.Frame(window, height=200, bg="#222222")
Frame2.pack(anchor=tk.NW, fill=tk.X)

Frame3 = tk.Frame(window, height=100, bg="#222222")
Frame3.pack(anchor=tk.N, fill=tk.X)

# Create Labels and Buttons
welcome = tk.Label(Frame1, text="IMAGE EDITOR KELOMPOK 2", font=("Arial", 25, "bold"), pady=20, padx=20, bg="#000000", fg="#FFFFFF")
welcome.pack()

importButton = tk.Button(Frame1, text="Import", padx=10, pady=5, bg="#00FF00", fg="black", font=("Arial", 14), command=importButton_callback)
importButton.pack(side=tk.LEFT, padx=20)

saveButton = tk.Button(Frame1, text="Save", padx=10, pady=5, bg="#00FF00", fg="black", font=("Arial", 16), command=saveButton_callback)
saveButton.pack(side=tk.LEFT, padx=20)

closeButton = tk.Button(Frame1, text="Close", padx=10, pady=5, bg="#00FF00", fg="black", font=("Arial", 16), command=closeButton_callback)
closeButton.pack(side=tk.LEFT, padx=20)

style = ttk.Style()
style.configure("CustomScale.Horizontal.TScale", troughcolor="#555555", sliderthickness=15, sliderlength=30)

#buat label dari slider brigthness
brightnessLabel = tk.Label(Frame2, text="Brightness", font=("Arial", 16, "bold"), bg="#222222", fg="#FFFFFF")
brightnessLabel.pack(anchor=tk.W, padx=20)

#buat slider dari brigthness
brightnessSlider = ttk.Scale(Frame2, style="CustomScale.Horizontal.TScale", length=screen_width, from_=0, to=2, orient=tk.HORIZONTAL,
                             command=brightness_callback)
brightnessSlider.set(1)
brightnessSlider.pack(anchor=tk.N, pady=10)

#buat label dari slider contrast
contrastLabel = tk.Label(Frame2, text="Contrast", font=("Arial", 16, "bold"), bg="#222222", fg="#FFFFFF")
contrastLabel.pack(anchor=tk.W, padx=20)

#buat slider dari contrast
contrastSlider = ttk.Scale(Frame2, style="CustomScale.Horizontal.TScale", length=screen_width, from_=0, to=2, orient=tk.HORIZONTAL,
                           command=contrast_callback)
contrastSlider.set(1)
contrastSlider.pack(anchor=tk.N, pady=10)

#buat label dari slider saturation
colorLabel = tk.Label(Frame2, text="Saturation", font=("Arial", 16, "bold"), bg="#222222", fg="#FFFFFF")
colorLabel.pack(anchor=tk.W, padx=20)

#buat slider dari saturation
colorSlider = ttk.Scale(Frame2, style="CustomScale.Horizontal.TScale", length=screen_width, from_=0, to=2, orient=tk.HORIZONTAL,
                        command=color_callback)
colorSlider.set(1)
colorSlider.pack(anchor=tk.N, pady=10)

#pembuatan tombol dari filter filter pada aplikasi
yellowButton = tk.Radiobutton(Frame3, text="Yellow Filter", font=("Arial", 16, "bold"), width=20, bg="#FFD700", fg="black",
                             value=1, command=yellowButton_callback)
yellowButton.pack(side=tk.LEFT, padx=20)

blueButton = tk.Radiobutton(Frame3, text="Cyan Filter", font=("Arial", 16, "bold"), width=20, bg="#00FFFF", fg="black",
                            value=2, command=cyanButton_callback)
blueButton.pack(side=tk.LEFT, padx=20)

pinkButton = tk.Radiobutton(Frame3, text="Pink Filter", font=("Arial", 16, "bold"), width=20, bg="#EE1289", fg="black",
                            value=3, command=pinkButton_callback)
pinkButton.pack(side=tk.LEFT, padx=20)

orangeButton = tk.Radiobutton(Frame3, text="Blue Filter", font=("Arial", 16, "bold"), width=20, bg="#0000FF", fg="black",
                              value=4, command=blueButton_callback)
orangeButton.pack(side=tk.LEFT, padx=20)

sepiaButton = tk.Radiobutton(Frame3, text="Sepia Filter", font=("Arial", 16, "bold"), width=20, bg="#DAA520", fg="black",
                             value=5, command=sepiaButton_callback)
sepiaButton.pack(side=tk.LEFT, padx=20)

showWindow = tk.Label(window)
showWindow.pack()

tk.mainloop()