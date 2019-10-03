import os
import shutil
from TabHandler.TabHandler import handle_tabs
from CommentHandler.CommentHandler import *
from CommentHandler.MultilineCommentHandler import *

strSource = 'C:\\Users\\Dragon\\Desktop\\PythonCourse'
strDestination = 'C:\\Users\\Dragon\\Desktop\\new'

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

dctFixedTabs = handle_tabs(dctCntrLines)
dctFixedComments = handle_comments(dctFixedTabs)
# dctFixMlComments = handle_multi_line_comments(fix_comments) not working


for file in lstFiles:
    for cntr, line in dctFixedComments.items():
        if lstFiles.index(file) == cntr:
            file_object = open(file, "w")
            file_object.writelines([str(cntr) for cntr in line])
            file_object.close()
