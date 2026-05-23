import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset.csv")

# Features
X = data[[
    "lateNightCommits",
    "weekendCommits",
    "codingStreak",
    "reviewLoad"
]]

# Target
y = data["burnout"]

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
joblib.dump(model, "burnout_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")
# Accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

# Save model
joblib.dump(model, "burnout_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")

# Sample prediction
sample = [[22, 8, 31, 14]]

prediction = model.predict(sample)

result = encoder.inverse_transform(prediction)

print("Burnout Risk:", result[0])