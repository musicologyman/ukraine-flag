import argparse

from PIL import Image, ImageColor, ImageDraw

STRONG_AZURE = '#0057b7'
YELLOW       = '#ffd700'

def process_args():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-o', '--output', default='ukraine.png')
    parser.add_argument('-w', '--width', type=int, default=400)
    parser.add_argument('-h', '--height', type=int, default=400)

    return parser.parse_args()

def main():

    args = process_args()

    width = args.width
    height = args.height
    output_filename = args.output

    with Image.new("RGBA", (width, height), (255, 255, 255, 0)) as im:

        d = ImageDraw.Draw(im)

        horizontal_center = width // 2
        vertical_center   = height // 2
        diameter          = min(width, height)
        radius            = diameter // 2
        left_boundary     = horizontal_center - radius
        right_boundary    = horizontal_center + radius
        top_boundary = vertical_center - radius
        bottom_boundary = vertical_center + radius
        bounds = [(left_boundary, top_boundary), 
                  (right_boundary, bottom_boundary)]

        d.pieslice(xy=bounds, 
                   start=180.0,
                   end=360.0,
                   fill=ImageColor.getrgb(STRONG_AZURE))

        d.pieslice(xy=bounds,
                   start=0.0,
                   end=180.0,
                   fill=ImageColor.getrgb(YELLOW))

        im.save(output_filename)

if __name__ == '__main__':
    main()


