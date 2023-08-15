import pickle, sklearn, lightgbm
import os

# Obtenha o diretório atual do script
current_directory = os.path.dirname(__file__)

def load_model():
    file_path = os.path.join(current_directory, "../model/model.pkl")
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model


def load_encoder():
    file_path = os.path.join(current_directory, "../model/ohe.pkl")
    with open(file_path, 'rb') as file:
        one_hot_encoder = pickle.load(file)
    return one_hot_encoder