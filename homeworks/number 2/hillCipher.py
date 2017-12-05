from sys import stdin

# extended euclid algorithm


def eea(a, b):
  if b == 0:
    return [a, 1, 0]

  dP, xP, yP = eea(b, a % b)
  d, x, y = dP, yP, xP - int(a / b) * yP
  return [d, x, y]

# greatest common divisor


def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)

# matrix adj2x2


def adj2x2(matrix):
  if len(matrix) == 2:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    return [[d, -b], [-c, a]]

# multiply two matrix


def cipher(message, key):

  if len(key) == 2 and len(message) == 2:
    answer = 2 * [0]
    for i in xrange(2):
      for j in xrange(2):
        answer[i] += message[j] * key[j][i]

    for i in xrange(2):
      answer[i] %= 26

    return answer

# return value char begining sinde 0


def charToNum(char):
  return ord(char) - ord('A')

# return value int


def numToChar(num):
  return chr(ord('A') + num)

# get matrix's determinant


def det2x2(matrix):
  if len(matrix) == 2:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    return a * d - b * c


# read input
line = stdin.readline().strip()
a, b = map(int, stdin.readline().strip().split(' '))
c, d = map(int, stdin.readline().strip().split(' '))

print "The message to encrypt is: " + line

# validate if line's length is odd
odd = False
if len(line) % 2 == 1:
  odd = True
  line += 'A'

# get key
key = [[a, b], [c, d]]
print "The key to encrypt is"
for i in key:
  for j in i:
    print j,
  print
print "\n"
detKey = det2x2(key)

if detKey != 0 and gcd(detKey, 26) == 1:

  # encrypting
  hidden = []
  for i in xrange(0, len(line), 2):
    tmp2Letter = [charToNum(line[i]), charToNum(line[i + 1])]
    hidden += cipher(tmp2Letter, key)

  # get inverse
  inverse = [[d, -b], [-c, a]]
  detAinv = eea(detKey, 26)[1]
  for i in xrange(2):
    for j in xrange(2):
      inverse[i][j] = (inverse[i][j] * detAinv) % 26

  print "The encrypted message is: " + ''.join(map(numToChar, hidden))
  print 'Decrypt message with the key'
  for i in inverse:
    for j in i:
      print j,
    print
  print "\n"

  originalMsg = []
  for i in xrange(0, len(line), 2):
    tmp2Letter = [hidden[i], hidden[i + 1]]
    originalMsg += cipher(tmp2Letter, inverse)

  originalMsg = ''.join(map(numToChar, originalMsg))
  if odd:  # remove auxiliary last element
    originalMsg = originalMsg[:-1]

  print "The original message is: " + originalMsg

else:
  print "You can not encrypt this message with that key :(. Please try with other"
