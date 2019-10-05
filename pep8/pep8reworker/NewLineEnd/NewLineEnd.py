def add_new_line(dictionary):
    intCounter = 0
    dctExport = {}
    for cntr, file in dictionary.items():
        if file[-1] != "\n":
            file.append("\n")
            dctNewLine = {intCounter: file}
        intCounter += 1
        dctExport.update(dctNewLine)
    return dctExport
