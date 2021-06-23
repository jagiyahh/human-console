import nltk
from nltk.corpus import wordnet
import os
import re
import webbrowser as wb
import speech_recognition as sr
import datetime

import webbrowser

chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

apps = {
    'Spotify': r'C:\Users\jonas\AppData\Roaming\Spotify\Spotify.exe',
    'Chrome': r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    'Notepad': r'%windir%\system32\notepad.exe',
    'Excel': r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE',
    'Discord': r'C:\Users\jonas\AppData\Local\Discord\app-0.0.309'

}

commands = ['run', 'open', 'kill', 'delete', 'search', 'time']

# synonyms = {}
#
# for a in commands:
#     array_synonyms = set()
#
#     for syn in wordnet.synsets(a):
#         for i in syn.lemmas():
#             f = nltk.pos_tag(nltk.word_tokenize(i.name()))
#             if f[0][1] in 'VB':
#                 array_synonyms.add(f[0][0])
#     synonyms[a] = array_synonyms

synonyms = {
    'run': {'execute', 'launch', 'start'},
    'open': {},
    'kill': {'stop', 'shut', 'halt', 'close'},
    'delete': {'remove', 'launch'},
    'search': {'find', 'google'}
}

temp = ['open', 'launch', 'execute', 'kill', 'close', 'shut', 'halt', 'delete', 'search', 'google']
searching = ['search', 'google']
execptions = [nltk.tag.str2tuple(a + '/VB') for a in temp]


def program_check(sentence_arr):
    for c in apps.keys():
        for b in sentence_arr:
            if c == b:
                return True


def get_key(val):
    for key, value in synonyms.items():
        if val == value:
            return key


def spch_to_txt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    sentence = r.recognize_google(audio, language='en-US')
    print(sentence)
    return sentence


def check_exc(tg):
    for a in range(len(execptions)):
        if tg == execptions[a][0]:
            return 1


def spk_tp(b, tg):
    if b + 1 < len(tg):
        return tg[b + 1][0]
    else:
        return ''


mic = 0

while 1:
    if mic:
        print("I'm listening")
        sen = spch_to_txt()
    else:
        print("What can I do for you?")
        sen = input()

    action = ''
    obj = ''
    object_arr = []

    tokens = nltk.word_tokenize(sen)
    tags = nltk.pos_tag(tokens)

    for x in range(len(tags)):
        if not action:
            if tags[x][1] in 'VB':
                if tags[x - 1][1] not in 'MD':
                    action = tags[x][0]
                    if tags[x][0] not in searching:
                        obj = spk_tp(x, tags)
                    else:
                        object_arr += (tokens[x + 1:])
            else:
                if check_exc(tags[x][0]):
                    action = tags[x][0]
                    if tags[x][0] not in searching:
                        obj = spk_tp(x, tags)
                    else:
                        object_arr += (tokens[x + 1:])

    chmurka = ' '.join(object_arr)

    if action not in commands:
        for a in synonyms.keys():
            if action in synonyms.get(a):
                action = a

    if action == 'speak':
        mic = 1
    elif action == 'type':
        mic = 0

    elif action == 'run':
        chmurka = apps.get(obj)
        os.startfile(chmurka)

    elif action == 'open':
        url = re.match(r'(https:\/\/)?(www\.)?(\w+\.)+com\/?[^\s]*', obj)
        if url:
            chmurka = url.group()
            webbrowser.get('chrome').open_new_tab(chmurka)
        else:
            os.startfile(obj)

    elif action == 'kill':
        if obj in apps.keys():
            os.system('taskkill /f /im ' + obj + '.exe')
        else:
            print("Sorry I don't have permission to close that program")

    elif action == 'delete':
        m = re.match(r'\w+\.\w+', obj)
        chmurka = m.group()
        os.remove(chmurka)

    elif action == 'search':
        wb.open_new_tab('https://www.google.com/search?q=' + chmurka)

    elif action == 'time':
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)

    else:
        print("Sorry I don't understand that")
