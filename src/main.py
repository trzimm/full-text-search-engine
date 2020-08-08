import pickle
import time
from tokenizer import analyze
from read_xml import parsexml
from build_index import build_index
from search import search

# Step 1 - Parse the XML
t0 = time.clock()
try:
    element_list = pickle.load(open("data/element_list.pickle", "rb"))
except (OSError, IOError) as e:
    element_list = parsexml()
    pickle.dump(element_list, open("data/element_list.pickle", "wb"))
t1 = time.clock() - t0
print("Loaded XML (sec): ", t1)

# Step 2 - Build the index
t0 = time.clock()
try:
    index_dict = pickle.load(open("data/index_dict.pickle", "rb"))
except (OSError, IOError) as e:
    index_dict = build_index(element_list)
    pickle.dump(index_dict, open("data/index_dict.pickle", "wb"))
t1 = time.clock() - t0
print("Loaded index (sec): ", t1)
print("Index size: ", len(index_dict))


while True:
    # Step 3 - Search
    search_term = input("\nEnter search term: ")
    t0 = time.clock()
    results_list = search(index_dict, search_term)
    t1 = time.clock() - t0

    # Step 4 - Print results
    for result in results_list:
        print(element_list[result])

    print("Found Results (sec): ", t1)
    print("Result size: ", len(results_list))