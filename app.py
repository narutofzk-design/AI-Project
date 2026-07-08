"""
AI-Powered Student Study Assistant
Main Flask Application - app.py
Routes and application configuration
"""

from flask import Flask, render_template, request, session, jsonify, redirect, url_for
import os

# Import our logic modules
from logic.chatbot_logic import get_response
from logic.planner_logic import generate_plan
from logic.quiz_logic import get_random_questions, score_quiz, get_available_topics
from logic.summarizer_logic import summarize_text

# ============================================================
# APP CONFIGURATION
# ============================================================
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for session cookies


# ============================================================
# ROUTE: HOME DASHBOARD
# ============================================================
@app.route('/')
def home():
    """Render the home dashboard with links to all 4 tools."""
    return render_template('home.html')


# ============================================================
# ROUTES: CHATBOT
# ============================================================
@app.route('/chatbot')
def chatbot():
    """Render the chatbot interface."""
    # Initialize chat history in session if it doesn't exist
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('chatbot.html', chat_history=session['chat_history'])


@app.route('/chatbot/ask', methods=['POST'])
def chatbot_ask():
    """Receive user message and return bot reply (JSON for AJAX)."""
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message.strip():
        return jsonify({'reply': 'Please type something!'})

    # Get bot response from our logic module
    bot_reply = get_response(user_message)

    # Store in session history
    if 'chat_history' not in session:
        session['chat_history'] = []

    session['chat_history'].append({'sender': 'user', 'text': user_message})
    session['chat_history'].append({'sender': 'bot', 'text': bot_reply})
    session.modified = True  # Tell Flask the session changed

    return jsonify({'reply': bot_reply})


# ============================================================
# ROUTES: STUDY PLANNER
# ============================================================
@app.route('/planner')
def planner():
    """Show the planner form."""
    return render_template('planner.html')


@app.route('/planner/generate', methods=['POST'])
def planner_generate():
    """Take subjects + hours/days, return generated schedule."""
    # Get form data
    subjects_raw = request.form.get('subjects', '')
    total_hours = request.form.get('total_hours', '10')
    days = request.form.get('days', '7')

    # Parse subjects (comma-separated)
    subjects = [s.strip() for s in subjects_raw.split(',') if s.strip()]

    if not subjects:
        return render_template('planner.html', error='Please enter at least one subject.')

    try:
        total_hours = int(total_hours)
        days = int(days)
    except ValueError:
        return render_template('planner.html', error='Hours and days must be numbers.')

    if total_hours <= 0 or days <= 0:
        return render_template('planner.html', error='Hours and days must be positive numbers.')

    # Generate the study plan using our logic module
    schedule = generate_plan(subjects, total_hours, days)

    return render_template('planner.html', schedule=schedule, subjects=subjects_raw,
                           total_hours=total_hours, days=days)


# ============================================================
# ROUTES: QUIZ
# ============================================================
@app.route('/quiz')
def quiz():
    """Show quiz start screen with topic selection."""
    topics = get_available_topics()
    return render_template('quiz.html', topics=topics)


@app.route('/quiz/start', methods=['POST'])
def quiz_start():
    """Generate quiz questions and store correct answers in session."""
    topic = request.form.get('topic', '')
    num_questions = int(request.form.get('num_questions', '5'))

    # Get random questions from our logic module
    questions = get_random_questions(topic, num_questions)

    if not questions:
        topics = get_available_topics()
        return render_template('quiz.html', topics=topics,
                               error='No questions available for that topic.')

    # Store correct answers in session
    session['quiz_answers'] = {str(i): q['correct'] for i, q in enumerate(questions)}
    session['quiz_topic'] = topic
    session.modified = True

    return render_template('quiz.html', questions=questions, topic=topic, taking_quiz=True)


@app.route('/quiz/submit', methods=['POST'])
def quiz_submit():
    """Compare submitted answers to session answers, return score."""
    if 'quiz_answers' not in session:
        return redirect(url_for('quiz'))

    correct_answers = session['quiz_answers']
    total = len(correct_answers)
    score = 0
    results = []

    for i in range(total):
        submitted = request.form.get(f'question_{i}', '')
        correct = correct_answers[str(i)]
        is_correct = submitted == correct
        if is_correct:
            score += 1
        results.append({
            'question_num': i + 1,
            'submitted': submitted,
            'correct': correct,
            'is_correct': is_correct
        })

    # Clean up session
    topic = session.pop('quiz_topic', 'Unknown')
    session.pop('quiz_answers', None)
    session.modified = True

    percentage = round((score / total) * 100) if total > 0 else 0

    return render_template('quiz.html', score=score, total=total,
                           percentage=percentage, results=results,
                           topic=topic, show_results=True)


# ============================================================
# ROUTES: SUMMARIZER
# ============================================================
@app.route('/summarizer')
def summarizer():
    """Show text input form."""
    return render_template('summarizer.html')


@app.route('/summarizer/generate', methods=['POST'])
def summarizer_generate():
    """Run summarization logic, return summary."""
    text = request.form.get('text', '')
    num_sentences = int(request.form.get('num_sentences', '3'))

    if not text.strip():
        return render_template('summarizer.html', error='Please enter some text to summarize.')

    if len(text.split('.')) < 3:
        return render_template('summarizer.html', error='Please enter at least 3 sentences for a meaningful summary.',
                               original_text=text)

    # Run summarization from our logic module
    summary = summarize_text(text, num_sentences)

    return render_template('summarizer.html', summary=summary, original_text=text,
                           num_sentences=num_sentences)


# ============================================================
# RUN THE APP
# ============================================================
if __name__ == '__main__':
    app.run(debug=True, port=5000)
