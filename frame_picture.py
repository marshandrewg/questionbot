from PIL import Image, ImageOps, ImageDraw, ImageSequence
import PIL
import io



foreground = Image.open('confetti_2.gif')
h,w = foreground.size

background = Image.open('512.png').convert("RGBA")
# background = background.resize((h,w))
background = ImageOps.pad(background, (h,w), color='#FFFFFF', centering=(0.5,0.5))
# background = ImageOps.grayscale(background)
# background.save('background_greyscale.png', format="png")
# background = Image.open('background_greyscale.png').convert("RGBA") 

from PIL import Image, ImageOps
# A list of the frames to be outputted
def animate_foreground():
    frames = []
    # Loop over each frame in the animated image
    for frame in ImageSequence.Iterator(foreground):
        # Draw the text on the frame
        # frame.show()
        # com1 = Image.alpha_composite(frame, foreground)
        frame.convert("RGBA")
        frame.save("test2.png", format="png")

        # NEEDS CONVERT RGBA
        framePng = Image.open('test2.png').convert("RGBA")

        h,w = framePng.size
        background_copy = background.copy()
        background_copy.paste(framePng, mask=framePng)
        # framePng.paste(foreground, mask=framePng)

        background_copy.save('test3.png')
        frames.append(background_copy)
    # Save the frames as a new image
    frames[0].save('out.gif', save_all=True, append_images=frames[1:], loop=0)
