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
    img.save("pessoa_e.png","png")
    #bot.send_message(-1001182585528, Nome)
    #bot.send_photo(chat_id=-1001182585528, photo=open(nome, 'rb'))

def tirinha(texto):
    fundo = Image.open('balao.jpg')
    img = Image.open("pessoa.png")

    draw = ImageDraw.Draw(fundo)

    font = ImageFont.truetype("arial.ttf", 15)

    #qr.thumbnail((800,800) , Image.ANTIALIAS)

    img_g = img.resize((120,120), resample=3, box=None, reducing_gap=None)
    img_p = img.resize((80,80), resample=3, box=None, reducing_gap=None)
    print(len(texto))
    if len(texto) > 12 :
        texto = texto[:12] + "\n" + texto[12:]
    if len(texto) > 25 :
        texto = texto[:25] + "\n" + texto[25:]
    if len(texto) > 38 :
        texto = texto[:38] + "\n" + texto[38:]
    if len(texto) > 51 :
        texto = texto[:51] 

    

    draw.text((460,110),texto,(255,0,0),font=font ) #713 457 #12 letras x 4 linhas
    
    fundo.paste(img_g, (50, 60)) 
    fundo.paste(img_p, (50, 340)) 
    fundo.paste(img_p, (372, 351)) 
    #nome = Nome + ".png"
    fundo.save("pessoa_b.png","png")
    #bot.send_message(-1001182585528, Nome)
    #bot.send_photo(chat_id=-1001182585528, photo=open(nome, 'rb'))

tirinha("mano que que ta acontecendo")


