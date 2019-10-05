import os
import shutil
from ImportHandler.ImportHandler import *
from NewLineEnd.NewLineEnd import *
from TabHandler.TabHandler import *
from CommentHandler.CommentHandler import *
from CommentHandler.MultilineCommentHandler import *

# example: C:\\Users\\UserName\\Desktop\\Test
strSource = 'Your source folder path here'
strDestination = 'Your destination folder path here'

shutil.copytree(strSource, strDestination)

lstFiles = []
strSuffx = '.py'
# r=root, d=directories, f = files
for r, d, f in os.walk(strDestination):
    for file in f:
        if file.endswith(strSuffx):
            lstFiles.append(os.path.join(r, file))

dctCntrLines = {}
intCounter = 0


for file in lstFiles:
    file_object = open(file, "r")
    dctCntrFiles = {intCounter: [cntr for cntr in file_object.readlines()]}
    dctCntrLines.update(dctCntrFiles)
    intCounter += 1
    file_object.close()

dctSeparateImports = handle_imports(dctCntrLines)
dctNewLine = add_new_line(dctSeparateImports)
dctFixedTabs = handle_tabs(dctNewLine)
dctFixedComments = handle_comments(dctFixedTabs)

# Multiline comment handler probably won't work, but you can try by uncommenting
# and changing dctFixedComments.items() with dctFixMlComments.items()

# dctFixMlComments = handle_multi_line_comments(dctFixedComments)


for file in lstFiles:
    for cntr, line in dctFixedComments.items(): #here
        if lstFiles.index(file) == cntr:
            file_object = open(file, "w")
            file_object.writelines([str(cntr) for cntr in line])
            file_object.close()
