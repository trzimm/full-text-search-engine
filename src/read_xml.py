try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# Step 1 - Parse the XML
def parsexml():
    tree = ET.parse('data/enwiki-latest-abstract1.xml')
    root = tree.getroot()

    docid=0
    my_list = []
    for doc in root:
        my_dict={'id': docid}
        for child in doc:
            if child.tag =='title':
                my_dict.update( {'title': child.text} )
            if child.tag =='abstract':
                my_dict.update( {'abstract': child.text})

        my_list.append(my_dict)
        docid = docid + 1
    
    return my_list