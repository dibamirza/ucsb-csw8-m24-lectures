# To install PIL, type `pip install pillow` in the console
from PIL import Image

def firstDraw():
    pic = Image.new('RGB', (200, 400), (255, 255, 255))
    # write some code
    # for loop!!!!
    for x in range(pic.size[0]):
        # x is the loop variable 
        # Inside the for loop, this code is going to run over and over again
        print(x)
        pic.putpixel((x,0), (100, 100, 100))

    # pic.putpixel((0,0), (100, 100, 100))
    # pic.putpixel((1,0), (100, 100, 100))
    # pic.putpixel((2,0), (100, 100, 100))
    # pic.putpixel((3,0), (100, 100, 100))
    # pic.putpixel((4,0), (100, 100, 100))
    # pic.putpixel((5,0), (100, 100, 100))
    # pic.putpixel((6,0), (100, 100, 100))
    # pic.putpixel((199, 399), (255, 0, 0))
    # save the image
    pic.save("mycanvas.jpg")


firstDraw()

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

y = height // 2

for x in range(pic.size[0]):
    # x is the loop variable 
    # Inside the for loop, this code is going to run over and over again
    # print(x)
    pic.putpixel((x,y), (0, 0, 0))


x = width // 2 
for y in range(height):
    # x is the loop variable 
    # Inside the for loop, this code is going to run over and over again
    # print(x)
    pic.putpixel((x,y), (0, 0, 0))

print(x) # Outside the loop
# Save the modified image to a new file
pic.save("mybutterfly.jpg")

# Run your code 
# see the new file appear on the left panel under "Files"
