import fitz
import sys

pdf_path = "/home/giosue/Scrivania/Elettronica digitale/original notes analogica. pdf"
try:
    doc = fitz.open(pdf_path)
    for i in range(25, min(30, len(doc))):
        page = doc.load_page(i)
        pix = page.get_pixmap(dpi=150)
        out_path = f"page_{i+1}.png"
        pix.save(out_path)
        print(f"Saved {out_path}")
    print(f"Total pages in document: {len(doc)}")
except Exception as e:
    print(f"Error: {e}")