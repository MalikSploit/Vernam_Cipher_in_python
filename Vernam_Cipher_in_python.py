from random import randint
import matplotlib.pylab as plt

# We need the Alphabet because we convert letters into numerical values
# So that we can use mathematical operation (note we encrypt the spaces as well)
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

#These are the letters we are interested in when dealing with frequency-analysis
#Space is almost always the most frequent 'Letter' in the Alphabet !!!
LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'  


def random_sequence(text):
    random = []
    for i in range(len(text)):
        random.append(randint(0, len(ALPHABET)-1))
    return random


# Vernam encryption
def encrypt(text, key):
    text = text.upper()
    cipher_text = ''
    # Consider all the plain_text letters : enumerate returns the item + it's index
    for index, char in enumerate(text):
        # The value with which we shift the given letter
        key_index = key[index]
        # The given letter in the plain_text
        char_index = ALPHABET.find(char)
        # Encrypted letter = char's value in the plain_text + random value (+using mod26)
        cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]
    return cipher_text


# Vernam decryption
def decrypt(cipher, key):
    plain_text = ''
    for index, char in enumerate(cipher):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain_text+= ALPHABET[(char_index - key_index) % len(ALPHABET)]
    return plain_text


#The method to do frequency analysis : we just count the occurrences of the given characters
def frequency_analysis(text):
    text = text.upper()
    #We use a dictionary to store the letter-frquency pair
    letter_frequencies = {}

    #Initialize the dictionary (of course with 0 frequencies)
    for letter in LETTERS :
        letter_frequencies[letter] = 0

    #Let's consider the text we want to analyse
    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter]+=1
    return letter_frequencies


def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


if __name__ == '__main__':
    message = 'These are short famous texts in English from classic sources like the Bible or Shakespeare Some texts have word definitions and explanations to help you Some of these texts are written in an old style of English Try to understand them because the English that we speak today is based on what our great great great great grandparents spoke before Of course not all these texts were originally written in English The Bible for example is a translation But they are all well known in English today and many of them express beautiful thoughts An administrator is a person who ensures that an organization operates efficiently Their specific duties depend on the type of company organization or entity where they work Above all administrators need to be highly organized and have good communication skills One who operates an engine The definition of an engineer is a person who uses science math and creativity to solve technical problems An example of an engineer is a person who designs a low cost system to produce a specific product An administrator is a person who ensures that an organization operates efficiently Their specific duties depend on the type of company organization or entity where they work Above all administrators need to be highly organized and have good communication skills '
    sequence = random_sequence(message)
    print("The original message is : %s\n" % message.upper())
    cipher = encrypt(message, sequence)
    print("Encrypted message is : %s\n" % cipher)
    decrypted_text = decrypt(cipher, sequence)
    print("Decrypted message is : %s\n" % decrypted_text)
    # We can see that they are no information leaking, because the occurence of letters are evenly distributed, therefore we cannot know which letter is mostly used.
    plot_distribution(frequency_analysis(cipher)) 
