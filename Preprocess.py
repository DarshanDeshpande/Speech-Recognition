import librosa
import glob
import os,time
from os import listdir
from os.path import isfile, join
import numpy as np

class_list, X_train, Y_train = [],[],[]
filename = "D:\\SpeechRecognitionData\\train\\audio\\"


class_names = os.listdir(filename)
print(class_names)

for classes in class_names:
    if classes == '_background_noise_':
        continue
    else:
        class_list.append(''.join(filename+classes))

print(class_list,"\n",len(class_list))


def create_X(address):
    wave,sr = librosa.load(address)
    wave.reshape(-1,1)
    return wave


def getLabel(filename):
    base_name = os.path.basename(filename)
    return base_name


def execute(X_train, Y_train):
    loop = 0
    for i in class_list:
        c=0
        loop+=1
        for file in glob.glob("".join(i+"\\*.wav")):
            if create_X(file).shape[0] == 22050:
                c+=1
                Y_train.append(getLabel(i))
                X_train.append(create_X(file))
                if c%100==0:
                    print("{} files processed in loop {}".format(c,loop))

    X_train = np.array(X_train).reshape(-1,22050)
    Y_train = np.array(Y_train)
    np.save("D:\\SpeechRecognitionData\\Arrays\\Xtrain",X_train)
    np.save("D:\\SpeechRecognitionData\\Arrays\\Ytrain",Y_train)


execute(X_train,Y_train)


