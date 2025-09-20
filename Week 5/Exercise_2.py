# Exercise 2 - Vanessa Belous

# Global Variables
spam_score = 0
message = ''
spam_in_email_list = []
spam_words_list = ['free', 'act now', 'urgent', 'guaranteed', 'cash', 'click here', 'dear friend', 'no risk', 'earn money', 'save big',
                   'best price', 'bonus', 'miracle', 'breakthrough', 'life-changing', 'unbelievable', 'phenomenal', 'weight loss', 'medicine', 'cure'
                   'limited time', 'hurry', 'expires', 'last chance', 'special deal', 'compare rates', 'discount', 'confidentiality', 'full refund',
                   'what are you waiting for']

# Iterates through list of spam words to check if they are in the email
def check_for_spam():
    global message
    global spam_score
    global spam_in_email_list

    for word in spam_words_list:
        if word in message:
            spam_in_email_list.append(word)
            spam_score += 1
        else:
            continue

# calculates the likelihood the email is spam, using the accumulated spam score and the length of the email
def likelihood_spam():
    global spam_score
    global message

    words_in_message = len(message.split())
    likelihood = round((spam_score / words_in_message) * 100, 2)
    return likelihood

def main():
    global message

    message = str.lower(input("Enter the email message you'd like to check for spam: "))

    check_for_spam()
    likelihood = likelihood_spam()

    print("\nSpam Score: ", spam_score)
    print("There is a ", likelihood, "% chance your message is spam.")

    # first evaluates if there were spam words at all before listing flagged words
    print("\nThe following words/phrases were flagged as spam: ")
    if not spam_in_email_list:
        print("\tNo words were flagged as spam!")
    else:
        for word in spam_in_email_list:
            print("\t-", word)


main()