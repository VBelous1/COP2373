# Exercise 7 - Vanessa Belous

import re

# this function uses a complex regular expression to identify sentences in a paragraph
def analyze_paragraph(paragraph):
    pattern = r'[A-Z\d].*?[.!?](?= [A-Z\d]|$)'
    # stores the sentences in a list
    sentences_list = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)
    # displays how many sentences are in the paragraph
    print("\nThere are", len(sentences_list), "sentences in your paragraph:")
    # returns the list of sentences so that another function can use it
    return sentences_list

# this function will print every sentence found in the user's paragraph using a for loop
def print_sentences(sentences_list):
    for sentence in sentences_list:
        print('\t->', sentence)

def main():
    print("Vanessa's Sentence Counter")
    paragraph = input("Enter a paragraph: ")

    # calls the function that finds the individual sentences in the paragraph, assigning the result to a variable
    sentences_list = analyze_paragraph(paragraph)
    # call to the function that will print the sentences in a formatted manner
    print_sentences(sentences_list)

main()