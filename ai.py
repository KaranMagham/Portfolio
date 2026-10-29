# Artificial Intelligence Practicals 1–10

## Practical 1: Breadth First Search (BFS) and Iterative Depth First Search (IDFS)

Aim:

- Implement BFS and iterative DFS to solve a given problem.
- Compare the performance and efficiency of both algorithms.

Code — BFS

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

start = input("Enter starting node (A-F): ").upper()
goal = input("Enter goal node (A-F): ").upper()

if start not in graph or goal not in graph:
    print("Invalid node.")
else:
    queue = deque([start])
    visited = set()
    traversal = []
    found = False

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        traversal.append(node)
        print("Visiting:", node)

        if node == goal:
            found = True
            break

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    print("BFS Traversal:", " -> ".join(traversal))
    print("Goal found!" if found else "Goal not found!")

Code — Iterative DFS

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

start = input("Enter starting node (A-F): ").upper()
goal = input("Enter goal node (A-F): ").upper()

if start not in graph or goal not in graph:
    print("Invalid node.")
else:
    stack = [start]
    visited = set()
    traversal = []
    found = False

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        traversal.append(node)
        print("Visiting:", node)

        if node == goal:
            found = True
            break

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    print("DFS Traversal:", " -> ".join(traversal))
    print("Goal found!" if found else "Goal not found!")




## Practical 2: A\* Search and Recursive Best-First Search (RBFS)

Aim:

- Implement A\* Search for a pathfinding problem.
- Implement RBFS for the same problem.
- Compare the performance and effectiveness of both algorithms.

Code — A Search\*

import heapq

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 3)],
    "D": [("G", 5)],
    "E": [("G", 1)],
    "F": [("G", 2)],
    "G": []
}

h = {"A": 5, "B": 4, "C": 3, "D": 3,
     "E": 1, "F": 2, "G": 0}

def a_star(start, goal):
    pq = [(h[start], 0, start, [start])]
    best_cost = {start: 0}

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if cost > best_cost.get(node, float("inf")):
            continue

        for neighbour, edge_cost in graph[node]:
            new_cost = cost + edge_cost

            if new_cost < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_cost
                heapq.heappush(
                    pq,
                    (new_cost + h[neighbour], new_cost,
                     neighbour, path + [neighbour])
                )

    return None, float("inf")

start = input("Enter starting node (A-G): ").upper()
goal = input("Enter goal node (A-G): ").upper()

if start not in graph or goal not in graph:
    print("Invalid node!")
else:
    path, cost = a_star(start, goal)
    if path:
        print("A* Path:", " -> ".join(path))
        print("Total path cost:", cost)
    else:
        print("Goal not found!")

Code — RBFS

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 3)],
    "D": [("G", 5)],
    "E": [("G", 1)],
    "F": [("G", 2)],
    "G": []
}

h = {"A": 5, "B": 4, "C": 3, "D": 3,
     "E": 1, "F": 2, "G": 0}

def rbfs(node, goal, cost, path, f_node, f_limit):
    if node == goal:
        return (path, cost), f_node

    successors = []

    for neighbour, edge_cost in graph[node]:
        if neighbour not in path:
            new_cost = cost + edge_cost
            f = max(new_cost + h[neighbour], f_node)
            successors.append(
                [f, neighbour, new_cost, path + [neighbour]]
            )

    if not successors:
        return None, float("inf")

    while successors:
        successors.sort(key=lambda x: x[0])
        best = successors[0]

        if best[0] > f_limit:
            return None, best[0]

        alternative = (
            successors[1][0] if len(successors) > 1
            else float("inf")
        )

        result, new_f = rbfs(
            best[1], goal, best[2], best[3],
            best[0], min(f_limit, alternative)
        )

        best[0] = new_f

        if result is not None:
            return result, new_f

    return None, float("inf")

start = input("Enter starting node (A-G): ").upper()
goal = input("Enter goal node (A-G): ").upper()

if start not in graph or goal not in graph:
    print("Invalid node!")
else:
    result, _ = rbfs(
        start, goal, 0, [start], h[start], float("inf")
    )

    if result:
        path, cost = result
        print("RBFS Path:", " -> ".join(path))
        print("Total path cost:", cost)
    else:
        print("Goal not found!")




## Practical 3: Decision Tree Learning Algorithm for Classification

Aim:

- Implement a Decision Tree to classify a dataset.
- Evaluate its accuracy on test data.
- Visualize and interpret the generated decision tree.

Code

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(
    criterion="gini", max_depth=3, random_state=42
)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:",
      round(accuracy_score(y_test, predictions) * 100, 2), "%")
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

plt.figure(figsize=(12, 7))
plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True
)
plt.title("Decision Tree Classification - Iris Dataset")
plt.show()




## Practical 4: Feed Forward Backpropagation Neural Network

Aim:

- Implement a Feed Forward Backpropagation Neural Network.
- Train the network using a dataset.
- Evaluate the trained network on test data.

Code

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = make_pipeline(
    StandardScaler(),
    MLPClassifier(
        hidden_layer_sizes=(10,),
        max_iter=1000,
        random_state=42
    )
)

model.fit(X_train, y_train)
print("Neural network trained successfully!")

predictions = model.predict(X_test)

print("First 5 predicted classes:")
print(iris.target_names[predictions[:5]])

print("First 5 actual classes:")
print(iris.target_names[y_test[:5]])

print("Accuracy:",
      round(accuracy_score(y_test, predictions) * 100, 2), "%")

print(classification_report(
    y_test, predictions, target_names=iris.target_names
))




## Practical 5: Support Vector Machines (SVM)

Aim:

- Implement SVM for binary classification.
- Optimize model parameters using Grid Search.
- Evaluate the model on test data.

Code

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report
)

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline = make_pipeline(StandardScaler(), SVC())

parameters = {
    "svc__C": [0.1, 1, 10],
    "svc__kernel": ["linear", "rbf"],
    "svc__gamma": ["scale", "auto"]
}

grid = GridSearchCV(pipeline, parameters, cv=5)
grid.fit(X_train, y_train)

predictions = grid.predict(X_test)

print("Best Parameters:", grid.best_params_)
print("Accuracy:",
      round(accuracy_score(y_test, predictions) * 100, 2), "%")
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("Classification Report:")
print(classification_report(
    y_test, predictions, target_names=data.target_names
))




## Practical 6: AdaBoost Ensemble Learning

Aim:

- Implement AdaBoost using weak classifiers.
- Train and evaluate the ensemble model.
- Compare its performance with an individual weak classifier.

Code

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

stump = DecisionTreeClassifier(max_depth=1, random_state=42)
stump.fit(X_train, y_train)
stump_predictions = stump.predict(X_test)

model = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=50,
    random_state=42
)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

stump_accuracy = accuracy_score(y_test, stump_predictions)
boost_accuracy = accuracy_score(y_test, predictions)

print("Decision Stump Accuracy:",
      round(stump_accuracy * 100, 2), "%")
print("AdaBoost Accuracy:",
      round(boost_accuracy * 100, 2), "%")

print("Classification Report:")
print(classification_report(y_test, predictions,
                            target_names=data.target_names))

print("\nModel Comparison:")
if boost_accuracy > stump_accuracy:
    print("AdaBoost performed better than the decision stump.")
elif boost_accuracy < stump_accuracy:
    print("Decision stump performed better on this test set.")
else:
    print("Both models achieved the same accuracy.")




## Practical 7: Naive Bayes Classifier

Aim:

- Implement Naive Bayes for classification.
- Calculate class probabilities.
- Evaluate the model using test data.

Code

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report
)

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = GaussianNB()
model.fit(X_train, y_train)

print("Naive Bayes model trained successfully!")

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)

print("\nFirst 5 Predictions:")
print(iris.target_names[predictions[:5]])

print("\nActual Classes:")
print(iris.target_names[y_test[:5]])

print("\nClass Probabilities for First Test Sample:")
for i, flower in enumerate(iris.target_names):
    print(f"{flower}: {probabilities[0][i]:.4f}")

print("\nModel Accuracy:",
      round(accuracy_score(y_test, predictions) * 100, 2), "%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(
    y_test, predictions, target_names=iris.target_names
))




## Practical 8: K-Nearest Neighbors (K-NN)

Aim:

- Implement K-NN for classification.
- Predict classes for test data.
- Evaluate prediction accuracy.

Code

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("First 5 Predictions:")
print(iris.target_names[predictions[:5]])

print("\nActual Classes:")
print(iris.target_names[y_test[:5]])

print("\nAccuracy:",
      round(accuracy_score(y_test, predictions) * 100, 2), "%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(
    y_test, predictions, target_names=iris.target_names
))




## Practical 9: Association Rule Mining

Aim:

- Implement the Apriori algorithm to find frequent itemsets.
- Generate association rules and calculate support, confidence, and lift.
- Analyze the discovered relationships.

Code

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

transactions = [
    ["Milk", "Bread", "Butter"],
    ["Bread", "Butter"],
    ["Milk", "Bread"],
    ["Milk", "Butter"],
    ["Milk", "Bread", "Butter"],
    ["Bread", "Eggs"],
    ["Milk", "Eggs"],
    ["Milk", "Bread", "Eggs"],
    ["Bread", "Butter", "Eggs"],
    ["Milk", "Bread", "Butter", "Eggs"]
]

encoder = TransactionEncoder()
encoded_data = encoder.fit(transactions).transform(transactions)

df = pd.DataFrame(encoded_data, columns=encoder.columns_)

frequent_itemsets = apriori(
    df, min_support=0.3, use_colnames=True
)

print("Frequent Itemsets:")
print(frequent_itemsets)

rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.5
)

print("\nAssociation Rules:")
print(rules[[
    "antecedents", "consequents",
    "support", "confidence", "lift"
]])

print("\nRules with Lift Greater Than 1:")
useful_rules = rules[rules["lift"] > 1]

if useful_rules.empty:
    print("No useful rules found.")
else:
    print(useful_rules[[
        "antecedents", "consequents",
        "support", "confidence", "lift"
    ]])

## Practical 10: Demo of OpenAI/TensorFlow Tools

Aim:

- Explore TensorFlow tools and libraries.
- Build, train, and evaluate a neural network.
- Demonstrate the capabilities and applications of TensorFlow.

Code

import tensorflow as tf
import matplotlib.pyplot as plt

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = (
    tf.keras.datasets.mnist.load_data()
)

# Normalize image pixel values
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build the neural network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(28, 28)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

# Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train the model
model.fit(
    x_train, y_train,
    epochs=5,
    validation_split=0.1
)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)

print("Test Accuracy:", round(accuracy * 100, 2), "%")

# Predict a test image
predictions = model.predict(x_test[:5])
predicted_classes = predictions.argmax(axis=1)

print("Predicted Classes:", predicted_classes)
print("Actual Classes:", y_test[:5])

# Display a test image
plt.imshow(x_test[0], cmap="gray")
plt.title(f"Predicted Digit: {predicted_classes[0]}")
plt.axis("off")
plt.show()
