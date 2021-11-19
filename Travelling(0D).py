from PIL import Image
me = Image.open("Foisal.jpg")
bg = Image.open("Paris.jpg")
bg.paste(me,(0,0),me)
bg.show()
print("[Program finished]")