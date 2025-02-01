from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from math_app.models import KeywordProblem
import joblib

def main():
    # Өмнө нь ангилсан бодлогуудын дата
    problems = []

    items = KeywordProblem.objects.all()
    for item in items:
        if item.keyword.topickeyword_set.count() > 0:
            problems.append((item.problem.statement,item.keyword.name))
            print(item.problem.statement,item.keyword.name)

    texts, labels = zip(*problems)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = MultinomialNB()
    model.fit(X, labels)

    joblib.dump((vectorizer, model), "problem_classifier.pkl")
