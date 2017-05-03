from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import json
import operator

MIN_WORD_LEN = 4
stopwords = stopwords.words('english')
food = wn.synset('food.n.02')
FOOD = set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()])


class Review:
    def __init__(self, review_id, user_id, business_id, stars, text):
        self.id = review_id
        self.user_id = user_id
        self.business_id = business_id
        self.stars = stars
        self.raw_text = text


def open_json(filename):
    with open(filename) as f:
        data = json.load(f)
    return data


def dump_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)


def content_fraction(text):
    ret = []
    tokens = text.split(" ")
    for token in tokens:
        if token.lower() not in stopwords:
            if len(token) < MIN_WORD_LEN:
                continue
            if token[len(token)-1].isalpha() == 0:
                token = token[:-1]
            if token[0].isalpha() == 0:
                token = token[1:]
            ret.append(token.lower())
    return ret


def generate_dict(input_file, output_file):
    input = open(input_file, 'r')
    lines = input.readlines()
    input.close()

    word_list = []
    for line in lines:
        word_list.extend(line.split()[1:])

    output = open(output_file, 'w')

    for word in set(word_list):
        output.write(str(word) + "\n")


def json_to_text(json_file, output_file):
    reviews = []
    restaurants = dict()
    with open(json_file) as datafile:
        data = json.load(datafile)
        for i in range(len(data)):
            reviews.append(Review(data[i]["review_id"], data[i]["user_id"], data[i]["business_id"], data[i]["stars"],
                                  data[i]["text"].replace("\n", " ")))

    for review in reviews:
        text_tokens = content_fraction(review.raw_text)
        bus_id = str(review.business_id)
        restaurants.setdefault(bus_id, dict())
        for t in range(len(text_tokens)):
            restaurants[bus_id].setdefault(str(text_tokens[t]), 0)
            restaurants[bus_id][str(text_tokens[t])] += 1
            #print("restaurant {0} count for token {1}: {2}".format(bus_id, str(text_tokens[t]), restaurants[bus_id][str(text_tokens[t])]))

    output = open(output_file, 'w')

    for i in restaurants:
        line = i + " "
        for key, value in restaurants[i].items():
            line = line + key + ":" + str(value) + " "
        output.write(line + "\n")
    output.close()


def unique_words(input_file, output_file):
    input = open(input_file, 'r')
    lines = input.readlines()
    input.close()

    word_list = []
    for line in lines:
        word_list.extend([w[:-2] for w in line.split()[1:]])

    output = open(output_file, 'w')

    for word in set(word_list):
        output.write(str(word) + "\n")

# generate the dict for word-id transformation
def make_vocab(filename):
    lines = open(filename, 'r')
    index = 0
    vocab = {}
    for line in lines:
        vocab[line[:-1]] = index
        index += 1

    lines.close()
    return vocab


def word_to_id(input_file, output_file, dict_file):
    input = open(input_file, 'r')
    lines = input.readlines()
    input.close()
    vocab = make_vocab(dict_file)

    output = open(output_file, 'w')
    for line in lines:
        sum_ = 0
        tmp_ = ""
        tokens = line.split()[:]
        error_ = 0
        for key in tokens[1:]:
            token = key.split(":")
            try:
                sum_ += int(token[1])
                if token[0] in vocab:
                    index = vocab[token[0]]
                    tmp_ += str(index) + ":" + token[1] + " "
            except ValueError:
                error_ += 1
            except IndexError:
                error_ += 1
        print("sum is: {}; error#: {}".format(sum_, error_))
        output.write(str(sum_) + " " + tmp_ + "\n")


def _format_(filename):
    in_file = open(filename, "r")
    lines = in_file.readlines()
    in_file.close()
    out_file = open(filename, "w")
    lines[0] = "[" + lines[0]
    for line in lines[:-1]:
        out_file.write(line[:-1] + ",\n")
    out_file.write(lines[len(lines)-1] + "]")
    out_file.close()


def main():
    #_format_("Cleveland_review.json")
    # print("============= Finish reformatting ===============")
    # json_to_text("Cleveland_review.json", "pre_yelp.txt")
    # print("============= Finish to text ===============")
    # unique_words("pre_yelp.txt", "vocab.txt")
    # print("============= Finish generating vocab ===============")
    # word_to_id("pre_yelp.txt", "Cleveland_frequency_analysis.txt", "vocab.txt")
    # print("============= Finish word_to_id ===============")
    city_in = ["Madison_review_frequency.json", "Cleveland_review_frequency.json"]
    city_out = ["Madison_restFood.json", "Madison_restFood.json"]
    
    for i in range(len(city_in)):
        most_frequent = []
        _food = set()
        count = 0
        data = open_json(city_in[i])
        for entry in data:
            for key in entry:
                for _key, _value in entry[key].items():
                    if _value > 80 and _key in FOOD and _key not in _food:
                        _food.add(_key)
                        count += 1
                        most_frequent.append({"name": _key, "value": _value})
        dump_json(city_out[i], most_frequent)
        print(count)


if __name__ == "__main__":
    main()