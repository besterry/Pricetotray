from os import name
import requests
from infi.systray import SysTrayIcon
from PIL import Image, ImageDraw,ImageFont
import time

image= "pil_text.ico"
n=1
while True:
    # создание иконки
    img = Image.new('RGBA', (50, 50), color = (0, 0, 0, 1))  # color background =  white  with transparency
    d = ImageDraw.Draw(img)
    d.rectangle([(0, 100), (50, 50)], fill=None, outline=None)  #  color = blue

    ##https://bablofil.com/binance-api/
    ##https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
    r = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    r1=str(r.text)

    #{"symbol":"BTCUSDT","price":"57476.92000000"}
    newstr = r1.replace(('{"symbol":"BTCUSDT","price":"'), "")
    parts=newstr.split('.')
    price=parts[0]


    #добавление текста на иконку
    font_type  = ImageFont.truetype("arial.ttf", 45)    
    d.text((0,0), f"{price}", fill=(255,255,0), font = font_type)    
    img.save(image)

    # иконка в трей
    if n==1:
        systray = SysTrayIcon(image, price)
        systray.start()
    else:
        systray.update(icon=image, hover_text = price)
    time.sleep(5)
    n+=1
systray.shutdown()