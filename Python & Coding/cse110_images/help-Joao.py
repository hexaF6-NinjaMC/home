from PIL import Image 

image_desert = Image.open('desert.jpg')
image_cat = Image.open('cat.jpg')
image_combined = Image.new('RGB', image_desert.size)
pixels_desert = image_desert.load()
pixels_cat = image_cat.load()
pixels_combined = image_combined.load()
width, height = image_desert.size

# I decided to print the RGB values at top left corner and bottom right corner of those pixels.
# Picture is 800 (0-799) pixels x 600 (0-599) pixels, strating at (0, 0) origin.
color = pixels_cat[0, 0]
color_two = pixels_cat[799, 599]
print(color)
# I added this variable to compare the values.
print(color_two)

# Part of your original code.
# It appears you checked each pixel for SPECIFIC values, but not a set range of values.
# I guess it needed to be more broad?

# for x in range (0, width):
#     for y in range(0, height):
#         (r, g, b) = pixels_desert[x, y]
#         if r <= 150 and g >=215 and b <= 60:
#            pixels_cat[x, y] = pixels_desert[x,y]
#         elif r <=145 and g >=210 and b <=145:
#             pixels_cat[x, y] = pixels_desert[x,y]
#         elif r <=155 and g >=210 and b <=155:
#             pixels_cat[x, y] = pixels_desert[x,y]
#         elif r <=230 and g >=254 and b <=230:
#             pixels_cat[x, y] = pixels_desert[x,y]
#         elif r <=164 and g >=164 and b <=84:
#             pixels_cat[x, y] = pixels_desert[x,y]
#         elif r <=66 and g >=120 and b <=45:
#            pixels_cat[x, y] = pixels_desert[x,y]
#         elif r <=130 and g >=200 and b <=130:
#             pixels_cat[x, y] = pixels_desert[x,y]
#         pixels_combined[x, y] = pixels_cat[x,y]


# Check all pixels for ONE set of RGB values.
# I can help explain how I got this on Zoom. It's a bit complicated.
for x in range (0, width):
    for y in range(0, height):
        (r, g, b) = pixels_cat[x, y]
        if r < 130 and g > 150 and b < 130:
            # Replace pixels_combined at [x, y] with pixels_desert at same point.
            pixels_combined[x, y] = pixels_desert[x, y]
        else:
            # Replace pixels_combined at [x, y] with pixels_cat at same point,
            # or, in other words, "keep the cat."
            pixels_combined[x, y] = pixels_cat[x, y]

        # Remove this line of code. It was part of the problem.
        # You just want to get pixels_combined.
        # ----------------------------------------------
        # pixels_combined[x, y] = pixels_cat[x, y]
        # ----------------------------------------------
    
# Show the combined picture after saving it.
image_combined.save('cat_desert.jpg')
image_combined.show()