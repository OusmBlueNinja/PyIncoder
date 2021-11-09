import Encoder


inarg = input('would you like to Encode (type encode), or decode (type decode) >>')
if inarg == 'encode':
  Encoder.Encode(input('scrabble your password >>'))
elif inarg == 'decode':
  Encoder.Decode(input('Enter your encoded password >>'))
else:
  print('Error invalid option')