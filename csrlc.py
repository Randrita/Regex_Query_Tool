import csv
def replace_csv(path,origin_word,replaced_word):
    text = open(path, "r")
    text = ''.join([i for i in text])
    save=os.listdir("G:\\regextester\\regex yo\\static\\db2")
    text = text.replace('{}'.format(origin_word),'{}'.format(replaced_word))
    if save:
        last_csv, extension = save[-1].split(".")
        csv_nm = int(last_csv)+1
    else:
        csv_nm=0
    file_path = os.path.join("static\\db2", str(csv_nm) + "." + extension)
    x = open(file_path,"w")
    x.writelines(text)
    x.close()
    return file_path