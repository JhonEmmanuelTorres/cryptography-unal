# functions

def rotate(current_address, coordinates)
  if LEFT == current_address
    for i in 0...SIZE
      coordinates[i][0], coordinates[i][1] = coordinates[i][1], coordinates[i][0]
      coordinates[i][1] = SIZE - coordinates[i][1] - 1
    end
  else
    for i in 0...SIZE
      coordinates[i][0], coordinates[i][1] = coordinates[i][1], coordinates[i][0]
      coordinates[i][0] = SIZE - coordinates[i][0] - 1
    end
  end
end

def build_message(container)
  message = ''
  container.each do |e|
    e.each do |f|
      if f
        message += f
      end
    end
  end
  return message
end

# Constants
LEFT = CIPHER = 0

# read input
print "Enter the SIZE of the grid:\t"
SIZE = gets.chomp.to_i

print "Enter the address of the rotation (0 = left, 1 = right):\t"
address = gets.chomp.to_i

print "Enter the mode (0 = cipher, 1 = decipher):\t"
mode = gets.chomp.to_i

print "Enter the number of holes:\t"
holes = gets.chomp.to_i

print "Enter the coordinates of the holes line by line (index begin with 0):\t"
coordinates = Array.new(holes)
for i in 0...holes
  x, y = gets.chomp.split.map(&:to_i)
  coordinates[i] = [x, y]
end

print "Enter the message to cipher or decipher:\t"
message = gets.chomp.split.join.upcase
if message.length < SIZE ** 2
  message += 'X' * (SIZE ** 2) - message.length
end

container = Array.new(SIZE).map { |e| e = Array.new(SIZE) }

# Algorithm

if mode == CIPHER

  index_string = 0
  # rotate
  4.times do
    coordinates.sort!
    coordinates.each do |a, b|
      if container[a][b].nil? # valide the pos is empty
        container[a][b] = message[index_string]
        index_string += 1
      end
    end
    rotate(address, coordinates)
  end

  message = build_message(container)
  puts "The message ciphered is: #{message}"
  print container

else

  # fill matrix
  message.each_char.with_index do |item, index|
    container[index / SIZE][index % SIZE] = item
  end
  # aux container to not replace value
  aux_container = Array.new(SIZE).map { |e| e = Array.new(SIZE, true) }
  print container,"\n"
  message = ''
  4.times do
    coordinates.sort!
    coordinates.each do |a, b|
      if !container[a][b].nil? and aux_container[a][b] # valide the pos is empty
        message += container[a][b]
        aux_container[a][b] = false
      end
    end
    rotate(address, coordinates)
  end

  puts "The message deciphered is: #{message}"

end
