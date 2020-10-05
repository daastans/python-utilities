import os

# Function to rename multiple files
def main():
    path="path/to/folder/containing/files"
    for count, filename in enumerate(os.listdir(path)):
      #count makes sure each file gets a unique name
        custom_trailer = "@laughingass" + str(count) + ".mp4"
        src =path+'/'+filename
        dst =path+'/'+ dst

        os.rename(src, dst)

if __name__ == '__main__':
    main()
