from base64 import standard_b64encode, standard_b64decode
from os import system
from sys import stdin
from pyaes import AESModeOfOperationCTR

# required functions


def readFile(path):
  with open(path, mode='rb') as file:
    data = file.read()
  return data


def writeFile(path, data):
  with open(path, mode='wb') as file:
    file.write(data)


def encrypt(message, key):
  return AESModeOfOperationCTR(key).encrypt(message)


def decrypt(cipherImage, key):
  return AESModeOfOperationCTR(key).decrypt(cipherImage)


# required input data

print "Enter the key (128, 192 or 256 bytes):\t",
key = stdin.readline().strip()

print "Enter name of the image:\t",
inputImage = stdin.readline().strip()

print "Enter name output image:\t",
outputImage = stdin.readline().strip()

# validation

if len(key) != 16 and len(key) != 24 and len(key) != 32:
  print "Key invalid"
  exit()

# homework

# read bits
message = readFile(inputImage)
# cipher image
imageCipher = encrypt(message, key)
# encode in base 64
imageCipher64 = standard_b64encode(imageCipher)

# show representation
print "The message in base 64 is:\t" + imageCipher64

# decode in base 64
imageCipher = standard_b64decode(imageCipher64)

# write image
writeFile(outputImage, decrypt(imageCipher, key))

# open image
system("xdg-open " + outputImage)
