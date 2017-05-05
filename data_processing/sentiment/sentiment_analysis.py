import nltk
import yaml
import re
import json

STOPWORDS = nltk.corpus.stopwords.words('english')
EPSILON = 0.000000001


def tokenize(string):
    split_regex = r'\W+'
    return [item for item in re.split(split_regex, string.lower()) if item and item not in STOPWORDS]


class DictionaryTagger(object):
    def __init__(self, dictionary_paths):
        files = [open(path, 'r') for path in dictionary_paths]
        dictionaries = [yaml.load(dict_file) for dict_file in files]
        map(lambda x: x.close(), files)
        self.dictionary = {}
        self.max_key_size = 0
        for curr_dict in dictionaries:
            for key in curr_dict:
                if key in self.dictionary:
                    self.dictionary[key].extend(curr_dict[key])
                else:
                    self.dictionary[key] = curr_dict[key]
                    self.max_key_size = max(self.max_key_size, len(key))

    def score(self, sentence):
        tokens = tokenize(sentence)
        taggings = [self.dictionary[token] for token in tokens if token in self.dictionary.keys()]
        N = len(tokens)
        sentiment = 0
        weight = 1
        for tags in taggings:
            if tags[0] == "positive":
                sentiment += 1
            elif tags[0] == "negative":
                sentiment -= 1
            elif tags[0] == "inc":
                weight *= 1.5
            elif tags[0] == "dec":
                weight /= 1.5
        return sentiment * weight / N


def sentiment_by_review(cityReview):
    dictTagger = DictionaryTagger(['dicts/positive.yml', 'dicts/negative.yml',
                                   'dicts/inc.yml', 'dicts/dec.yml', 'dicts/inv.yml'])
    with open(cityReview) as f:
        review_data = json.load(f)
    sentiment_data = []
    N = len(review_data)
    n = 0
    for i in review_data:
        output = dict()
        output["business_id"] = i["business_id"]
        output["score"] = dictTagger.score(i["text"])
        output["funny"] = i["funny"]
        output["useful"] = i["useful"]
        output["stars"] = i["stars"]
        output["cool"] = i["cool"]
        sentiment_data.append(output)
        print("finishing: {}/{}".format(n, N))
        n += 1

    # "Madison_review.json"
    output = cityReview.split(".")[0][:-6] + "sentiment.json"
    with open(output, "w") as f:
        json.dump(sentiment_data, f)


def sentiment_by_restaurant(citySentiment):
    rest_sentiment = dict()
    with open(citySentiment) as f:
        review_data = json.load(f)

    for i in review_data:
        if i["business_id"] in rest_sentiment:
            rest_sentiment[i["business_id"]] += i["score"]
        else:
            rest_sentiment[i["business_id"]] = i["score"]

    ret = [{"business_id": key, "score": rest_sentiment[key]} for key in rest_sentiment]

    output = citySentiment.split(".")[0] + "_by_restaurant.json"
    with open(output, "w") as f:
        json.dump(ret, f)


def calc_zeros(jsonfile):
    with open(jsonfile) as f:
        data = json.load(f)
    zero, non_zero = 0, 0
    for i in data:
        if float(i["score"]) < EPSILON:
            zero += 1
        else:
            non_zero += 1
    print("#zero: {}; #non_zero: {}".format(zero, non_zero))


def main():
    cityName = ["Madison", "Cleveland"]
    sentiment_by_review("Cleveland_review.json")
    sentiment_by_restaurant("Cleveland_sentiment.json")
    calc_zeros("Cleveland_sentiment_by_restaurant.json")

    return

if __name__ == '__main__':
    main()