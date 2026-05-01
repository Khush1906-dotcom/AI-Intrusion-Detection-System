import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Column names (NSL-KDD)
columns = ["duration","protocol_type","service","flag","src_bytes","dst_bytes",
           "land","wrong_fragment","urgent","hot","num_failed_logins",
           "logged_in","num_compromised","root_shell","su_attempted",
           "num_root","num_file_creations","num_shells","num_access_files",
           "num_outbound_cmds","is_host_login","is_guest_login","count",
           "srv_count","serror_rate","srv_serror_rate","rerror_rate",
           "srv_rerror_rate","same_srv_rate","diff_srv_rate",
           "srv_diff_host_rate","dst_host_count","dst_host_srv_count",
           "dst_host_same_srv_rate","dst_host_diff_srv_rate",
           "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate",
           "dst_host_serror_rate","dst_host_srv_serror_rate",
           "dst_host_rerror_rate","dst_host_srv_rerror_rate","label"]

# Load dataset
data = pd.read_csv("dataset.csv", names=columns)

# Remove extra spaces (important fix)
data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Convert numeric columns properly
for col in data.columns:
    try:
        data[col] = pd.to_numeric(data[col])
    except:
        pass

# Encode categorical columns
label_encoders = {}
for col in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Check data types
print("\nData Types After Cleaning:\n")
print(data.dtypes)

# Features & Labels
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("\nAccuracy:", accuracy)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("\nModel saved successfully!")