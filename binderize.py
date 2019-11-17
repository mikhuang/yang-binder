import sys
import json
import io

from PyPDF2 import PdfFileMerger, PdfFileReader

from BinderSetting import BinderSetting


def binderize(settings):
    # download sources
    buffers = settings.buffer_resources()

    # combine
    pdf_merged_buffer = io.BytesIO()
    merger = PdfFileMerger()
    for buffer in buffers:
        merger.append(PdfFileReader(buffer))
    merger.write(pdf_merged_buffer)

    # # Option 1:
    # # Return the content of the buffer in an HTTP response (Flask example below)
    # response = make_response(pdf_merged_buffer.getvalue())
    # # Set headers so web-browser knows to render results as PDF
    # response.headers['Content-Type'] = 'application/pdf'
    # response.headers['Content-Disposition'] = \
    #     'attachment; filename=%s.pdf' % 'Merged PDF'
    # return response

    # save
    with open("output/merged.pdf", "wb") as fp:
        fp.write(pdf_merged_buffer.getvalue())


def main():
    settings = open(filename, "r")
    binderize(BinderSetting(json.load(settings)))


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "sample.json"
    main()
