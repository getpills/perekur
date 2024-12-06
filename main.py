from PIL import Image

# Открываем изображение
image = Image.open('img.jpg')
xsize =40
ysize =30
# Преобразуем изображение в градации серого
gray_image = image.convert('L')
threshold = 120
bw_image = gray_image.point(lambda x: 255 if x > threshold else 0, '1')

bw_image = bw_image.resize((xsize*3-1, ysize*6-2), Image.Resampling.LANCZOS)
bw_image
pixels = bw_image.load()
width, height = bw_image.size
far = [[0 for _ in range(ysize)] for _ in range(xsize)]

for y in range(height):
  for x in range(width):
    v = pixels[x, y]
    
    # Здесь вы можете делать что-нибудь с каждым пикселем 
    # Например:
   
    color = v/255;
    #try to guess 
    if (y%6 ==5 or y%6==0 or x%3==0):
      continue
    num=0;
    xpos = x%3
    ypos = y%6
    power = ypos-1 + 4*(xpos-1)
    
    mainposx = x//3
    mainposy = y//6
    far[mainposx][mainposy] += color*(2**power)
    


for y in range(ysize):
  line = ""
  for x in range(xsize):
    # Здесь вы можете выполнять действия с каждым элементом far
    line+=chr(10240+int(far[x][y]))
  print(line)
