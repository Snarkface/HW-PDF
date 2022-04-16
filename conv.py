import sys
from fpdf import FPDF
from PIL import Image


def main(output_filename, image_filenames):
    pdf = FPDF()
    pdf.set_image_filter("DCTDecode")
    pdf.set_margin(0)
    pdf.add_page()
    for image_file in image_filenames:
        pdf.image(Image.open(image_file).convert('LA'), h=pdf.eph, w=pdf.epw)
    pdf.output(output_filename)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
