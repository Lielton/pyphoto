import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def open_image():
    global img, img_original
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        img = Image.open(file_path)
        img_original = img.copy()
        width_entry.delete(0, tk.END)
        width_entry.insert(0, img.width)
        height_entry.delete(0, tk.END)
        height_entry.insert(0, img.height)
        display_image(img)

def resize_image():
    global img, img_original
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        img = img_original.resize((width, height), Image.LANCZOS)
        display_image(img)
    except ValueError:
        messagebox.showerror('Error', 'Por favor, insira valores válidos para a largura e altura.')

def save_image():
    global img
    if img is None:
        messagebox.showerror('Error', 'Nenhuma imagem para salvar!')
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension='.png',
        filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            img.save(file_path)
            messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")
        except Exception as e:
            messagebox.showerror("Error", f"Não foi possível salvar a imagem: {e}")

def display_image(image):
    img_tk = ImageTk.PhotoImage(image)
    image_label.config(image=img_tk)
    image_label.image = img_tk

root = tk.Tk()
root.title("PyPhoto")

size_frame = tk.Frame(root)
size_frame.grid(row=0, column=0, padx=5, pady=5)

open_button = tk.Button(size_frame, text="Abrir Imagem", command=open_image)
open_button.grid(row=0, column=1, padx=5, pady=5)

tk.Label(size_frame, text='Largura:').grid(row=0, column=2)
width_entry = tk.Entry(size_frame, width=5)
width_entry.grid(row=0, column=3, padx=5)
tk.Label(size_frame, text='Altura:').grid(row=0, column=4)
height_entry = tk.Entry(size_frame, width=5)
height_entry.grid(row=0, column=5, padx=5)

resize_button = tk.Button(size_frame, text="Redimensionar", command=resize_image)
resize_button.grid(row=0, column=6, padx=5, pady=5)

save_button = tk.Button(size_frame, text="Salvar", command=save_image)
save_button.grid(row=0, column=7, padx=5, pady=5)

image_label = tk.Label(root)
image_label.grid(row=1, column=0, padx=5, pady=5)

img = None
img_original = None

root.mainloop()