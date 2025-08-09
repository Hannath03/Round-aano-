import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


def calculate_roundness(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return image, None, None, None

    contour = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)

    if perimeter == 0:
        return image, None, None, None

    
    roundness = (4 * np.pi * area) / (perimeter ** 2)

    
    cv2.drawContours(image, [contour], -1, (0, 44, 91), 4)

    return image, roundness, area, perimeter


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if not file_path:
        return

    processed_image, roundness, area, perimeter = calculate_roundness(file_path)

    if roundness is None:
        messagebox.showerror("Oops!", "No chapati detected! Try another image 🍽️")
        return

    
    processed_image_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(processed_image_rgb)
    pil_img = pil_img.resize((300, 300))
    tk_img = ImageTk.PhotoImage(pil_img)

    panel.config(image=tk_img)
    panel.image = tk_img

    
    if roundness > 0.95:
        verdict = "🌟 PERFECT CIRCLE ALERT! NASA SHOULD STUDY THIS CHAPATI FOR PLANETARY ORBITS! YOU ARE A CHAPATI ROCKSTAR! 🌟"
    elif roundness > 0.8:
        verdict = "😎 ROUND ENOUGH TO ROLL,FLAT ENOUGH TO FOLD- MULTITASKING CHAPATHI! ⭐"
    else:
        verdict = "🤪 YOUR CHAPATI FAILED IN BOTH GEOMETRY AND ART!"

    # Full analysis report
    report = (
        f"🥟 Chapati Roundness Check 🥟\n\n"
        f"🟡 Area: {area:.2f} px²\n"
        f"🟠 Perimeter: {perimeter:.2f} px\n"
        f"🔵 Roundness Score: {roundness:.3f}\n\n"
        f"🎉 {verdict}"
    )

    roundness_label.config(
        text=report,
        font=("Comic Sans MS", 14, "bold"),
        fg="#5b2c00",
        bg="#f0fff0",
        justify=LEFT
    )

# GUI Setup
root = Tk()
root.title("🤔ROUND AANO🙂 ?")

root.geometry("750x550")
root.configure(bg="#ffe5b4")

# Title
title_frame = Frame(root, bg="#ffb347")
title_frame.pack(fill=X, pady=15)
title_label = Label(
    title_frame,
    text="✨ Is Your Chapati a Perfect Circle? ✨",
    font=("Papyrus", 20, "bold"),
    bg="#ffb347",
    fg="#5b2c00"
)
title_label.pack(padx=10, pady=10)

# Upload Button
btn = Button(
    root,
    text="🍽️ Upload Your Chapati Image 🍽️",
    command=open_image,
    font=("Helvetica", 16, "bold"),
    bg="#ffb347",
    fg="white",
    padx=15,
    pady=10,
    activebackground="#ffb347"
)
btn.pack(pady=20)

# Frame for Image & Result side by side
content_frame = Frame(root, bg="#ffe5b4")
content_frame.pack(pady=15)

# Image panel on left
panel = Label(content_frame, bg="#fff9e6", width=300, height=300, bd=5, relief="ridge")
panel.pack(side=LEFT, padx=15)

# Result label on right
roundness_label = Label(
    content_frame,
    text="📊 Upload an image to see your Chapati's analysis!",
    font=("Arial", 14, "italic"),
    bg="#ffe5b4",
    fg="#333333",
    justify=LEFT,
    wraplength=300
)
roundness_label.pack(side=RIGHT, padx=15)

# Footer
footer = Label(
    root,
    text="“A round chapati is the shape of happiness 🥳”",
    font=("Comic Sans MS", 20, "italic"),
    bg="#ffe5b4",
    fg="#7d5a50"
)
footer.pack(side=BOTTOM, pady=15)

root.mainloop()



