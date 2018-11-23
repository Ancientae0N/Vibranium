import json

from flask import Flask, render_template
from flask_cors import CORS

from tfidf import ExtractiveSummarizer_tfidf
from balance import balance_equation

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
text_summarizer = ExtractiveSummarizer_tfidf(corpus="clean_dataset")
with open("element_data.json", "r") as f:
    element_data = json.load(f)


@app.route("/")
def first():
    return render_template("element.html")


@app.route("/summary/<element>/<length>")
def summary(element, length):
    length = int(length)
    assert type(element) == str and len(element) < 3
    assert 2 < length
    element = element.lower()
    text = element_data[element]["text"]
    return text_summarizer.tf_idf_summarizer(text, sentence_count=length)


@app.route("/data/<element>")
def get_element_data(element):
    if element == "all":
        return json.dumps(element_data)
    else:
        element = element.lower()
        if element in element_data:
            return json.dumps(element_data[element])
        else:
            return "Invalid element " + element


@app.route("/balance/<equation>")
def get_balanced_equation(equation):
    return balance_equation(equation)


@app.route("/<element>")
def load_element_page(element):
    if element not in element_data:
        return "Invalid element " + element
    return render_template("element.html", ELEMENT=element)


if __name__ == "__main__":
    app.run(debug=True)
