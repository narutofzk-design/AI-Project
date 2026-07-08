"""
Chatbot Logic Module
Uses keyword matching to generate responses.
No AI/ML libraries needed - just simple string matching.
"""


# Dictionary of keywords mapped to responses
# The bot checks if any keyword exists in the user's message
KEYWORD_RESPONSES = {
    # Greetings
    'hello': "Hello! I'm your Study Assistant. How can I help you today?",
    'hi': "Hi there! Ready to help you study. What do you need?",
    'hey': "Hey! What can I help you with today?",

    # Study help
    'exam': "Exams can be stressful! Here are some tips:\n1. Start early - don't cram\n2. Use active recall (test yourself)\n3. Take breaks every 45 minutes\n4. Get enough sleep before the exam",
    'test': "For test preparation, try the Pomodoro technique: study for 25 minutes, then take a 5-minute break. After 4 rounds, take a longer break.",
    'study': "Here are effective study strategies:\n1. Summarize notes in your own words\n2. Teach the material to someone else\n3. Use flashcards for key terms\n4. Practice with past papers",
    'focus': "To improve focus:\n1. Remove distractions (phone on silent)\n2. Study in a quiet space\n3. Use the Pomodoro technique\n4. Stay hydrated and take breaks",
    'concentrate': "Having trouble concentrating? Try:\n1. Breaking tasks into smaller chunks\n2. Setting specific goals for each session\n3. Using background white noise\n4. Exercising before studying",

    # Emotional support
    'stress': "Feeling stressed? That's normal! Try:\n1. Deep breathing exercises\n2. Take a short walk\n3. Break your work into smaller tasks\n4. Talk to a friend or counselor",
    'anxious': "Anxiety before studying is common. Try:\n1. Start with the easiest task first\n2. Set realistic goals\n3. Practice mindfulness\n4. Remember - progress is more important than perfection",
    'tired': "Feeling tired? Here's what might help:\n1. Take a 20-minute power nap\n2. Go for a short walk outside\n3. Have some water (dehydration causes fatigue)\n4. Switch to a different subject for variety",
    'overwhelmed': "Feeling overwhelmed is okay! Try:\n1. Write down everything you need to do\n2. Pick the most urgent task first\n3. Break it into tiny steps\n4. Celebrate small wins!",
    'bored': "Bored with studying? Try:\n1. Change your study location\n2. Use different study methods (videos, diagrams)\n3. Study with a friend\n4. Set a reward for finishing",

    # Schedule related
    'schedule': "Need help with scheduling? Try our Study Planner tool! It can create a balanced study schedule for you based on your subjects and available time.",
    'plan': "Planning is key to success! Use our Study Planner feature to create a personalized schedule. Just enter your subjects and available hours.",
    'time': "Time management tips:\n1. Use a planner or calendar\n2. Set specific study times\n3. Prioritize important subjects\n4. Don't multitask - focus on one thing at a time",

    # Tools
    'quiz': "Want to test yourself? Try our Quiz feature! Select a topic and challenge yourself with multiple-choice questions.",
    'summarize': "Need to summarize something? Use our Text Summarizer tool! Just paste your text and it will extract the key sentences.",
    'summary': "Our Summarizer tool can help you condense long texts into key points. Give it a try!",

    # Farewell
    'thanks': "You're welcome! Good luck with your studies!",
    'thank you': "Happy to help! Keep up the great work!",
    'bye': "Goodbye! Remember: consistency beats intensity. Study a little every day!",
    'goodbye': "See you later! You've got this!",

    # Subjects
    'math': "For math, practice is everything! Work through problems step by step, and don't skip the basics. Khan Academy is a great free resource.",
    'science': "For science subjects, focus on understanding concepts rather than memorizing. Draw diagrams, do experiments when possible, and relate topics to real life.",
    'english': "For English/writing, read widely, practice writing regularly, and always proofread your work. Reading improves vocabulary naturally!",
    'history': "For history, create timelines, make connections between events, and try to understand WHY things happened, not just WHAT happened.",
    'programming': "For programming, the best way to learn is by doing! Write code every day, even if it's small programs. Debug errors patiently - they teach you the most.",

    # Help
    'help': "I can help you with:\n1. Study tips and strategies\n2. Time management advice\n3. Dealing with exam stress\n4. Pointing you to our tools (Planner, Quiz, Summarizer)\nJust ask me anything!",
}

# Fallback responses when no keyword matches
FALLBACK_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Hmm, I don't have info on that. Try asking about study tips, exams, or scheduling!",
    "I'm still learning! Try asking about study strategies, exam prep, or time management.",
    "Could you be more specific? I can help with study tips, stress, scheduling, and more.",
]

# Keep track of which fallback to use (cycles through them)
_fallback_index = 0


def get_response(message):
    """
    Takes a user message and returns a bot response.
    Uses keyword matching - checks if any keyword is in the message.

    Args:
        message (str): The user's input message

    Returns:
        str: The bot's response
    """
    global _fallback_index

    # Convert to lowercase for matching
    message_lower = message.lower().strip()

    # Check each keyword against the message
    # We check longer phrases first to avoid partial matches
    sorted_keywords = sorted(KEYWORD_RESPONSES.keys(), key=len, reverse=True)

    for keyword in sorted_keywords:
        if keyword in message_lower:
            return KEYWORD_RESPONSES[keyword]

    # No keyword matched - use a fallback response
    response = FALLBACK_RESPONSES[_fallback_index]
    _fallback_index = (_fallback_index + 1) % len(FALLBACK_RESPONSES)
    return response
