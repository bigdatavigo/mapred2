#!/usr/bin/python3
import sys

for linea in sys.stdin:
    linea=linea.strip()
    palabras=linea.split()
    for palabra in palabras:
        print(palabra+"\t"+"1")