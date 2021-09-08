import subprocess


class GangaConnector:
    """

    """
    def __init__(self):
        """

        """
        self.name = ""
        self.script = ""

    def write_script(self, arguments):
        """

        :return:
        """
        arg1 = arguments["date"]
        arg2 = arguments["time"]

        template = open("ganga/template_ganga_script-Ver_1.0.txt", "r")
        new_script = open("ganga/ganga_script-Ver_1.0.py", "w")

        script_lines = template.readlines()
        template.close()

        for ln in script_lines:
            if "##1##" in ln:
                output_line = ln.replace("##1##", "\"" + arg1 + "\"").replace("##2##", "\"" + arg2 + "\"")
            else:
                output_line = ln

            print(output_line)
            new_script.writelines(output_line)

        new_script.close()

    def run(self, arguments):
        """

        :param arguments:
        :return:
        """
        self.write_script(arguments)

        exit_code = subprocess.call('./submitter.sh')
        print(exit_code)




