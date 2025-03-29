
import datetime
import os.path


def write_log(text, file_name, folder_name):
    if file_name == "" and folder_name == "":
        year = datetime.date.today().year
        month = datetime.date.today().month
        day = datetime.date.today().day

        if not os.path.isdir("{}".format(year)):
            os.mkdir("{}".format(year))
        if not os.path.isdir("{}/{}".format(year, month)):
            os.mkdir("{}/{}".format(year, month))

        with open("{}/{}/{}.txt".format(year, month, day), "a+") as file:
            file.write(text+"\n")

    else:
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        with open("{}/{}".format(folder_name, file_name), "a+") as file:
            file.write(text+"\n")


write_log("Hello", "log", "Hidayet")
write_log("Hello", "", "")

