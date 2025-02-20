from flask import Flask
from textblob import TextBlob
from googletrans import Translator

app = Flask('__name__')

@app.route('/')
def home():
    return 'Olá, mundo!'

@app.route('/sentimento/<frase>')
def sentimento(frase):
    tb = TextBlob(frase)
    translator = Translator()
    tb_en = translator.translate(str(tb), dest='en').text

    #print(tb_en)
    # Create a TextBlob object from the translated text
    tb_en_blob = TextBlob(tb_en)
    polaridade  = tb_en_blob.sentiment.polarity
    return "polaridade: {}".format(polaridade)


app.run(debug = True)