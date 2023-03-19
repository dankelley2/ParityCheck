

# Sample code to practice error correction algorithms (Hamming Codes)
# Right now this is using bytes instead of bits, which does not make sense, but I will change it soon.

# Create sample data as a char
data = "This is a much longer string of data that will print in multiple lines"

# Generate Byte array from the data
data_bytes = bytearray(data, 'utf-8')

# Reserve a unsigned 8 bit integer for the length of the data
data_bytes.insert(0, len(data_bytes))

# Pad data_bytes with 0's to make it a multiple of 11
while len(data_bytes) % 11 != 0:
    data_bytes.append(0)

# Split the data_bytes into 11 bit chunks
data_chunks = [data_bytes[i:i+11] for i in range(0, len(data_bytes), 11)]

# Loop through each chunk
for chunk in data_chunks:
    # Insert the extendend parity bit
    chunk.insert(0, 0)

    # Insert 4 parity bits into the chunk
    chunk.insert(1, 0)
    chunk.insert(2, 0)
    chunk.insert(4, 0)
    chunk.insert(8, 0)

    # Calculate the parity bits for index 1
    chunk[1] = chunk[3] ^ chunk[5] ^ chunk[7] ^ chunk[9] ^ chunk[11] ^ chunk[13] ^ chunk[15]

    # Calculate the parity bits for index 2
    chunk[2] = chunk[3] ^ chunk[6] ^ chunk[7] ^ chunk[10] ^ chunk[11] ^ chunk[14] ^ chunk[15]

    # Calculate the parity bits for index 4
    chunk[4] = chunk[5] ^ chunk[6] ^ chunk[7] ^ chunk[12] ^ chunk[13] ^ chunk[14] ^ chunk[15]
    
    # Calculate the parity bits for index 8
    chunk[8] = chunk[9] ^ chunk[10] ^ chunk[11] ^ chunk[12] ^ chunk[13] ^ chunk[14] ^ chunk[15]

    # Calculate the extended parity bit at index 0 using all other bits
    chunk[0] = chunk[1] ^ chunk[2] ^ chunk[4] ^ chunk[8] ^ chunk[3] ^ chunk[5] ^ chunk[6] ^ chunk[7] ^ chunk[9] ^ chunk[10] ^ chunk[11] ^ chunk[12] ^ chunk[13] ^ chunk[14] ^ chunk[15]

    # Print the chunk to the console as a single line of 16 bits
    print(chunk.hex())
    print()
