import os

files = os.listdir("")

for filename in files:
    if (filename.endswith('.MOV')):
        matching = [s for s in files if s.startswith(filename[:-4]) and s.endswith('.JPG')]
        if (len(matching) > 0):
            try:
                os.remove("" + filename)
            except:
                print('Failed to remove: ' + filename)
            print('Removed: ' + filename)
