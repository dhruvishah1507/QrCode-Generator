import customtkinter as ctk
from playsound3 import playsound
from PIL import Image
import qrcode



window = ctk.CTk()
window.geometry("400x500")
window.resizable(width=False, height=False)
window.title("QRCode Generator")

qrimage = None

def genQR():
    global qrimage
    textURL = url.get()
    Code = qrcode.make(textURL)
    Code.save("NewCode.png")
    qrimage = ctk.CTkImage(light_image=Image.open("NewCode.png"), size=(300,300))
    imglab.configure(image=qrimage)
    



label = ctk.CTkLabel(window, text="QRCode Gen - DhruviCodes", font=("Vardana", 24)).pack(pady=10)

url = ctk.CTkEntry(window, placeholder_text="Enter your URL here.....", width=300, font=("Vardana", 20))
url.pack(pady=20)

getbtn = ctk.CTkButton(window, text="Genenrate QR", font=("Varadana",24), command=lambda: genQR())
getbtn.pack(pady=10)

imglab = ctk.CTkLabel(window, text="")
imglab.pack(pady=20)


window.mainloop()