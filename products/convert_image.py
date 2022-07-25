import datetime
from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image


def Convert2jpg(self, saveName):
    """
    Convert the image to a jpg file.
    """
    Current_Date = datetime.datetime.today().strftime("%d-%b-%Y")
    convert2jpg_filename = (
        "%s.jpg" % f'"lkm-creations_"{saveName}"_"{str(Current_Date)}'
    )  # create a filename
    convert2jpg_image = Image.open(self.image)
    if convert2jpg_image.mode in ("RGBA", "LA"):
        background = Image.new(
            convert2jpg_image.mode[:-1], convert2jpg_image.size, "#fff"
        )
        background.paste(convert2jpg_image, convert2jpg_image.split()[-1])
        convert2jpg_image = background
    convert2jpg_image.thumbnail((800, 800))
    convert2jpg_image_io = BytesIO()
    convert2jpg_image.save(
        convert2jpg_image_io, format="JPEG", quality=100
    )
    self.image.save(
        convert2jpg_filename,
        ContentFile(convert2jpg_image_io.getvalue()),
        save=False,
    )


def Convert2webp(self, saveName):
    """
    Convert the image to webp format and save it to the database.
    """
    Current_Date = datetime.datetime.today().strftime("%d-%b-%Y")
    convert2webp_filename = (
        "%s.webp" % f'"lkm-creations_"{saveName}"_"{str(Current_Date)}'
    )
    convert2webp_image = Image.open(self.image)
    convert2webp_image.thumbnail((800, 800))
    convert2webp_image_io = BytesIO()
    convert2webp_image.save(
        convert2webp_image_io, format="WEBP", quality=90
    )
    self.image_preferred.save(
        convert2webp_filename,
        ContentFile(convert2webp_image_io.getvalue()),
        save=False,
    )


def Convert2png(self, saveName):
    """
    Convert the image to a png file.
    """
    Current_Date = datetime.datetime.today().strftime("%d-%b-%Y")
    convert2png_filename = (
        "%s.png" % f'"lkm-creations_"{saveName}"_"{str(Current_Date)}'
    )  # create a filename
    convert2png_image = Image.open(self.image)
    convert2png_image.thumbnail((900, 600))
    convert2png_image_io = BytesIO()
    convert2png_image.save(convert2png_image_io, format="PNG", quality=100)
    self.image.save(
        convert2png_filename,
        ContentFile(convert2png_image_io.getvalue()),
        save=False,
    )
