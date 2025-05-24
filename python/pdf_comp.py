from pypdf import PdfReader, PdfWriter

reader = PdfReader('C:\\Users\\jm\\ac\\7000_各種Doc\\1126履歴書\\20240113_FUJITSU\\内定\\提出資料\\20240601_劉積民_内定承諾書.pdf')
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

for page in writer.pages:
    # ⚠️ This has to be done on the writer, not the reader!
    page.compress_content_streams(level=9)  # This is CPU intensive!

with open('C:\\Users\\jm\\ac\\7000_各種Doc\\1126履歴書\\20240113_FUJITSU\\内定\\提出資料\\20240601_劉積民_内定承諾書1.pdf', "wb")as f:
    writer.write(f)