import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model
from speech_to_text import main as s_t_t 
from text_to_speech import main as t_t_s
from browserSearch import main as m
from browserSearch import search as s

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word)  for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag) 

def predict_class(sentence):
    b_o_w = bag_of_words(sentence)
    res = model.predict(np.array([b_o_w])) [0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print("say hey J.A.R.V.I.S to start")
start = s_t_t()
ints = predict_class(start)
res = get_response(ints, intents)
if res == "Hello sir":
    print("J.A.R.V.I.S is running")
    t_t_s("Jarvis is running")
    stop = False
    while not stop: 
        message = s_t_t()
        ints = predict_class(message)
        res = get_response(ints, intents)
        if res == "goodbye sir":
            stop = True
        print(res)
        t_t_s(res)
        if "opening" in res:
            m(res)
        if "search" in message:
            s(message)    