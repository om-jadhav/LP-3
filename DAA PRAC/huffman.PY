# Huffman Encoding using Greedy Method

# Create Huffman codes
def huffman_encoding(text):

    # Count frequency of each character
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    # Create nodes
    nodes = [[freq, char] for char, freq in frequency.items()]

    # Build Huffman Tree
    while len(nodes) > 1:

        # Find node with smallest frequency
        nodes.sort()

        left = nodes.pop(0)
        right = nodes.pop(0)

        # Merge the two nodes
        merged = [left[0] + right[0], left, right]

        nodes.append(merged)

    # Generate Huffman codes
    codes = {}

    def generate_codes(node, code=""):

        if isinstance(node[1], str):
            codes[node[1]] = code
            return

        generate_codes(node[1], code + "0")
        generate_codes(node[2], code + "1")

    generate_codes(nodes[0])

    # Encode the text
    encoded_text = ""

    for char in text:
        encoded_text += codes[char]

    return codes, encoded_text


# Input
text = input("Enter text: ")

# Huffman Encoding
codes, encoded_text = huffman_encoding(text)

# Display Huffman Codes
print("\nHuffman Codes:")

for char, code in codes.items():
    print(char, ":", code)

# Display encoded text
print("\nEncoded Text:", encoded_text)