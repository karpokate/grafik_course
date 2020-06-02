from PIL import Image, ImageDraw

image = Image.open('colored_photo.jpg')  # Открываем изображение
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей

for x in range(width):
    for y in range(height):
       r = pix[x, y][0] #узнаём значение красного цвета пикселя
       g = pix[x, y][1] #зелёного
       b = pix[x, y][2] #синего
       sr = (r + g + b) // 3 #среднее значение
       draw.point((x, y), (sr, sr, sr)) #рисуем пиксель

image.save("colored_result.jpg", "JPEG")

#  инверсия
for x in range(width):
   for y in range(height):
      r = pix[x, y][0]
      g = pix[x, y][1]
      b = pix[x, y][2]
      draw.point((x, y), (255 - r, 255 - g, 255 - b))
image.save("colored_result2.jpg", "JPEG")
# инверсия серого
for x in range(width):
  for y in range(height):
      r = pix[x, y][0]
      g = pix[x, y][1]
      b = pix[x, y][2]
      sr = (r + g + b) // 3
      draw.point((x, y), (255 - sr, 255 - sr, 255 - sr))

image.save("colored_result3.jpg", "JPEG")
# более темный

for x in range(width):
    for y in range(height):
        r = pix[x, y][0]
        g = pix[x, y][1]
        b = pix[x, y][2]
        if (r+g+b)>100: #если сумма значений больше 100 , то используем инверисю
            sr = (r + g + b) // 3
            draw.point((x, y), (255-sr, 255-sr, 255-sr))
        else: #иначе обычный оттенок серого
            sr = (r + g + b) // 3
            draw.point((x, y), (sr, sr, sr))
image.save("colored_result4.jpg", "JPEG")