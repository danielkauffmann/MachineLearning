import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix

data = sns.load_dataset('iris')
# data.head()

# Check for null values/
# data.isnull().sum()

# Exploring the data.
count = data.species.value_counts()
sns.countplot(x='species', data=data)
# plt.show()

x = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Plotting.


sns.pairplot(data, hue="species", kind="reg")

density = sns.PairGrid(data, hue="species")
density = density.map_diag(sns.kdeplot, lw=3, shade=True)
density = density.map_offdiag(sns.kdeplot, lw=1, legend=True)

plt.figure()
sns.heatmap(data.corr(), annot=True, fmt="f").set_title("Correlation of attributes (petal length,width and sepal "
                                                        "length,width) among Iris species")

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.2,
                                                    random_state=40)

model = LogisticRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
report = classification_report(y_test, predictions)
score = accuracy_score(y_test, predictions)
print(f'Prediction Score: {predictions}\n\nClassification Report:{report}\nAccuracy Score: {score}')
plt.figure()
plot_confusion_matrix(model, x_test, y_test)
plt.show()