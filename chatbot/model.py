from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import pickle
import cv2
import warnings
warnings.filterwarnings("ignore")

# Load dataset
df = pd.read_csv('large.csv')

# Encode input (test) and output (result) as numbers
le_test = LabelEncoder()
le_result = LabelEncoder()

df['test_encoded'] = le_test.fit_transform(df['test'])
df['result_encoded'] = le_result.fit_transform(df['result'])

X = df[['test_encoded']]
y = df['result_encoded']


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = GaussianNB()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model and encoders
pickle.dump(model, open('model.pkl', 'wb'))
while True:
# Predicting a sample input
    sample_text = input("user:")
    sample_encoded = le_test.transform([sample_text])
    prediction = model.predict([sample_encoded])
    decoded_output = le_result.inverse_transform(prediction)
    print(f"Input: {sample_text}")
    print(f"bot: {decoded_output[0]}")
    if sample_text=="bye":
        break
