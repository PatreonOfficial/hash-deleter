# deletes files based on hash
import hashlib as hash
import os
import shutil


move = []
dir = "sourcefiles/"
files = os.listdir(dir)

os.mkdir("delme")

def remove(files, dir):
    for i in files:
        with open(dir + i, 'rb', buffering=0) as f:
            curhash = hash.file_digest(f, "sha1").hexdigest()
            f.close()
            if curhash in move:
                shutil.move(dir + i, "delme/" + i)
                print("found: " + i)

def addToList(addFile):
    f = open(addFile, 'rb', buffering=0)
    log = open("files.txt", "w")
    move.append(hash.file_digest(f, "sha1").hexdigest())
    log.write(str(move))
    log.close()

def auto():
    move = []
    t = []
    for i in files:
        with open(dir + i, 'rb', buffering=0) as f:
            curhash = hash.file_digest(f, "sha1").hexdigest()
            f.close()
            if curhash in move:
                shutil.move(dir + i, "delme/" + i)
                print("found: " + i)
                t.append(curhash)
            else:
                move.append(curhash)
    files2 = os.listdir(dir)
    for i in files2:
        with open(dir + i, 'rb', buffering=0) as f:
            curhash = hash.file_digest(f, "sha1").hexdigest()
            f.close()
            if curhash in t:
                shutil.move(dir + i, "delme/" + i)
                print("found: " + i)
while True:
    run = input("(S)etup, (A)uto, (M)anuel, (H)elp: ")
    if str(run).upper() == "S":
        dir = input("Path to folder: ")
        os.mkdir(dir)

    if str(run).upper() == "A":
        auto()

    elif str(run).upper() == "M":
        x = input("Specify Filename: ")
        addToList(dir + x)
        remove(files, dir)

    elif str(run).upper() == "H":
        print("Setup sets the working directory")
        print("Auto automaticly finds multiple files with the same hash")
        print("Manuel lets you define a file wich hash should be searched for")
        print("More in 'readme.md'")

    else:
        print("Invalid Input")