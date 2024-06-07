'''
Write a program to manipulate pdf files using pyPDF. 
Your programs should be able to merge multiple pdf files into a single pdf. 
You are welcome to add more functionalities

pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and 
transforming the pages of PDF files. 
It can also add custom data, viewing options, and passwords to PDF files. 
pypdf can retrieve text and metadata from PDFs as well.
'''

from pypdf import PdfWriter
import os

merger = PdfWriter()

files = os.listdir("Day 71-80/Day 76")

for file in files:
    if file.endswith(".pdf"):
        print(file)
        merger.append(f"Day 71-80/Day 76/{file}")
    
merger.write("Day 71-80/Day 76/merged-pdf.pdf")
merger.close()