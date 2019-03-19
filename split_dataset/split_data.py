import os, random



# Read the filenames
dirname = 'data_raw'
files = [f[:-4] for f in os.listdir(dirname) if f[-4:].lower() =='.txt']


# Random divide
test = random.sample(files, len(files)//10)
train = [f for f in files if f not in test]


# Save to .txt file
def list2txt(arr, fname):
    with open(fname+ '.txt', 'w') as f:
        for a in arr:
            f.write('/home/martibsk/dev/myDarknet/data/gripping/images/train/'+a+'.jpg\n')



print(len(test))
print(len(train))
print(len(files), len(test+train))

list2txt(test, 'test')
list2txt(train, 'train')
