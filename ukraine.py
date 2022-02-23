from PIL import Image, ImageColor, ImageDraw, ImageFont

STRONG_AZURE = '#0057b7'
YELLOW = '#ffd700'

with Image.new("RGBA", (400, 400), (255, 255, 255, 0)) as im:

    d = ImageDraw.Draw(im)

    d.pieslice(xy=[0.0, 0.0, 400.0, 400.0],
               start=180.0,
               end=360.0,
               fill=ImageColor.getrgb(STRONG_AZURE))

    d.pieslice(xy=[0.0, 0.0, 400.0, 400.0],
               start=0.0,
               end=180.0,
               fill=ImageColor.getrgb(YELLOW))

    im.save('ukraine.png')


