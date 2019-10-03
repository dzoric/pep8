import re

def handle_comments(dictionary):
    intMaxLineLength = 79
    intCounter = 0
    dctExport = {}
    for cntr, file in dictionary.items():
        lstHandledComments = []
        for line in file:
            if cntr == intCounter:
                if line.startswith('#'):
                    # find comments with # followed by 
                    # any sign that's not # and add whitespace
                    if re.findall(r'^#[^#]', line):
                        if re.findall(r'^# ', line):
                            pass
                        else:
                            line = line.replace(re.findall(r'^#[^#]', 
                                                           line)[0][0], '# ')
                    # ...any sign followed by # sign
                    elif re.findall(r'[^#]#', line):
                        # whitespace followed by # is ok
                        if re.findall(r'[\s](?=#)', line):
                            pass
                        # text between two # signs
                        elif re.findall(r'#(.*?)#', line):
                            line = line.replace(re.findall(r'#(.*?)#', line)[1], 
                                                ' ' + re.findall(r'#(.*?)#', 
                                                                 line)[1] + ' ')
                    # ...# followed by any non # characters until word boundary
                    elif re.findall(r'#(.*?)\b\n', line):
                        line = line.replace(re.findall(r'#(.*?)\b\n', line)[0],
                                           ' ' + re.findall(r'#(.*?)\b\n', 
                                                            line)[0])
                    # make it find last character before 79th character and add \n#
                    if len(line) > intMaxLineLength:
                        lstMaxLength = []
                        intMaxLenCntr = 0
                        intDivision = len(line)/intMaxLineLength
                        while intMaxLenCntr <= intDivision:
                            if intMaxLenCntr == 0:
                                strSliced = line[intMaxLineLength*intMaxLenCntr:
                                                 intMaxLineLength*(intMaxLenCntr+
                                                                   1)]
                                lstMaxLength.append(strSliced)
                                intMaxLenCntr += 1
                            elif intMaxLenCntr == 1:
                                strSliced = line[intMaxLineLength*intMaxLenCntr:
                                                 (intMaxLineLength-1)*
                                                 (intMaxLenCntr+1)]
                                lstMaxLength.append(strSliced)
                                intMaxLenCntr += 1
                            else:
                                strSliced = line[(intMaxLineLength-1)*
                                                 intMaxLenCntr:
                                                 (intMaxLineLength-2)*
                                                 (intMaxLenCntr+1)]
                                lstMaxLength.append(strSliced)
                                intMaxLenCntr += 1
                        line = "\n# ".join(lstMaxLength)
                lstHandledComments.append(line)
            dctHandledComments = {intCounter: lstHandledComments}
        intCounter += 1
        dctExport.update(dctHandledComments)
    return dctExport
