from typing import Iterable, Mapping

from PIL import Image

from resource_loader import load_image


def split_font_image(font_image, char_height) -> Iterable:
    for y in range(0, font_image.height, char_height):
        box = (0, y, font_image.width, y + char_height)
        yield font_image.crop(box)


chars = ''.join(map(chr, range(32, 64))) + \
    "юабцдефгхийклмнопярстужвьызшэщчь" \
    "ЮАБЦДЕФГХИЙКЛМНОПЯРСТУЖВЬЫЗШЭЩЧЬ"


def map_chars_to_images(font_image) -> Mapping[str, Image.Image]:
    return dict((c, img) for c, img in zip(chars, split_font_image(font_image, 8)))


def join_characters(characters: Iterable[Image.Image]):
    """
    Join passed character images horizontally into one image
    """
    characters = list(characters)
    width = sum(map(lambda c: c.width, characters))
    height = max(map(lambda c: c.height, characters))

    canvas = Image.new('RGB', (width, height))

    x = 0
    for char in characters:
        box = (x, 0)
        canvas.paste(char, box)
        x += char.width

    return canvas


def render_text(font, text):
    return join_characters(font[c] for c in text)


def main():
    font_image = load_image("resources/font.png")
    character_mapping = map_chars_to_images(font_image)
    text_image = render_text(character_mapping, "Привет!!!")
    scale_factor = 4
    text_image = text_image.resize(size=(text_image.width*scale_factor, text_image.height*scale_factor),
                                   resample=Image.NONE)
    text_image.show()


if __name__ == '__main__':
    main()
