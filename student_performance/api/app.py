from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('final.csv')
df = df.iloc[:,1:]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/original_data')
def visualize_data():
    table_html = df.to_html()
    return render_template('data.html', table=table_html)

@app.route('/Findings')
def clusters():
    return render_template('finding.html', out1='static/output1.png', out2='static/output2.png',out3='static/output3.png',out4='static/output4.png')

@app.route('/Clusterubg')
def clustering():
    return render_template('clustering.html', dendrogram_image='static/dendogram.png', other_image='static/elbow.png')


if __name__ == '__main__':
    app.run(debug=True)
