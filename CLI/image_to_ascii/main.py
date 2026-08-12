from PIL import Image
from pathlib import Path

def main():
    scale = "@%#*+=-:. "
    text = ''

    img_input = Path() / 'image input'
    img_output = Path() / 'image output'

    img = Image.open(img_input / 'linux_penguin.jpg')

    img_jpg_bw = img.convert(mode='L').save(img_input / 'imgbw.jpg')
    img_jpg_bw = Image.open(img_input / 'imgbw.jpg')
    size = (300, 100)    #Recomendado uma proporção de 3:1
    img_jpg_bw = img_jpg_bw.resize(size)

    xy = img_jpg_bw.size  #Retorna uma tupla com a dimensão da imagem (x, y)

    for y in range(xy[1]):
        for x in range(xy[0]):
            rgb = img_jpg_bw.getpixel(xy=(x, y))
            value= int(rgb/25.5)
            if value == 0:
                value = 1
            value_to_ascii = scale[value-1]
            text += value_to_ascii
        text += '\n'

    with open(img_output / 'image_converted.txt', 'w', encoding='utf8') as file:
        file.write(text)

    print(text)


if __name__ == '__main__':
    main()