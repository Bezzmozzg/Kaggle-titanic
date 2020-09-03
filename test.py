import pandas as pd
from flask import Flask

df_t = pd.read_csv('titanic.csv')

result = df_t.query("Survived == 1 and Age > 18").sort_values('Age').head(10)

app = Flask(__name__)


@app.route('/')
def main():
    return result.to_html()


@app.route('/data.json')
def data():
    return df_t.to_json()


if __name__ == '__main__':
    app.run()
