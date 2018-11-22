from flask import Flask
from elements.tfidf import ExtractiveSummarizer_tfidf
import json
app = Flask(__name__)
text_summarizer = ExtractiveSummarizer_tfidf(corpus = "clean_dataset")
with open("element_data.json", "r") as f:
    element_data = json.load(f)


@app.route("/summary/<element>/<length>")
def summary(element, length):
    length = int(length)
    assert type(element) == str  and len(element) < 3
    assert 2 < length
    element = element.lower()
    text = element_data[element]["text"]
    return text_summarizer.tf_idf_summarizer(text, sentence_count=length)


@app.route("/data/<element>")
def get_element_data(element):
    assert type(element) == str and  1 <= len(element) < 3
    element = element.lower()
    print(element_data[element])
    return json.dumps(element_data[element])


if __name__ == "__main__":
    app.run(debug=True)