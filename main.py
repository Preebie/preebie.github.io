import flask
from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify, make_response
import warnings
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.pyplot import figure
from sklearn import metrics, tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, f1_score, make_scorer,
                             plot_confusion_matrix, precision_recall_curve,
                             precision_recall_fscore_support, precision_score,
                             recall_score, roc_auc_score, roc_curve)
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier

warnings.filterwarnings("ignore")


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/aboutme.html', methods=['GET', 'POST'])
def aboutme():
    return render_template('aboutme.html')

@app.route('/contactme.html', methods=['GET', 'POST'])
def contactme():
    return render_template('contactme.html')


if __name__ == "__main__":
    app.run(debug=True)