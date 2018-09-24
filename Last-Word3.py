import codecs
file1=codecs.open("Last.txt","r","utf-8")

lines = file1.read().split("\n")
print(lines)