from src.ExcelReader import ExcelReader
import os


def get_file_names(input_file):

    f_in = open(input_file, 'r', encoding="utf-8-sig")
    result = []

    counter = 1
    for line in f_in:
        clean_line = line.strip().replace("\"", "")
        file_name = clean_line.split('\\')[-1]
        file_path = clean_line.split(file_name)[0]
        file_ext = file_name.split('.')[-1]
        new_file_name = "autovia_input_" + str(counter) + "." + file_ext
        result.append({"file_path": file_path, "file_name": new_file_name, "file_ext": file_ext})

        os.rename(clean_line, file_path + new_file_name)

        counter += 1

    return result


if __name__ == '__main__':

    # 1 - Clean the input file list

    step = 3

    if step == 1:
        data = get_file_names("input_files_paths.txt")
        print(data)

        # 1. check if file contains the needed sheet
        # ANG-FOP-18 = various incidents - non accidents
        # ANG-FOP-19 = accidents

        rxl = ExcelReader("ANG-FOP-19")
        for info in data:
            infile = info["file_path"] + info["file_name"]
            has_sheet = rxl.look_for_sheet(infile)
            print(info["file_name"], has_sheet)
            info["ANG-FOP-19"] = int(has_sheet)

        rxl.sheet = "ANG-FOP-18"

        for info in data:
            infile = info["file_path"] + info["file_name"]
            has_sheet = rxl.look_for_sheet(infile)
            print(info["file_name"], has_sheet)
            info["ANG-FOP-18"] = int(has_sheet)

        print(data)

    elif step == 2:

        rxl = ExcelReader("ANG-FOP-19")
        rxl.combine_sheets('input/input_files.json')

    elif step == 3:

        rxl = ExcelReader("ANG-FOP-18")
        rxl.combine_sheets('input/input_files.json')

    else:
        print("All done")
