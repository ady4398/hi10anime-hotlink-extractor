import re
import codecs
import pyperclip
import sys

if len(sys.argv) < 2:
    raise ValueError("Usage: >>>python stringXtractor.py example.html")

htmlfile = str(sys.argv[1])
html = codecs.open(htmlfile, 'r', 'utf-8')

text = html.read()
my_file = open('links.txt', '+w')

for m in re.finditer('https://sinbad.hi10anime.com(.+?)">', text):
    foundtext = m.group(0)
    if foundtext.find('jtoken') != -1 or foundtext.find('btoken') != -1:
        my_file.write(m.group(0).replace('">','') + "\n")

for m in re.finditer('https://masrur.hi10anime.com(.+?)">', text):
    foundtext = m.group(0)
    if foundtext.find('jtoken') != -1 or foundtext.find('btoken') != -1:
        my_file.write(m.group(0).replace('">','') + "\n")
    
html.close()
my_file.close()

my_file2 = open('links.txt', 'r')
paperclip = my_file2.read()
pyperclip.copy(paperclip)

my_file2.close()
print("\nAll Done\n-------\nBatch Links Copied to Clipboard\n-------\nExtracted from " + htmlfile)
