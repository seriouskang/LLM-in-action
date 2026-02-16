import pymupdf
import os

pdf_file_path = "./chap04/data/test-paper.pdf"
doc = pymupdf.open(pdf_file_path)

header_height = 80
footer_height = 80
full_text = ''
for page in doc:
    rect = page.rect
    # print(rect)

    header = page.get_text(clip=(0, 0, rect.width, header_height))
    # print(header)
    footer = page.get_text(clip=(0, rect.height - footer_height, rect.width, rect.height))
    # print(footer)
    text = page.get_text(clip=(0, header_height, rect.width, rect.height-footer_height))
    # print(text)
    
    full_text += text + '\n---------------------------------------------------------------\n'
print(full_text)
exit

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0]
# print(pdf_file_name)

txt_file_path = f"chap04/data/{pdf_file_name}_with_preprocessing.txt"
with open(txt_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)