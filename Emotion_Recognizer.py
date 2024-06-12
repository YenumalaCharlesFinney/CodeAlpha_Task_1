# Function to classify sentence emotions
def classify_emotion(sentence):
    sentence = sentence.lower()

    if 'happy' in sentence or 'joy' in sentence or 'excited' in sentence:
        return 'Happy'
    elif 'angry' in sentence or 'mad' in sentence or 'frustrated' in sentence:
        return 'Angry'
    elif '?' in sentence:
        return 'Question'
    elif 'sad' in sentence or 'depressed' in sentence or 'unhappy' in sentence or 'hate' in sentence:
        return 'Sad'
    elif 'trust' in sentence or 'trusting' in sentence or 'trusted' in sentence:
        return 'Trust'
    elif 'love' in sentence or 'loving' in sentence or 'affectionate' in sentence:
        return 'Love'
    else:
        return 'Neutral'


# Define the emotions that the system can detect
emotions = ['Happy', 'Angry', 'Question', 'Sad', 'Trust', 'Love', 'Neutral']

# Mention the emotions the system can detect
print("This system can detect emotions such as:", ", ".join(emotions))

# Prompt the user to enter a sentence
user_sentence = input("Enter a sentence: ")

# Classify the user's sentence
emotion = classify_emotion(user_sentence)
print(f"The sentence '{user_sentence}' is classified as: {emotion}")
