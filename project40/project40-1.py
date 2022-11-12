from glob import glob

img_path = r"./original"

img_list = glob(img_path + '/*.jpg')
img_list.extend(glob(img_path + '/*.png'))

print(img_list)
