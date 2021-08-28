import os

DIR = ''

def removeFile(filename):
    try:
        os.remove(DIR + filename)
    except:
        print('Failed to remove: ' + filename)
        return
    print('Removed: ' + filename)


allFiles = os.listdir(DIR)
files = [s for s in allFiles if s.endswith('.MOV')]
jpgFiles = [s for s in allFiles if s.endswith('.JPG')]

for filename in files:
    matching = [s for s in jpgFiles if s.startswith(filename[:-4])]
    if (len(matching) > 0):
        removeFile(filename)
