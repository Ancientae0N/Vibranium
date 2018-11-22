import wikipedia
import json
with open("elements.json", "w") as f:
    element_data = json.load()

def scrape_wiki():
    final_data = dict()
    happened = False
    for i, key in enumerate(element_data, start=1):
        final_data[key] = element_data[key]
        if i == 110:
            continue
        # print(element_data[key]["name"])
        try:
            page = wikipedia.page(element_data[key]["name"])
        except wikipedia.DisambiguationError:
            print("vishal lodu", key)
            page = wikipedia.page(element_data[key]["name"] + "_(element)")
        except:
            print("didn't work for", key)
            continue
        raw_text = page.content
        index = raw_text.find("\n\n")

        final_data[key]["text"] = raw_text[:index].strip()
        print(i, "Completed", key)

    with open("element_data.json", "w") as f:
        json.dump(final_data, f)
