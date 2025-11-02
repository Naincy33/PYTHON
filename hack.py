import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define a dictionary to store the emotional states and their corresponding questions
emotional_states = {
    "happy": ["What's making you happy today?", "What's your favorite hobby?", "What's the best thing that's happened to you recently?"],
    "sad": ["What's been on your mind lately?", "What's been making you feel down?", "What's something you're looking forward to?"],
    "angry": ["What's been frustrating you lately?", "What's something that's making you feel angry?", "What's something you're passionate about?"],
    "neutral": ["How's your day going so far?", "What's been on your mind lately?", "What's something you're grateful for?"]
}

# Define a function to ask the user questions and analyze their emotional state
def analyze_emotional_state():
    emotional_state = None
    while emotional_state is None:
        # Ask the user a random question from the emotional state dictionary
        question = random.choice(random.choice(emotional_states.values()))
        user_response = input(question + " ")

        # Analyze the user's response to determine their emotional state
        sentiment = sia.polarity_scores(user_response)
        if sentiment['compound'] > 0.5:
            emotional_state = "happy"
        elif sentiment['compound'] < -0.5:
            emotional_state = "sad"
        else:
            emotional_state = "neutral"

    # Print out the user's emotional state
    print("Based on your responses, it seems like you're feeling " + emotional_state + ".")

# Run the chatbot
analyze_emotional_state()