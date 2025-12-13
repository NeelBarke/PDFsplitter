from PyPDF2 import PdfReader, PdfWriter
import os
#PyPDF2 library required to run,so install it first!

INPUT_PDF = "" #file path of the combined pdf
OUTPUT_FOLDER = "split_files"
PAGES_PER_REPORT = 1 #how many pages per pdf after splitting

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

reader = PdfReader(INPUT_PDF)
total_pages = len(reader.pages)

report_index = 1

for start in range(0, total_pages, PAGES_PER_REPORT):
    writer = PdfWriter()

    end = min(start + PAGES_PER_REPORT, total_pages)
    for page_num in range(start, end):
        writer.add_page(reader.pages[page_num])

    out_path = os.path.join(OUTPUT_FOLDER, f"file{report_index}.pdf")
    with open(out_path, "wb") as f:
        writer.write(f)

    print(f"Created {out_path}")
    report_index += 1

print("Done splitting!")
