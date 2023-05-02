import pickle
model_filename = "model.pkl"

with open(model_filename, "rb") as file:
    model = pickle.load(file)
print(len(model.feature_names_in_))