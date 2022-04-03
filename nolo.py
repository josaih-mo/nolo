# Nolo v1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0
# why did i put alot of 0
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
  with open(fn, ifelseret(bro,"w","x")) as f:
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
print("""
[1] Hello World
[2] Socket.io-client bot
""")
u = input(": ")
if (u == "1"):
  write("helloworld.js", "console.log(\"Hello World! - Nolo\")")
if (u == "2"):
  print("Coming soon")
