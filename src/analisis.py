import csv

from utils import *
import os

try:
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print (' You need to install nltk (http://nltk.org/index.html)')



def fullAnalisisTxt(file):

    filename = "../public/docs/"+ file

    palabras = []

    with open(filename) as fname:
        for lineas in fname:
            palabras.extend(lineas.split())


    print ('Input File Name : '+filename)
    try:
        input_file = load_file(filename)
        text = ''
        line_count=1
        for i in input_file:
            text+=str(line_count)+'| '+str(i)
            line_count+=1
        """
        print ('\n')
        #time.sleep(2)
        print ('-----------------Input Text-----------------')
        print (text)
        print ('--------------------------------------------\n')
        """
    except Exception as e:
        print ('Error Occured while loading text file. Error : '+str(e))
    finally:
        input_file.close()

    language = detect_language(text)
    """
    print ('\n')
    print ('----------------------------')
    print ('Language Deteced : ',language.upper())
    print ('----------------------------')
    print ('\n')

    print ('Checking for bad words in '+language.upper()+' language...')
    print ('**********************************************************\n')
    """

    badwords = load_bad_words(language)

    badwords = set(badwords)
    palabras = set(palabras)


    cant = badwords & palabras

    return len(cant), len(palabras)


def fullAnalisisPdf(file):

    filename = "../public/docs/"+ file

    palabras = getTextPdf(filename).split(" ")

    badwords = load_bad_words("SPANISH")

    badwords = set(badwords)
    palabras = set(palabras)


    cant = badwords & palabras

    return len(cant), len(palabras)

def fullAnalisisDocx(file):

    filename = "../public/docs/"+ file

    palabras = getTextDOCX(filename).split(" ")

    badwords = load_bad_words("SPANISH")

    badwords = set(badwords)
    palabras = set(palabras)


    cant = badwords & palabras

    return len(cant), len(palabras)
