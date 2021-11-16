import glob
path = "/path/to/folder"
imgs = []
for filename in glob.iglob(path + '**/*.jpg', recursive=True):
    imgs.append(filename)

print(imgs) #returns array of images