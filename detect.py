import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print(" AI Intrusion Detection System")
print("--------------------------------")

print("\nEnter sample network data:")

# Take simple inputs (we’ll use limited features for demo)
duration = float(input("Duration: "))
src_bytes = float(input("Source Bytes: "))
dst_bytes = float(input("Destination Bytes: "))
count = float(input("Connection Count: "))
srv_count = float(input("Service Count: "))

# Create full feature vector (41 features)
sample = [0]*41

# Fill important positions (basic demo)
sample[0] = duration
sample[4] = src_bytes
sample[5] = dst_bytes
sample[22] = count
sample[23] = srv_count

# Convert to numpy array
sample = np.array([sample])

# Prediction
prediction = model.predict(sample)

# Output
if prediction[0] == 0:
    print("\n NORMAL TRAFFIC ")
else:
    print("\n ATTACK DETECTED ")