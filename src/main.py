import pickle
from tokenizer import analyze
from read_xml import parsexml
from build_index import build_index
from search import search

# Step 1 - Parse the XML
try:
    element_list = pickle.load(open("data/element_list.pickle", "rb"))
except (OSError, IOError) as e:
    element_list = parsexml()
    pickle.dump(element_list, open("data/element_list.pickle", "wb"))

# Step 2 - Build the index
try:
    index_dict = pickle.load(open("data/index_dict.pickle", "rb"))
except (OSError, IOError) as e:
    index_dict = build_index(element_list)
    pickle.dump(index_dict, open("data/index_dict.pickle", "wb"))

# Step 3 - Search
search_term = input("Enter search term: ")
results_list = search(index_dict, search_term)

# Step 4 - Print results
for result in results_list:
    print(element_list[result])