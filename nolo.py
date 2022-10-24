# Nolo v1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0
# why did i put alot of 0

from translate import Translator
from os.path import exists

def ifelseret(test,one,two):
  return one if test else two


def resultof(code):
  try:
    code()
  except:
    return False
  return True
def write(fn, text):
  bro = resultof(open(fn, "w"))
  try:
      f = open(fn, "w")
      f.write(text)
  except:
      f = open(fn, "x")
      f.write(text)
     
     
print("""
  _   _ 
 | \ | |
 |  \| |
 | . ` |
 | |\  |
 |_| \_|olo
 v1.0
""")

print("Welcome to Nolo! Pulling up the config file...")

if (exists(".nolo")):
  print("We found your nolo config file!")
  f = open(".nolo", "r")
  r = f.read()
  s = r.split("\n")
  lang = s[1-1]
else:
  print("Welcome to Nolo! Let's begin setting up Nolo, so you're comfortable.")
  print("""
  Let's start with the language. Enter a valid language code.
  """)
  lang = input(": ")
  f = open(".nolo", "w")
  f.write(lang)
  f.close()

print(Translator(lang).translate("""
Choose an option:
[1] Config
[2] Create Node.js File
"""))
u = input(": ")

if (u == "1"):
  print(Translator(lang).translate("Enter new language code:"))
  lang = input(": ")
  f = open(".nolo", "w")
  f.write(lang)
  f.close()
  print(Translator(lang).translate("Done!"))
else: 
  if (u == "2"):
    print(Translator(lang).translate("""
    [1] Hello World
    [2] Socket.io-client bot
    """))
    u = input(": ")
    if (u == "1"):
      write("scripts/helloworld.js", "console.log(\""+Translator(lang).translate("Hello World! - Nolo")+"\")")
    if (u == "2"):
      print(Translator(lang).translate("Coming soon!"))
  else:
    print(Translator(lang).translate("Invalid option!"))