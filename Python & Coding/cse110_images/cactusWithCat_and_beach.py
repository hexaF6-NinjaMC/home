from PIL import Image
import os
clear = lambda: os.system("cls")
clear()

image_background = Image.open("cactus.jpg")
image_foreground = Image.open("cat_small.jpg")

image_combined = Image.new("RGB", image_background.size)
pixels_combined = image_combined.load()

pixels_background = image_background.load()
pixels_foreground = image_foreground.load()

(width, height) = image_background.size

for y in range(0, height):
    for x in range(0, width):
        (r1, g1, b1) = pixels_foreground[x, y]
        (r2, g2, b2) = pixels_background[x,y]
        if g1 > 200 and (r1, b1) < (182, 200):
            pixels_combined[x, y] = (r2, g2, b2)
        else:
            pixels_combined[x, y] = (r1, g1, b1)

        (r3, g3, b3) = pixels_combined[x, y]
        pixels_combined[x, y] = (r3, g3, b3)

image_combined.show()

image_combined.save("cactus_with_cat.jpg")

image_background_two = Image.open("beach.jpg")
image_foreground_two = Image.open("cactus_with_cat.jpg")

image_combo_two = Image.new("RGB", image_background_two.size)
pixels_combo_two = image_combo_two.load()

pixels_background_two = image_background_two.load()
pixels_foreground_two = image_foreground_two.load()

(width_two, height_two) = image_background_two.size

for y in range(0, height_two):
    for x in range(0, width_two):
        (r1, g1, b1) = pixels_foreground_two[x, y]
        (r2, g2, b2) = pixels_background_two[x,y]
        if g1 > 200 and (r1, b1) < (182, 200):
            pixels_combo_two[x, y] = (r2, g2, b2)
        else:
            pixels_combo_two[x, y] = (r1, g1, b1)

        (r3, g3, b3) = pixels_combo_two[x, y]
        new_red = r3 + 50
        new_green = g3 + 50
        new_blue = b3 + 50
        pixels_combo_two[x, y] = (new_red, new_green, new_blue)

image_combo_two.show()

image_combo_two.save("beach_with_cactus_with_cat.jpg")
