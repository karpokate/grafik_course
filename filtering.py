from PIL import  Image
from PIL import ImageFilter
from pylab import *

image  = Image.open('man_bgw.jpg')
figure (figsize=(15,15))
titles = ["Original", "Contour", "Detail", "Edge Enhance", "Edge Enhance More", "Emboss", "Find Edges", "Lowpass1", "Lowpass 2", "Sharpen"]
    # ,"Custom Filter 1", "Custom Filter 2"]

img1 = image.filter (ImageFilter.CONTOUR)
img2 = image.filter (ImageFilter.DETAIL)
img3 = image.filter (ImageFilter.EDGE_ENHANCE)
img4 = image.filter (ImageFilter.EDGE_ENHANCE_MORE)
img5 = image.filter (ImageFilter.EMBOSS)
img6 = image.filter (ImageFilter.FIND_EDGES)
img7 = image.filter (ImageFilter.SMOOTH)
img8 = image.filter (ImageFilter.SMOOTH_MORE)
img9 = image.filter (ImageFilter.SHARPEN)


commands = [image,img1,img2, img3, img4, img5, img6, img7, img8, img9]

def subplotRes (image, number) :
    subplot(3,4,number+1)
    plt.imshow(image[number])
    plt.title(titles[number])


def main () :
    for number in range(len(titles)) :
        subplotRes(commands,number)
    plt.show()

if __name__ == "__main__":
    main()