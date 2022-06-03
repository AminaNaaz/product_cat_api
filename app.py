from flask import Flask,render_template,url_for,request
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import texthero as hero
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pickle


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)