import re

def handle_imports(dictionary):
    intCounter = 0
    dctExport = {}
    for cntr, file in dictionary.items():
        lstSeparateImports = []
        dctSepImports = {}
        for line in file:
            if cntr == intCounter:
                if re.findall(r'\bimport\b( \w+),', line):
                    line = re.sub(r',', '\nimport', line)
                lstSeparateImports.append(line)
            dctSepImports = {intCounter: lstSeparateImports}
        intCounter += 1
        dctExport.update(dctSepImports)
    return dctExport


