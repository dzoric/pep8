import re

def handle_multi_line_comments(dictionary):
    intMaxLineLength = 79
    intCounter = 0
    dctExport = {}
    for cntr, file in dictionary.items():
        lstHandledMlComments = []
        intStartIndex = None
        intEndIndex = None
        for line in file:
            if cntr == intCounter:
                if re.findall(r'"""(\w+)', line):
                    intStartIndex = file.index(line)
                if re.findall(r'"""\n', line):
                    intEndIndex = file.index(line)
                lstHandledMlComments.append(line)
                if intStartIndex is not None and intEndIndex is not None:
                    lstMlComm = lstHandledMlComments[intStartIndex:(intEndIndex+1)]
                    lstJoinedMlComm = "".join(lstMlComm)
                    # Every joined element has \n at the end that needs to be
                    # replaced, every but last one, thus:
                    lstJoinedMlComm = lstJoinedMlComm.replace("\n", " ")
                    lstJoinedMlComm = lstJoinedMlComm + "\n"
                    lstJoinedMlComm = lstJoinedMlComm.replace(' \n', '\n')
                    lstHandledMlComments[intStartIndex] = lstJoinedMlComm
                    del lstHandledMlComments[(intStartIndex+1):(intEndIndex+1)]
                    intStartIndex = None
                    intEndIndex = None
                intItemIndex = 0
                for item in lstHandledMlComments:
                    if item.startswith('"""') and item.endswith('"""\n') and \
                    len(item) > intMaxLineLength:
                        intItemIndex = lstHandledMlComments.index(item)
                        lstMaxLength = []
                        intMaxLenCntr = 0
                        intDivision = len(item)/intMaxLineLength
                        while intMaxLenCntr <= intDivision:
                            if intMaxLenCntr == 0:
                                strSliced = item[intMaxLineLength*intMaxLenCntr:
                                                 intMaxLineLength*(intMaxLenCntr+
                                                                   1)]
                                lstMaxLength.append(strSliced)
                                intMaxLenCntr += 1
                            elif intMaxLenCntr == 1:
                                strSliced = item[intMaxLineLength*intMaxLenCntr:
                                                 (intMaxLineLength-1)*
                                                 (intMaxLenCntr+1)]
                                lstMaxLength.append(strSliced)
                                intMaxLenCntr += 1
                            else:
                                strSliced = item[(intMaxLineLength-1)*
                                                 intMaxLenCntr:
                                                 (intMaxLineLength-1)*
                                                 (intMaxLenCntr+1)]
                                lstMaxLength.append(strSliced)
                                intMaxLenCntr += 1
                        item = "\n".join(lstMaxLength)
                    lstHandledMlComments[intItemIndex] = item
            dctHandledMlComments = {intCounter: lstHandledMlComments}
        intCounter += 1
        dctExport.update(dctHandledMlComments)
    return dctExport
