import re


def handle_comments(dictionary):
    intMaxLineLength = 79
    intCounter = 0
    dctExport = {}
    for cntr, file in dictionary.items():
        lstHandledComments = []
        dctHandledComments = {}
        for line in file:
            if cntr == intCounter:
                if line.startswith('#') or re.findall(r'\s#', line):
                    # find comments with # followed by 
                    # any sign that's not # and add whitespace
                    if re.findall(r'^#[^#]', line):
                        if re.findall(r'^# ', line):
                            pass
                        else:
                            line = line.replace(re.findall(r'^#[^#]', 
                                                           line)[0][0], '# ')
                    # ...any sign that is not # followed by # sign
                    elif re.findall(r'[^#]#', line):
                        # whitespace followed by # is not ok
                        if re.findall(r'[\s](?=#)', line):
                            if re.findall(r'[\s]#(\w+)', line):
                                line = line.replace(re.findall(r'(?<=\s)#(?=\w+)',
                                                         line)[0], '# ')
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
                            if line.startswith("#"):
                                if intMaxLenCntr == 0:
                                    strSliced = line[intMaxLineLength*
                                                     intMaxLenCntr:
                                                     intMaxLineLength*
                                                     (intMaxLenCntr+1)]
                                    lstMaxLength.append(strSliced)
                                    intMaxLenCntr += 1
                                elif intMaxLenCntr == 1:
                                    strSliced = line[intMaxLineLength*
                                                     intMaxLenCntr:
                                                     (intMaxLineLength-1)*
                                                     (intMaxLenCntr+1)]
                                    strSliced = '# ' + strSliced
                                    lstMaxLength.append(strSliced)
                                    intMaxLenCntr += 1
                                else:
                                    strSliced = line[(intMaxLineLength-1)*
                                                     intMaxLenCntr:
                                                     (intMaxLineLength-1)*
                                                     (intMaxLenCntr+1)]
                                    strSliced = '# ' + strSliced
                                    lstMaxLength.append(strSliced)
                                    intMaxLenCntr += 1
                            elif re.findall('\s#', line):
                                rexIndentation = re.findall(r'\s+(?=#)', line)[0]
                                print rexIndentation
                                if intMaxLenCntr == 0:
                                    strSliced = line[intMaxLineLength*
                                                     intMaxLenCntr:
                                                     intMaxLineLength*
                                                     (intMaxLenCntr+1)]
                                    lstMaxLength.append(strSliced)
                                    intMaxLenCntr += 1
                                elif intMaxLenCntr == 1:
                                    strSliced = line[intMaxLineLength*
                                                     intMaxLenCntr:
                                                     (intMaxLineLength-1)*
                                                     (intMaxLenCntr+1)]
                                    strSliced = rexIndentation + '# ' + strSliced
                                    lstMaxLength.append(strSliced)
                                    intMaxLenCntr += 1
                                else:
                                    strSliced = line[(intMaxLineLength-1)*
                                                     intMaxLenCntr:
                                                     (intMaxLineLength-1)*
                                                     (intMaxLenCntr+1)]
                                    strSliced = rexIndentation + '# ' + strSliced
                                    lstMaxLength.append(strSliced)
                                    intMaxLenCntr += 1
                        line = "\n".join(lstMaxLength)
                lstHandledComments.append(line)
            dctHandledComments = {intCounter: lstHandledComments}
        intCounter += 1
        dctExport.update(dctHandledComments)
    return dctExport

