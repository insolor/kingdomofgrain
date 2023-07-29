from typing import Iterable, Mapping

from PIL import Image

from kingdomofgrain import RESOURCES
from kingdomofgrain.resource_loader import load_image


def split_font_image(font_image, char_height) -> Iterable:
    """
    Split long vertical bitmap font image into separate characters
    """
    for y in range(0, font_image.height, char_height):
        box = (0, y, font_image.width, y + char_height)
        yield font_image.crop(box)


# KOI-7 N1 characters from ' ' to 'Ъ'
chars = "".join(map(chr, range(32, 64))) + "юабцдефгхийклмнопярстужвьызшэщчъ" + "ЮАБЦДЕФГХИЙКЛМНОПЯРСТУЖВЬЫЗШЭЩЧЪ"

char_to_image_index = {char: index for index, char in enumerate(chars)}


def map_chars_to_images(font_image) -> Mapping[str, Image.Image]:
    return dict((c, img) for c, img in zip(chars, split_font_image(font_image, 8)))


def join_characters(characters: Iterable[Image.Image]):
    """
    Join passed character images horizontally into one image
    """
    characters = list(characters)
    width = sum(map(lambda c: c.width, characters))
    height = max(map(lambda c: c.height, characters))

    canvas = Image.new("RGB", (width, height))

    x = 0
    for char in characters:
        canvas.paste(char, (x, 0))
        x += char.width

    return canvas


def render_text(font, text):
    """
    Convert text into an image using the given bitmap font
    """
    return join_characters(font[c] for c in text)


def _main():
    font_image = load_image(RESOURCES / "font.png")
    character_mapping = map_chars_to_images(font_image)
    text_image = render_text(character_mapping, "Привет!!!")
    scale_factor = 4
    text_image = text_image.resize(
        size=(text_image.width * scale_factor, text_image.height * scale_factor),
        resample=Image.NONE,
    )
    text_image.show()


if __name__ == "__main__":
    _main()
