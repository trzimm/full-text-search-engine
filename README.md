### Description
This is based on the **Let's build a full text search engine** written in Golang
https://artem.krylysov.com/blog/2020/07/28/lets-build-a-full-text-search-engine/

### Setup

Download the dataset
```
wget -O - https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract1.xml.gz | gunzip -c > enwiki-latest-abstract1.xml
```

Setup Python
```
pip3 install nltk

# uncomment line
nltk.download('wordnet')
```

Run
```
python3 src/main.py
```