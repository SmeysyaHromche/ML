import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load and preprocess the Boston Housing dataset from a CSV file
# Замените 'path_to_your_file.csv' на путь к вашему файлу CSV
boston = pd.read_csv('path_to_your_file.csv')

# Предполагаем, что 'MEDV' является целевой переменной (ценой домов), а остальные столбцы - признаками
X = boston.drop(columns=['MEDV'])  # Все колонки, кроме 'MEDV'
y = boston['MEDV']  # Целевая переменная

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data (zero mean, unit variance)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert data to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)  # Преобразуем в тензор
y_test = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)  # Преобразуем в тензор

# 2. Define the Feedforward Neural Network
class FeedforwardNN(nn.Module):
    def __init__(self):
        super(FeedforwardNN, self).__init__()
        self.fc1 = nn.Linear(X_train.shape[1], 64)  # Input layer (13 -> 64)
        self.fc2 = nn.Linear(64, 64)                # Hidden layer (64 -> 64)
        self.fc3 = nn.Linear(64, 1)                 # Output layer (64 -> 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)  # Linear output layer
        return x

# Instantiate the model
model = FeedforwardNN()

# 3. Define loss function and optimizer
criterion = nn.MSELoss()  # Mean Squared Error for regression
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. Train the model
epochs = 500
for epoch in range(epochs):
    model.train()  # Set model to training mode

    # Forward pass: compute predicted y by passing X to the model
    y_pred = model(X_train)

    # Compute and print loss
    loss = criterion(y_pred, y_train)

    # Zero gradients, backward pass, and update the weights
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 50 == 0:  # Print every 50 epochs
        print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}')

# 5. Evaluate the model
model.eval()  # Set model to evaluation mode
with torch.no_grad():
    y_test_pred = model(X_test)
    test_loss = criterion(y_test_pred, y_test)

print(f'\nTest Loss: {test_loss.item():.4f}')
