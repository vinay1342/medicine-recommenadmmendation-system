import pickle

# Path to your pickle file
file_path = 'E:/medicine recommendation system/svc.pkl'

# Load the pickle file
with open(file_path, 'rb') as file:
    data = pickle.load(file)

# Print the data or check its type
print(type(data))
print(data)
from sklearn.svm import SVC

svc = SVC(probability=True)
