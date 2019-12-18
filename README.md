# Speech-Recognition
A speech recognition model using a three layered Conv1D neural network made for Tensorflow's Speech Recognition Kaggle Challenge 
# Using the Model
1. Compile and run the preprocess.py file
2. Compile and run the DataSplit.ipynb jupyter notebook. This notebook splits the Xtrain and Ytrain files obtained after executing the preprocess.py so as to save time for training. The notebook gives 50 npy files containing shuffled data.
3. Run the Model.py to train the model(Accuracy ~94% with 10 epochs)
The trained model and one set of feature and label files can be found <a href="https://drive.google.com/open?id=1ZoDwWZUbLIkJQYqaYDr2U3J16msidoF8">here</a>
# Credits
1. Kaggle and Tensorflow for the Speech Data which can be found <a href="https://www.kaggle.com/c/tensorflow-speech-recognition-challenge">here</a>
