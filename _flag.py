from PIL import Image
import os

if not os.path.exists("small"):
    os.makedirs("small")
if not os.path.exists("medium"):
    os.makedirs("medium")
print("country name")
country_name = str(input())
flag = Image.open("_flag.tga") 

medium_flag = flag.resize((41, 26), Image.LANCZOS)

small_flag = flag.resize((10, 7), Image.LANCZOS)

flag.save("{}.tga".format(country_name))
medium_flag.save("medium/{}.tga".format(country_name))
small_flag.save("small/{}.tga".format(country_name))

#WN8jvcKuTwRSg4R
