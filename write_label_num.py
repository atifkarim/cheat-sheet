import os

dataFile = open("/home/atif/training_by_several_learning_process/GTSRB/Final_Training/Images/GTSRB_Label_content.txt", "w")
for line in range(43):
    dataFile.write("%s -- \n" % line)
dataFile.close()
