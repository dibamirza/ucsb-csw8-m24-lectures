# To install PIL, type `pip install pillow` in the console
from PIL import Image

# Open an existing image file
pic = Image.open("butterfly.jpg")

# Write a line of code to get the dimensions of the image
(width, height) = pic.size # 2-tuple
print(f"{width}, {height}")
pix = pic.getpixel((0, 0))
print(f"Top left color: {pix}")

pix = pic.getpixel((pic.size[0] - 1, pic.size[1] - 1 ))
print(f"Bottom righ color: {pix}")

# Write code to manipulate pic
# pic.putpixel((0,0), (100, 100, 100))
# pic.putpixel((1,0), (100, 100, 100))
# pic.putpixel((2,0), (100, 100, 100))
# pic.putpixel((3,0), (100, 100, 100))
# pic.putpixel((4,0), (100, 100, 100))
# pic.putpixel((5,0), (100, 100, 100))
# pic.putpixel((6,0), (100, 100, 100))

# Draws a horizontal line, then extended to a band
# y = height // 2
# for x in range(width): # [0, 1, 2, ..... width - 1]
    # # x is the loop variable 
    # # Inside the for loop, this code is going to run over and over again
    # # print(x)
    # pic.putpixel((x,y), (0, 0, 0))
    # pic.putpixel((x,y+1), (0, 0, 0))
    # pic.putpixel((x,y+2), (0, 0, 0))
    # pic.putpixel((x,y+3), (0, 0, 0))
    # pic.putpixel((x,y+4), (0, 0, 0))

# A better version of drawing a black band
# nested loop
# mid_y = height // 2
# for x in range(width): # [0, 1, 2, ..... width - 1]
#     # x is the loop variable 
#     # Inside the for loop, this code is going to run over and over again
#     # print(x)
#     for y in range(height//2, height): # [height//2 , height// 2 + 1, ... height -1]
#         pic.putpixel((x,y), (100, 100, 100))

# Let's transform the butterfly to grayscale!!!
for x in range(width): # [0, 1, 2, ..... width - 1]
    # x is the loop variable 
    # Inside the for loop, this code is going to run over and over again
    # print(x)
    for y in range(height):
        if x < width //2 and y < height//2:
            (r, g, b) = pic.getpixel((x,y))
            c = int((r + g + b)/3)
            pic.putpixel((x,y), (c, c, c))




# #. Draws a verticall line
# x = width // 2 
# for y in range(height):
#     # x is the loop variable 
#     # Inside the for loop, this code is going to run over and over again
#     # print(x)
#     pic.putpixel((x,y), (0, 0, 0))

print(x) # Outside the loop
# Save the modified image to a new file
pic.save("mygraybutterfly.jpg")

# Run your code 
# see the new file appear on the left panel under "Files"
