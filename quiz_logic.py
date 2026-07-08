"""
Quiz Logic Module
Contains a static question bank organized by topic.
Uses random.sample() to pick questions.
Scoring compares submitted answers against stored correct answers.
"""

import random


# ============================================================
# QUESTION BANK
# Each topic has a list of questions with options and correct answer
# ============================================================
QUESTION_BANK = {
    'Python Programming': [
        {
            'question': 'What is the correct way to create a variable in Python?',
            'options': ['var x = 5', 'x = 5', 'int x = 5', 'x := 5'],
            'correct': 'x = 5'
        },
        {
            'question': 'Which of these is a Python data type?',
            'options': ['integer', 'string', 'list', 'All of the above'],
            'correct': 'All of the above'
        },
        {
            'question': 'What does the len() function do?',
            'options': ['Returns the length of an object', 'Creates a new list',
                        'Converts to integer', 'Prints text'],
            'correct': 'Returns the length of an object'
        },
        {
            'question': 'How do you start a comment in Python?',
            'options': ['//', '#', '/*', '--'],
            'correct': '#'
        },
        {
            'question': 'What is the output of print(2 ** 3)?',
            'options': ['6', '8', '5', '9'],
            'correct': '8'
        },
        {
            'question': 'Which keyword is used to define a function in Python?',
            'options': ['function', 'def', 'func', 'define'],
            'correct': 'def'
        },
        {
            'question': 'What does the append() method do for lists?',
            'options': ['Removes an item', 'Adds an item to the end',
                        'Sorts the list', 'Reverses the list'],
            'correct': 'Adds an item to the end'
        },
        {
            'question': 'Which of these is the correct if statement syntax?',
            'options': ['if x == 5:', 'if (x == 5)', 'if x = 5 then', 'if x == 5 then:'],
            'correct': 'if x == 5:'
        },
        {
            'question': 'What is a Python dictionary?',
            'options': ['An ordered list', 'A key-value pair collection',
                        'A type of loop', 'A function'],
            'correct': 'A key-value pair collection'
        },
        {
            'question': 'How do you create a for loop that runs 5 times?',
            'options': ['for i in range(5):', 'for(i=0; i<5; i++)',
                        'for i = 1 to 5', 'loop 5 times:'],
            'correct': 'for i in range(5):'
        },
    ],

    'General Science': [
        {
            'question': 'What is the chemical symbol for water?',
            'options': ['H2O', 'CO2', 'NaCl', 'O2'],
            'correct': 'H2O'
        },
        {
            'question': 'What planet is known as the Red Planet?',
            'options': ['Venus', 'Mars', 'Jupiter', 'Saturn'],
            'correct': 'Mars'
        },
        {
            'question': 'What is the speed of light approximately?',
            'options': ['300,000 km/s', '150,000 km/s', '500,000 km/s', '100,000 km/s'],
            'correct': '300,000 km/s'
        },
        {
            'question': 'What is the powerhouse of the cell?',
            'options': ['Nucleus', 'Mitochondria', 'Ribosome', 'Cell membrane'],
            'correct': 'Mitochondria'
        },
        {
            'question': 'What gas do plants absorb from the atmosphere?',
            'options': ['Oxygen', 'Nitrogen', 'Carbon Dioxide', 'Hydrogen'],
            'correct': 'Carbon Dioxide'
        },
        {
            'question': 'What is Newton\'s First Law about?',
            'options': ['Force = Mass x Acceleration', 'Objects at rest stay at rest',
                        'Every action has a reaction', 'Energy cannot be created'],
            'correct': 'Objects at rest stay at rest'
        },
        {
            'question': 'How many bones are in the adult human body?',
            'options': ['106', '206', '306', '156'],
            'correct': '206'
        },
        {
            'question': 'What is the largest organ in the human body?',
            'options': ['Heart', 'Liver', 'Skin', 'Brain'],
            'correct': 'Skin'
        },
    ],

    'Mathematics': [
        {
            'question': 'What is the value of Pi (to 2 decimal places)?',
            'options': ['3.14', '3.16', '3.12', '3.18'],
            'correct': '3.14'
        },
        {
            'question': 'What is the square root of 144?',
            'options': ['10', '11', '12', '14'],
            'correct': '12'
        },
        {
            'question': 'What is 15% of 200?',
            'options': ['25', '30', '35', '20'],
            'correct': '30'
        },
        {
            'question': 'What is the formula for the area of a circle?',
            'options': ['2*pi*r', 'pi*r^2', 'pi*d', '2*pi*r^2'],
            'correct': 'pi*r^2'
        },
        {
            'question': 'What type of angle is exactly 90 degrees?',
            'options': ['Acute', 'Right', 'Obtuse', 'Straight'],
            'correct': 'Right'
        },
        {
            'question': 'What is the next prime number after 7?',
            'options': ['8', '9', '10', '11'],
            'correct': '11'
        },
        {
            'question': 'What is 3! (3 factorial)?',
            'options': ['3', '6', '9', '12'],
            'correct': '6'
        },
        {
            'question': 'In a right triangle, what is the longest side called?',
            'options': ['Adjacent', 'Opposite', 'Hypotenuse', 'Base'],
            'correct': 'Hypotenuse'
        },
    ],

    'Study Skills': [
        {
            'question': 'What is the Pomodoro Technique?',
            'options': ['A cooking method', 'A study timer method (25 min work, 5 min break)',
                        'A memorization trick', 'A type of exam'],
            'correct': 'A study timer method (25 min work, 5 min break)'
        },
        {
            'question': 'What is active recall?',
            'options': ['Reading notes repeatedly', 'Testing yourself from memory',
                        'Highlighting text', 'Listening to lectures'],
            'correct': 'Testing yourself from memory'
        },
        {
            'question': 'What is spaced repetition?',
            'options': ['Studying everything in one day',
                        'Reviewing material at increasing intervals',
                        'Repeating words out loud',
                        'Spacing out your desk'],
            'correct': 'Reviewing material at increasing intervals'
        },
        {
            'question': 'Which is generally MORE effective for learning?',
            'options': ['Re-reading notes', 'Highlighting everything',
                        'Practice testing', 'Copying notes word-for-word'],
            'correct': 'Practice testing'
        },
        {
            'question': 'How much sleep do most students need for optimal learning?',
            'options': ['4-5 hours', '5-6 hours', '7-9 hours', '10-12 hours'],
            'correct': '7-9 hours'
        },
        {
            'question': 'What is mind mapping?',
            'options': ['A GPS technique', 'A visual diagram linking ideas',
                        'A type of meditation', 'A reading speed technique'],
            'correct': 'A visual diagram linking ideas'
        },
        {
            'question': 'What should you do if you don\'t understand something in class?',
            'options': ['Ignore it', 'Ask questions or seek help',
                        'Skip that topic', 'Wait until the exam'],
            'correct': 'Ask questions or seek help'
        },
    ],
}


def get_available_topics():
    """
    Returns a list of all available quiz topics.

    Returns:
        list: List of topic name strings
    """
    return list(QUESTION_BANK.keys())


def get_random_questions(topic, n=5):
    """
    Picks n random questions from the specified topic.

    Args:
        topic (str): The topic to get questions from
        n (int): Number of questions to return (default 5)

    Returns:
        list: List of question dicts, or empty list if topic not found
    """
    if topic not in QUESTION_BANK:
        return []

    available = QUESTION_BANK[topic]

    # Don't try to pick more questions than available
    n = min(n, len(available))

    return random.sample(available, n)


def score_quiz(submitted_answers, correct_answers):
    """
    Compares submitted answers against correct answers.

    Args:
        submitted_answers (dict): {question_index: selected_answer}
        correct_answers (dict): {question_index: correct_answer}

    Returns:
        dict: {'score': int, 'total': int, 'percentage': float}
    """
    score = 0
    total = len(correct_answers)

    for key, correct in correct_answers.items():
        if submitted_answers.get(key) == correct:
            score += 1

    percentage = round((score / total) * 100, 1) if total > 0 else 0

    return {
        'score': score,
        'total': total,
        'percentage': percentage
    }
