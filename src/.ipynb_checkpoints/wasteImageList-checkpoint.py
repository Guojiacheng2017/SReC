import os

# path = '/mnt/wasteNet_SH-main/dataset_test/poison_trash'
path = '/mnt/SReC/sim_comp/poison_trash'
os.chdir(path)


data = open('/mnt/SReC/datasets/simple_testde/test_poison.txt', 'w')

for file in os.listdir(path):
    # if file.endswith('.jpg'):
    name = file
    data.write(name + "\n")
    # print(file, file=data)

data.close()
