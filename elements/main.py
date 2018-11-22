import json

from flask import Flask, render_template
from flask_cors import CORS

from elements.tfidf import ExtractiveSummarizer_tfidf

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
        return json.dumps(element_data[element])


if __name__ == "__main__":
    app.run(debug=True)
