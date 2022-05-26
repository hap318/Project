import random, math
from nltk.corpus import stopwords
from nltk.classify.api import ClassifierI
from nltk.probability import FreqDist

stop = stopwords.words('english')


def split_data(data, ratio=0.7):  # when the second argument is not given, it defaults to 0.7

    n = len(data)  # Found out number of samples present.  data could be a list or a generator
    train_indices = random.sample(range(n), int(n * ratio))  # Randomly select training indices
    test_indices = list(set(range(n)) - set(train_indices))  # Other items are testing indices

    train = [data[i] for i in train_indices]  # Use training indices to select data
    test = [data[i] for i in test_indices]  # Use testing indices to select data

    return (train, test)  # Return split data


# add your normalise function here
def normalise(wordlist):
    lowered = [word.lower() for word in wordlist]
    filtered = [word for word in lowered if word.isalpha() and word not in stop]
    return filtered


# add your functions for finding most_frequent_words and above_threshold_words
def most_frequent_words(posfreq, negfreq, topk):
    difference = posfreq - negfreq
    sorteddiff = difference.most_common()
    justwords = [word for (word, freq) in sorteddiff[:topk]]
    return justwords


def above_threshold(posfreq, negfreq, threshold):
    difference = posfreq - negfreq
    sorteddiff = difference.most_common()
    filtered = [w for (w, f) in sorteddiff if f > threshold]
    return filtered


class SimpleClassifier(ClassifierI):

    def __init__(self, pos, neg):
        self._pos = pos
        self._neg = neg

    def classify(self, words):
        score = 0

        for word, value in words.items():
            if word in self._pos:
                score += value
            if word in self._neg:
                score -= value

        # add code here that assigns an appropriate value to score
        if score < 0:
            return "neg"
        if score > 0:
            return "pos"
        if score == 0:
            posneg = random.randint(0, 1)
            if posneg == 0:
                return "pos"
            if posneg == 1:
                return "neg"

    ##we don't actually need to define the classify_many method as it is provided in ClassifierI
    # def classify_many(self, docs):
    #    return [self.classify(doc) for doc in docs]

    def labels(self):
        return ("pos", "neg")


## put your extended SimpleClassifier classes here
class SimpleClassifier_mf(SimpleClassifier):

    def __init__(self, k):
        self._k = k

    def train(self, training_data):

        pos_freq_dist = FreqDist()
        neg_freq_dist = FreqDist()

        for reviewDist, label in training_data:
            if label == 'pos':
                pos_freq_dist += reviewDist
            else:
                neg_freq_dist += reviewDist

        self._pos = most_frequent_words(pos_freq_dist, neg_freq_dist, self._k)
        self._neg = most_frequent_words(neg_freq_dist, pos_freq_dist, self._k)


class SimpleClassifier_ot(SimpleClassifier):

    def __init__(self, k):
        self._k = k

    def train(self, training_data):

        pos_freq_dist = FreqDist()
        neg_freq_dist = FreqDist()

        for reviewDist, label in training_data:
            if label == 'pos':
                pos_freq_dist += reviewDist
            else:
                neg_freq_dist += reviewDist

        self._pos = above_threshold(pos_freq_dist, neg_freq_dist, self._k)
        self._neg = above_threshold(neg_freq_dist, pos_freq_dist, self._k)


# code for your NBClassifier
class NBClassifier(ClassifierI):

    def __init__(self):
        pass

    def _set_known_vocabulary(self, training_data):
        # add your code here
        known = []
        for doc, label in training_data:
            known += list(doc.keys())
        self.known = set(known)

    def _set_priors(self, training_data):
        priors = {}
        for (doc, label) in training_data:
            priors[label] = priors.get(label, 0) + 1
        total = sum(priors.values())
        for key, value in priors.items():
            priors[key] = value / total
        self.priors = priors

    def _set_cond_probs(self, training_data):
        conds = {}
        for (doc, label) in training_data:
            classcond = conds.get(label, {})
            for word in doc.keys():
                classcond[word] = classcond.get(word, 0) + 1

            conds[label] = classcond

        for label, classcond in conds.items():
            for word in self.known:
                classcond[word] = classcond.get(word, 0) + 1
            conds[label] = classcond

        print(conds)
        for label, dist in conds.items():
            total = sum(dist.values())
            conds[label] = {key: value / total for (key, value) in dist.items()}

        self.conds = conds

    def train(self, training_data):
        self._set_known_vocabulary(training_data)
        self._set_priors(training_data)
        self._set_cond_probs(training_data)

    def classify(self, doc):
        doc_probs = {key: math.log(value) for (key, value) in self.priors.items()}
        # <put your definition of classify here>
        for word in doc.keys():
            if word in self.known:
                doc_probs = {classlabel: sofar + math.log(self.conds[classlabel].get(word, 0)) for (classlabel, sofar)
                             in doc_probs.items()}

        highprob = max(doc_probs.values())
        classes = [c for c in doc_probs.keys() if doc_probs[c] == highprob]
        return random.choice(classes)


class ConfusionMatrix:
    def __init__(self, predictions, goldstandard, classes=("pos", "neg")):

        (self.c1, self.c2) = classes
        self.TP = 0
        self.FP = 0
        self.FN = 0
        self.TN = 0
        for p, g in zip(predictions, goldstandard):
            if g == self.c1:
                if p == self.c1:
                    self.TP += 1
                else:
                    self.FN += 1

            elif p == self.c1:
                self.FP += 1
            else:
                self.TN += 1

    def precision(self):
        p = 0
        # put your code to compute precision here
        p += self.TP / (self.TP + self.FP)
        return p

    def recall(self):
        r = 0
        # put your code to compute recall here
        r += self.TP / (self.TP + self.FN)
        return r

    def f1(self, p, r):
        f1 = 0
        # put your code to compute f1 here
        f1 += (2 * p * r) / (p + r)
        return f1

