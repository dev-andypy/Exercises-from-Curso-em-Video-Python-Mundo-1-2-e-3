import qrcode
data = str(input("Digite a URL para o QrCode: "))

img = qrcode.make(data)
type(img)  # qrcode.image.pil.PilImage
img.save("C:/Users/gosto/Desktop/erik/myqrcode.png")