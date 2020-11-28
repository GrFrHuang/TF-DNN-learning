from PIL import Image, ImageFilter
import cv2
import matplotlib.pyplot as plt

# % matplotlib inline

imgMode = 'RGB'
imgSize = 500
imgPath = '../../assets/imgAssets/testImg1.jpg'
img = Image.open(imgPath)

if img.mode != imgMode:
    img = img.convert(imgMode)  # 读取图片的过程中如果遇到非'RGB'就转换格式

if img.size != (imgSize, imgSize):
    img.resize((imgSize, imgSize), Image.NEAREST)  # 默认的插值算法是Image.NEAREST
    print('debug', img)

plt.imshow(img)  # 显示图片
plt.axis('on')  # 不显示坐标轴
plt.show()

plt.savefig('test.png')
