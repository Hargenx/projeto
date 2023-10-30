def split_lines(s):
  return s.split('\n')


print("String original:")
txt = "Esta\né uma\nstring\ncom quebra\n de \nlinha.\n"
print(txt)
print("Dividindo a string em uma lista de linhas: ")
t = txt.splitlines(True)
print(t)
