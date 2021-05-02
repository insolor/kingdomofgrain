from pathlib import Path
from typing import Tuple, Iterator

from PIL import Image
from PIL.ImageFile import ImageFile


def load_image(path) -> ImageFile:
    image = Image.open(path)
    # image.load()
    return image


def load_all_images(path) -> Iterator[Tuple[str, ImageFile]]:
    for file_path in Path(path).glob("*"):
        yield file_path.stem, load_image(file_path)


def main():
    images = dict(load_all_images('resources'))

    for name, image in images.items():
        print(name)
        image.show(title=name)


if __name__ == '__main__':
    main()
