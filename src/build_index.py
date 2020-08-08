from tokenizer import analyze

# Step 2 - Build the index
def build_index(element_list):
    index_dict = dict()

    for doc in element_list:      
        for token in analyze(doc['abstract']):
            if token in index_dict.keys():
                word_list = index_dict[token]
                word_list.append(doc['id'])
            else:
                word_list = [doc['id']]

            index_dict.update( { token: word_list } )

    return index_dict