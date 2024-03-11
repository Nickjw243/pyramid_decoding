def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    message_words = {}
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            number, word = parts
            message_words[int(number)] = word

    pyramid = []
    current_number = 1
    while current_number in message_words:
        pyramid.append(list(range(current_number, current_number + len(pyramid) + 1)))
        current_number += len(pyramid)
    print(pyramid)

    decoded_message = ' '.join(message_words[pyramid[i][-1]] for i in range(len(pyramid)))
    
    return decoded_message

decoded_message = decode('Textfile.txt')
print(decoded_message)