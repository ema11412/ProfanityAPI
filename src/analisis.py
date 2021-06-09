import csv

from utils import *
import os




def fullAnalisisTxt(file):

    filename = "../public/docs/"+ file

    palabras = []

    with open(filename) as fname:
        for lineas in fname:
            palabras.extend(lineas.split())


    badwords = load_bad_words("SPANISH")

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
