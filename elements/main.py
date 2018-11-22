from flask import Flask, render_template
import wikipedia
import pprint
from elements.tfidf import ExtractiveSummarizer_tfidf
import json
app = Flask(__name__)
text_summarizer = ExtractiveSummarizer_tfidf(corpus = "clean_dataset")
with open("elements_data.json", "r") as f:
	element_data = json.load(f)


@app.route("/summary/:element/:length")
def summary(element, length):
	assert type(element) == str  and len(element) < 3
	assert 2 < length < 11
	element = element.lower()
	text = element_data[element]["text"]
	return text_summarizer.tf_idf_summarizer(text, sentence_count=length)


@app.route("/data/:element")
def get_element_data(element):
	assert type(element) == str and  1 <= len(element) < 3
	element = element.lower()
	return json.dumps(element_data[element])





	

# @app.route("/element")
# def summary_page():
# 	# summary = text_summarizer.tf_idf_summarizer(text, sentence_count = 5)
# 	# print(summary)
# 	return "this is the summary"




if __name__ == "__main__":
	app.run(debug=True)