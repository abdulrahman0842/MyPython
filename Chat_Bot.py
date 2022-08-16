'''***Chat_Bot***'''

import nltk
2
from nltk.stem import WordNetLemmatizer
3
lemmatizer = WordNetLemmatizer()
4
import pickle
5
import numpy as np
6
7
from keras.models import load_model
8
model = load_model('chatbot_model.h5')
9
import json
10
import random
11
intents = json.loads(open('intents.json').read())
12
words = pickle.load(open('words.pkl','rb'))
13
classes = pickle.load(open('classes.pkl','rb'))
14
15
def clean_up_sentence(sentence):
16
    # tokenize the pattern - splitting words into array
17
    sentence_words = nltk.word_tokenize(sentence)
18
    # stemming every word - reducing to base form
19
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
20
    return sentence_words
21
# return bag of words array: 0 or 1 for words that exist in sentence
22
23
def bag_of_words(sentence, words, show_details=True):
24
    # tokenizing patterns
25
    sentence_words = clean_up_sentence(sentence)
26
    # bag of words - vocabulary matrix
27
    bag = [0]*len(words)  
28
    for s in sentence_words:
29
        for i,word in enumerate(words):
30
            if word == s: 
31
                # assign 1 if current word is in the vocabulary position
32
                bag[i] = 1
33
                if show_details:
34
                    print ("found in bag: %s" % word)
35
    return(np.array(bag))
36
37
def predict_class(sentence):
38
    # filter below  threshold predictions
39
    p = bag_of_words(sentence, words,show_details=False)
40
    res = model.predict(np.array([p]))[0]
41
    ERROR_THRESHOLD = 0.25
42
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
43
    # sorting strength probability
44
    results.sort(key=lambda x: x[1], reverse=True)
45
    return_list = []
46
    for r in results:
47
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
48
    return return_list
49
50
def getResponse(ints, intents_json):
51
    tag = ints[0]['intent']
52
    list_of_intents = intents_json['intents']
53
    for i in list_of_intents:
54
        if(i['tag']== tag):
55
            result = random.choice(i['responses'])
56
            break
57
    return result
58
59
#Creating tkinter GUI
60
import tkinter
61
from tkinter import *
62
63
def send():
64
    msg = EntryBox.get("1.0",'end-1c').strip()
65
    EntryBox.delete("0.0",END)
66
67
    if msg != '':
68
        ChatBox.config(state=NORMAL)
69
        ChatBox.insert(END, "You: " + msg + '\n\n')
70
        ChatBox.config(foreground="#446665", font=("Verdana", 12 )) 
71
72
        ints = predict_class(msg)
73
        res = getResponse(ints, intents)
74
        
75
        ChatBox.insert(END, "Bot: " + res + '\n\n')           
76
77
        ChatBox.config(state=DISABLED)
78
        ChatBox.yview(END)
79
80
root = Tk()
81
root.title("Chatbot")
82
root.geometry("400x500")
83
root.resizable(width=FALSE, height=FALSE)
84
85
#Create Chat window
86
ChatBox = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)
87
88
ChatBox.config(state=DISABLED)
89
90
#Bind scrollbar to Chat window
91
scrollbar = Scrollbar(root, command=ChatBox.yview, cursor="heart")
92
ChatBox['yscrollcommand'] = scrollbar.set
93
94
#Create Button to send message
95
SendButton = Button(root, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
96
                    bd=0, bg="#f9a602", activebackground="#3c9d9b",fg='#000000',
97
                    command= send )
98
99
#Create the box to enter message
100
EntryBox = Text(root, bd=0, bg="white",width="29", height="5", font="Arial")
101
#EntryBox.bind("<Return>", send)
102
103
#Place all components on the screen
104
scrollbar.place(x=376,y=6, height=386)
105
ChatBox.place(x=6,y=6, height=386, width=370)
106
EntryBox.place(x=128, y=401, height=90, width=265)
107
SendButton.place(x=6, y=401, height=90)
108
109
root.mainloop()
