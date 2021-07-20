import PyPDF2
import os
from tika import parser


def open_pdfs_ver0(file_list):

    result = []

    for item in file_list:
        info = {}
        file_path = 'data/' + item
        file_name = item.split('.pdf')[0]

        pdf_input_object = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_input_object)
        pdf_info = pdf_reader.getDocumentInfo()

        info["file_name"] = file_name
        info["content"] = pdf_info['/Title']

        result.append(info)

        info_content = info["content"].split('-')
        pretty_stdout = file_name + '\t' + info_content[0] + '\t' + info_content[1]

        print(pretty_stdout)


def open_pdfs_ver1(input_file):

    raw = parser.from_file(input_file)
    print(raw['content'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    input_file_list = list(filter(lambda x: x.endswith('.pdf'), os.listdir('data')))

    open_pdfs_ver0(input_file_list)

