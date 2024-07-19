from PyPDF2 import PdfWriter
import os

def find(name, path):
    if(name == "q.pdf" or name == "Q.pdf"):
        exit()
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    print("No file found")
    return None

merger = PdfWriter()

while(True):
    fileA = find(input("Enter the name of the 1st pdf file you want (Q to quit): ")+".pdf", os.getcwd())
    if(fileA == None):
        continue
    fileB = find(input("Enter the name of the 2nd pdf file you want: ")+".pdf", os.getcwd())
    if(fileB == None):
        continue
    merger.append(fileA)
    merger.append(fileB)
    merger.write("merged-pdf.pdf")
    merger.close
    print("Files merged as merged-pdf.pdf")
    



