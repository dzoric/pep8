import re


def handle_tabs(dictionary):
    intCounter = 0
    dctExport = {}
    for cntr, file in dictionary.items():
        lstNoTab = []
        for line in file:
            if cntr == intCounter:
                rexTabTo4Space = re.sub(r'\t', '    ', line)
                lstNoTab.append(rexTabTo4Space)
            dctNoTab = {intCounter: lstNoTab}
        intCounter += 1
        dctExport.update(dctNoTab)
    return dctExport
