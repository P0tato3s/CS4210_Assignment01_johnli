#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#encode the original categorical training features into numbers and add to the 4D array X.
#--> add your Python code here
# X =
age_map = {"Young": 1, "Prepresbyopic": 2, "Presbyopic": 3}
spectacle_map = {"Myope": 1, "Hypermetrope": 2}
astigmatism_map = {"Yes": 1, "No": 2}
tear_map = {"Normal": 1, "Reduced": 2}

for row in db:
    age, spec, astig, tear, cls = row
    X.append([
        age_map[age],
        spectacle_map[spec],
        astigmatism_map[astig],
        tear_map[tear]
    ])


#encode the original categorical training classes into numbers and add to the vector Y.
#--> addd your Python code here
# Y =
class_map = {"Yes": 1, "No": 2}
for row in db:
    Y.append(class_map[row[4]])

#fitting the decision tree to the data using entropy as your impurity measure
#--> addd your Python code here
#clf =

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()

