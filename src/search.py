from tokenizer import analyze

# Step 3 - Search
def search(index_dict, search_term):
    results_list = []
    for token in analyze(search_term):
        if token in index_dict.keys():
            if len(results_list) == 0:
                results_list = index_dict[token]
            else:
                results_list = list(set(results_list) & set(index_dict[token]))
    return results_list