
# coding: utf-8

# In[6]:


import speech_recognition
import tempfile
from gtts import gTTS
from pygame import mixer
def listenTo():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    return r.recognize_google(audio, language='zh-TW')


def speak(sentence, lang):
    mixer.init()
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang=lang)
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()


# In[7]:


get_ipython().system(' pip install googletrans')


# In[8]:


from googletrans import Translator
translator = Translator()
translator.translate('大家好', dest='en').text


# In[1]:


lang = 'en'
speak(translator.translate(listenTo(), lang).text, lang)

