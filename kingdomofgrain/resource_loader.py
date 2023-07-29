from pathlib import Path
from typing import Tuple, Iterator

from PIL import Image
from PIL.ImageFile import ImageFile

from kingdomofgrain import RESOURCES


def load_image(path) -> Image:
    image = Image.open(path)
    return image


def load_all_images(path: Path) -> Iterator[Tuple[str, ImageFile]]:
    """
    Load all the images from the given directory (will fail if there is a file which is not an image)
    """
    for file_path in path.glob("*"):
        yield file_path.stem, load_image(file_path)


def _main():
    images = dict(load_all_images(RESOURCES))

    for name, image in images.items():
        print(name)
        image.show(title=name)


if __name__ == "__main__":
    _main()
