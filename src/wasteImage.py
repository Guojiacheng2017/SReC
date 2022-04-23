import os

path = '/Users/bling/Desktop/NYU_S1/Machine Learning/project/wasteNet_SH/dataset/dry_trash'
os.chdir(path)

data = open('/Users/bling/Desktop/NYU_S2/DL/HW/Github/SReC/datasets/wasteImage.txt', 'w')

for file in os.listdir(path):
    # if file.endswith('.jpg'):
    name = file
    data.write(name + "\n")
    # print(file, file=data)

data.close()