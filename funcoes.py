import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


def imagem(texto):
    
    #fundo = Image.open('fundo.png')
    img = Image.open("pessoa.png")

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", 70)
    #qr.thumbnail((800,800) , Image.ANTIALIAS)
    #qr = qr.resize((780,780), resample=3, box=None, reducing_gap=None)
    draw.text((10, 10),texto,(255,0,0),font=font ,stroke_width=2) #713 457
    #fundo.paste(qr, (512, 743)) #570 803
    #nome = Nome + ".png"
    img.save("pessoa.png","png")
    #bot.send_message(-1001182585528, Nome)
    #bot.send_photo(chat_id=-1001182585528, photo=open(nome, 'rb'))


