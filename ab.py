import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_image(img_path, name=''):
    img = mpimg.imread(img_path)
    plt.figure()
    plt.imshow(img)
    plt.title(name)

show_image("./data/images/jz/jz2.jpg")

