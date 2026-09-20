# Name: Maribel Rivera
# Date: September 20, 2026
# Program: Spam Scanner. Calculates spam score based on keyword matches in an email message.

# Function: get_spam_keywords
# Returns a list of 30 common spam words/phrases.
def get_spam_keywords():
    return [
        "free", "winner", "cash", "prize", "credit", "loan",
        "urgent", "act now", "limited time", "click here",
        "congratulations", "claim", "offer", "cheap", "discount",
        "guarantee", "risk-free", "bonus", "earn money", "income",
        "investment", "no fees", "save big", "order now",
        "exclusive", "gift", "win", "money back", "apply now"
    ]

# Function: scan_message
# Parameters: message (string), keywords (list)
# Returns: spam_score (int), matched_words (list)
def scan_message(message, keywords):
    message_lower = message.lower()
    spam_score = 0
    matched_words = []

    # Check each keyword in the message
    for word in keywords:
        if word in message_lower:
            spam_score += 1
            matched_words.append(word)

    return spam_score, matched_words

# Function: rate_spam
# Parameters: score (int)
# Returns: likelihood message (string)
def rate_spam(score):
    if score == 0:
        return "This message is NOT likely to be spam."
    elif score <= 5:
        return "This message is somewhat suspicious."
    elif score <= 15:
        return "This message is likely spam."
    else:
        return "This message is DEFINITELY spam!"

# Main Program
def main():
    print("=== Spam Scanner Program ===")
    print()

    # Get user message
    user_message = input("Enter the email message you want to scan:\n")

    # Load keywords
    keywords = get_spam_keywords()

    # Scan message
    score, matched = scan_message(user_message, keywords)

    # Rate spam likelihood
    likelihood = rate_spam(score)

    # Display results
    print("\n=== Scan Results ===")
    print(f"Spam Score: {score}")
    print(f"Likelihood: {likelihood}")

    if matched:
        print("\nKeywords/Phrases Found:")
        for word in matched:
            print(f"- {word}")
    else:
        print("\nNo spam keywords were found in the message.")

# Run the program
main()
