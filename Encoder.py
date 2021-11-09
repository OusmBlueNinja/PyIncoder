import os, timeit

def Encode(password2):
  while 1:
    try:
      os.remove("password.encript")
      break
    except:
      break
  
  print("DO NOT USE ' or backslash oposite of this >>  /")
  password = password2
  val = 0
  passlen = len(password)
  list = []
  start = timeit.timeit()
  for passlen in password:
    curent = password[val].lower()
    val = val + 1
    print(curent, 'has been procesed')
    if curent == '1':
      list.append('73s6')
    elif curent == '2':
      list.append('g5y7')
    elif curent == '3':
      list.append('h839')
    elif curent == '4':
      list.append('1732')
    elif curent == '5':
      list.append('hijk')
    elif curent == '6':
      list.append('heo8')
    elif curent == '7':
      list.append('hidw')
    elif curent == '8':
      list.append('87t6')
    elif curent == '9':
      list.append('876u')
    elif curent == '0':
      list.append('687v')
    elif curent == 'a':
      list.append('0tw8')
    elif curent == 'b':
      list.append('d4k5')
    elif curent == 'c':
      list.append('tqgd')
    elif curent == 'd':
      list.append('af39')
    elif curent == 'e':
      list.append('p0s9')
    elif curent == 'f':
      list.append('4vxp')
    elif curent == 'g':
      list.append('ak3p')
    elif curent == 'h':
      list.append('kqan')
    elif curent == 'i':
      list.append('3ep7')
    elif curent == 'j':
      list.append('5sg8')
    elif curent == 'k':
      list.append('up7b')
    elif curent == 'l':
      list.append('8ai7')
    elif curent == 'm':
      list.append('nqt1')
    elif curent == 'n':
      list.append('xgsj')
    elif curent == 'o':
      list.append('rczw')
    elif curent == 'p':
      list.append('65cu')
    elif curent == 'q':
      list.append('6o0h')
    elif curent == 'r':
      list.append('qqaa')
    elif curent == 's':
      list.append('jly3')
    elif curent == 't':
      list.append('so4s')
    elif curent == 'u':
      list.append('vlnh')
    elif curent == 'v':
      list.append('h786')
    elif curent == 'w':
      list.append('bcia')
    elif curent == 'x':
      list.append('04i6')
    elif curent == 'y':
      list.append('nvet')
    elif curent == 'z':
      list.append('2vx8')
    elif curent == '!':
      list.append('90q6')
    elif curent == '@':
      list.append('1qcu')
    elif curent == '#':
      list.append('o77v')
    elif curent == '$':
      list.append('hhqe')
    elif curent == '%':
      list.append('fe9x')
    elif curent == '^':
      list.append('cnnc')
    elif curent == '&':
      list.append('6tvt')
    elif curent == '*':
      list.append('794j')
    elif curent == '(':
      list.append('swng')
    elif curent == ')':
      list.append('kq39')
    elif curent == '_':
      list.append('n9fy')
    elif curent == '-':
      list.append('lnx7')
    elif curent == '+':
      list.append('oz4n')
    elif curent == '=':
      list.append('nowt')
    elif curent == '`':
      list.append('iwov')
    elif curent == '~':
      list.append('3n88')
    elif curent == ',':
      list.append('27wz')
    elif curent == '<':
      list.append('27wz')
    elif curent == '.':
      list.append('lvbl')
    elif curent == '>':
      list.append('6bzj')
    elif curent == '/':
      list.append('5m88')
    elif curent == '?':
      list.append('rbhj')
    elif curent == '[':
      list.append('9qo7')
    elif curent == ']':
      list.append('qbws')
    elif curent == '{':
      list.append('o9yw')
    elif curent == '}':
      list.append('r68p')
    elif curent == ':':
      list.append('xnpi')
    elif curent == ';':
      list.append('xnpi')
    elif curent == '"':
      list.append('t85u')
    elif curent == '|':
      list.append('akz2')
    elif curent == ' ':
      list.append(' ')
    else:
      print('Error', curent, 'canot be incoded due to encoder errors')
      
      
    
    
    
      
          
  f = open('password.encript', 'x')
  f.close()
  f = open('password.encript', 'w')
  
  print()
  val2 = 0
  i = len(list)
  for i in list:
    f.write(list[val2])
    val2 = val2 + 1
  
  f.close()
  f = open('password.encript', 'r')
  x = f.read()
  print('new password >> '+ f.read())
  end = timeit.timeit()
  print('incripted in ', start - end, ' Seconds')
  f.close()
  return 'new password >> '+ x

def Decode(inarg):
  print('Error cannot decode ', inarg, 'due to decoder Errors')
  print("")
  print('Error Not Set Up Yet')
  
  