import os
import os.path

def traversalFolder(path):
    filePaths = []
    #parent:rootdir, dirnames:folder names, filenames:
    for parent, dirnames, filenames in os.walk(path):

        # for dirname in dirnames:
        #     print "parent is:" + parent
        #     print "dirname is " + dirname

        for filename in filenames:
            # print "parent is:" + parent
            # print "filename is" + filename
            # filePath = os.path.join(parent, filename)
            # print filePath
            filePaths.append(os.path.join(parent, filename))
    return filePaths

def formatSize(size, type = None):
    fSize = float(size)
    if type == None or type == "Bytes":
        return "%d Bytes" % (size)
    elif type == "KB":
        return "%f KB" % (fSize / 1024)
    elif type == "MB":
        return "%f MB" % (fSize / 1024 / 1024)
    elif type == "G":
        return "%f G" % (fSize / 1024 / 1024 /1024)
    else:
        return "Type ERROR"

    # try:
    #     # bytes = float(size)
    #     kb = size / 1024
    # except:
    #     print "size format is error"
    #     return "Error"

    # if kb >= 1024:
    #     M = kb / 1024
    #     if M >= 1024:
    #         G = M / 1024
    #         return "%dG" % (G)
    #     else:
    #         return "%dM" % (M)
    # else:
    #     return "%dKB" % (kb)

def getDocSize(path, type = None):
    try:
        size = os.path.getsize(path)
        return formatSize(size, type)
    except Exception as err:
        print err

def getFolderSize(path, type = None):
    try:
        size = os.path.getsize(path)
        return formatSize(size, type)
    except Exception as err:
        print err

if __name__ == '__main__':
    filePaths = traversalFolder("/Users/limingding/Documents/PythonProject/RentProj/")
    for path in filePaths:
        print getDocSize(path, "Bytes")
        print getDocSize(path, "KB")
        print getDocSize(path, "MB")
        print getDocSize(path, "G")

        