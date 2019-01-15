import os
from PIL import Image
from pathlib import Path
import tesserocr
import sqlite3
import cv2

bd_path = "D:\OCR_documents\data.db" # Путь к базе данных
path = 'D:/OCR_documents/data' # Каталог со сканированными изображениями товарно-транспортных накладных

# Обрезаем необходимые поля данных, проводим предварительную обработку изображений для улучшения качества распознавания текста
fds = sorted(os.listdir(path))  
for img in fds:
    imgfile = Path(os.path.join(path, img))
    img = Image.open(imgfile)
    #width = img.size[0]
    #height = img.size[1]
    images = []
    
    img1 = img.crop( (3022,410,3097,453) ) #дата
    img1.save('crop_1.jpg')
    img1 = cv2.imread('crop_1.jpg')
    img1 = Image.fromarray(cv2.GaussianBlur(img1,(3,3),0))
    images = images + [img1]

    img2 = img.crop( (3116,410,3195,455) ) #месяц
    img2.save('crop_2.jpg')
    img2 = cv2.imread('crop_2.jpg')
    img2 = Image.fromarray(cv2.GaussianBlur(img2,(3,3),0))
    images = images + [img2]

    img3 = img.crop( (3208,410,3295,456) ) #год
    img3.save('crop_3.jpg')
    img3 = cv2.imread('crop_3.jpg')
    img3 = Image.fromarray(cv2.GaussianBlur(img3,(3,3),0))
    images = images + [img3]

    img4 = img.crop( (3034,358,3291,398) ) #номер накладной
    img4.save('crop_4.jpg')
    img4 = cv2.imread('crop_4.jpg')
    img4 = Image.fromarray(cv2.GaussianBlur(img4,(3,3),0))
    images = images + [img4]

    img5 = img.crop( (3046,308,3289,348) ) #ОКУД
    img5.save('crop_5.jpg')
    img5 = cv2.imread('crop_5.jpg')
    img5 = Image.fromarray(cv2.GaussianBlur(img5,(3,3),0))
    images = images + [img5]

    img6 = img.crop( (523,465,1520,507) ) #грузоотправитель
    img6.save('crop_6.jpg')
    img6 = cv2.imread('crop_6.jpg')
    img6 = Image.fromarray(cv2.GaussianBlur(img6,(3,3),0))
    images = images + [img6]

    img7 = img.crop( (524,533,1520,569) ) #грузополучатель
    img7.save('crop_7.jpg')
    img7 = cv2.imread('crop_7.jpg')
    img7 = Image.fromarray(cv2.GaussianBlur(img7,(3,3),0))
    images = images + [img7]

    img8 = img.crop( (459,593,1526,629) ) #плательщик
    img8.save('crop_8.jpg')
    img8 = cv2.imread('crop_8.jpg')
    img8 = Image.fromarray(cv2.GaussianBlur(img8,(3,3),0))
    images = images + [img8]

    img9 = img.crop( (1214,345,2071,404) ) #Что это (название документа)
    img9.save('crop_9.jpg')
    img9 = cv2.imread('crop_9.jpg')
    img9 = Image.fromarray(cv2.GaussianBlur(img9,(3,3),0))
    images = images + [img9]

    img10 = img.crop( (228,979,492,1018) ) #код 1
    img10.save('crop_10.jpg')
    img10 = cv2.imread('crop_10.jpg')
    img10 = Image.fromarray(cv2.GaussianBlur(img10,(3,3),0))
    images = images + [img10]

    img11 = img.crop( (226,1027,492,1072) ) #код 2
    img11.save('crop_11.jpg')
    img11 = cv2.imread('crop_11.jpg')
    img11 = Image.fromarray(cv2.GaussianBlur(img11,(3,3),0))
    images = images + [img11]

    img12 = img.crop( (523,978,749,1019) ) #номер 1
    img12.save('crop_12.jpg')
    img12 = cv2.imread('crop_12.jpg')
    img12 = Image.fromarray(cv2.GaussianBlur(img12,(3,3),0))
    images = images + [img12]

    img13 = img.crop( (523,1026,746,1072) ) #номер 2
    img13.save('crop_13.jpg')
    img13 = cv2.imread('crop_13.jpg')
    img13 = Image.fromarray(cv2.GaussianBlur(img13,(3,3),0))
    images = images + [img13]

    img14 = img.crop( (766,978,1023,1020) ) #артикул 1
    img14.save('crop_14.jpg')
    img14 = cv2.imread('crop_14.jpg')
    img14 = Image.fromarray(cv2.GaussianBlur(img14,(3,3),0))
    images = images + [img14]

    img15 = img.crop( (768,1028,1023,1075) ) #артикул 2
    img15.save('crop_15.jpg')
    img15 = cv2.imread('crop_15.jpg')
    img15 = Image.fromarray(cv2.GaussianBlur(img15,(3,3),0))
    images = images + [img15]

    img16 = img.crop( (1049,982,1224,1020) ) #количество 1
    img16.save('crop_16.jpg')
    img16 = cv2.imread('crop_16.jpg')
    img16 = Image.fromarray(cv2.GaussianBlur(img16,(3,3),0))
    images = images + [img16]

    img17 = img.crop( (1047,1028,1220,1073) ) #количество 2
    img17.save('crop_17.jpg')
    img17 = cv2.imread('crop_17.jpg')
    img17 = Image.fromarray(cv2.GaussianBlur(img17,(3,3),0))
    images = images + [img17]

    img18 = img.crop( (1244,982,1380,1021) ) #цена 1
    img18.save('crop_18.jpg')
    img18 = cv2.imread('crop_18.jpg')
    img18 = Image.fromarray(cv2.GaussianBlur(img18,(3,3),0))
    images = images + [img18]

    img19 = img.crop( (1244,1029,1377,1072) ) #цена 2
    img19.save('crop_19.jpg')
    img19 = cv2.imread('crop_19.jpg')
    img19 = Image.fromarray(cv2.GaussianBlur(img19,(3,3),0))
    images = images + [img19]

    img20 = img.crop( (1393,987,1734,1022) ) #наименование 1
    img20.save('crop_20.jpg')
    img20 = cv2.imread('crop_20.jpg')
    img20 = Image.fromarray(cv2.GaussianBlur(img20,(3,3),0))
    images = images + [img20]

    img21 = img.crop( (1393,1032,1735,1074) ) #наименование 2
    img21.save('crop_21.jpg')
    img21 = cv2.imread('crop_21.jpg')
    img21 = Image.fromarray(cv2.GaussianBlur(img21,(3,3),0))
    images = images + [img21]

    img22 = img.crop( (1744,980,1932,1022) ) #единица измерения 1
    img22.save('crop_22.jpg')
    img22 = cv2.imread('crop_22.jpg')
    img22 = Image.fromarray(cv2.GaussianBlur(img22,(3,3),0))
    images = images + [img22]

    img23 = img.crop( (1745,1031,1932,1074) ) #единица измерения 2
    img23.save('crop_23.jpg')
    img23 = cv2.imread('crop_23.jpg')
    img23 = Image.fromarray(cv2.GaussianBlur(img23,(3,3),0))
    images = images + [img23]

    img24 = img.crop( (2115,984,2375,1023) ) #количество мест 1
    img24.save('crop_24.jpg')
    img24 = cv2.imread('crop_24.jpg')
    img24 = Image.fromarray(cv2.GaussianBlur(img24,(3,3),0))
    images = images + [img24]

    img25 = img.crop( (2112,1031,2376,1077) ) #количество мест 2
    img25.save('crop_25.jpg')
    img25 = cv2.imread('crop_25.jpg')
    img25 = Image.fromarray(cv2.GaussianBlur(img25,(3,3),0))
    images = images + [img25]

    img26 = img.crop( (2389,984,2655,1024) ) #масса 1
    img26.save('crop_26.jpg')
    img26 = cv2.imread('crop_26.jpg')
    img26 = Image.fromarray(cv2.GaussianBlur(img26,(3,3),0))
    images = images + [img26]

    img27 = img.crop( (2389,1032,2655,1077) ) #масса 2
    img27.save('crop_27.jpg')
    img27 = cv2.imread('crop_27.jpg')
    img27 = Image.fromarray(cv2.GaussianBlur(img27,(3,3),0))
    images = images + [img27]

    img28 = img.crop( (2666,987,2896,1025) ) #сумма 1
    img28.save('crop_28.jpg')
    img28 = cv2.imread('crop_28.jpg')
    img28 = Image.fromarray(cv2.GaussianBlur(img28,(3,3),0))
    images = images + [img28]

    img29 = img.crop( (2667,1031,2898,1077) ) #сумма 2
    img29.save('crop_29.jpg')
    img29 = cv2.imread('crop_29.jpg')
    img29 = Image.fromarray(cv2.GaussianBlur(img29,(3,3),0))
    images = images + [img29]

    img30 = img.crop( (881,2032,1115,2078) ) #отпуск 1
    img30.save('crop_30.jpg')
    img30 = cv2.imread('crop_30.jpg')
    img30 = Image.fromarray(cv2.GaussianBlur(img30,(3,3),0))
    images = images + [img30]

    img31 = img.crop( (1468,2034,1731,2078) ) #отпуск 2
    img31.save('crop_31.jpg')
    img31 = cv2.imread('crop_31.jpg')
    img31 = Image.fromarray(cv2.GaussianBlur(img31,(3,3),0))
    images = images + [img31]

    img32 = img.crop( (2995,1931,3317,1977) ) #принял 1 
    img32.save('crop_32.jpg')
    img32 = cv2.imread('crop_32.jpg')
    img32 = Image.fromarray(cv2.GaussianBlur(img32,(3,3),0))
    images = images + [img32]

    img33 = img.crop( (2902,2139,3314,2188) ) #принял 2
    img33.save('crop_33.jpg')
    img33 = cv2.imread('crop_33.jpg')
    img33 = Image.fromarray(cv2.GaussianBlur(img33,(3,3),0))
    images = images + [img33]
    
# Последовательно распознаем текст на каждом полученном изображении
    text = []
    for img in images:
        tex = tesserocr.image_to_text(img, lang='rus')
        tex = tex.replace(',', '.').replace("\n", '').replace("’", '').replace("'", '').replace('"', '').replace("?", '').replace("‘", '')
        text.append(tex)
    data = text[0]+'.'+text[1]+'.'+text[2]

# Заносим распознанный текст в базу данных (Sqlite)    
    conn = sqlite3.connect(bd_path)
    cursor = conn.cursor()
    albums = [(text[3], data, text[4], text[5], text[6], text[7], text[29], text[30], text[31], text[32])]
    cursor.executemany("INSERT INTO TTN VALUES (?,?,?,?,?,?,?,?,?,?)", albums)
    conn.commit()
    albums = [(text[3], text[9], text[11], text[13], text[15], text[17], text[19], text[21], text[23], text[25], text[27])]
    cursor.executemany("INSERT INTO Products VALUES (?,?,?,?,?,?,?,?,?,?,?)", albums)
    conn.commit()
    albums = [(text[3], text[10], text[12], text[14], text[16], text[18], text[20], text[22], text[24], text[26], text[28])]
    cursor.executemany("INSERT INTO Products VALUES (?,?,?,?,?,?,?,?,?,?,?)", albums)
    conn.commit()
    conn.close()