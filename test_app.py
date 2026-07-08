"""
Test script to verify all routes and templates work correctly.
Run this to check for errors before deploying.
"""
import sys
sys.path.insert(0, '.')

from app import app

def test_all_routes():
    """Test all GET routes return 200 status."""
    app.config['TESTING'] = True
    client = app.test_client()

    print("=" * 50)
    print("TESTING ALL ROUTES")
    print("=" * 50)

    # Test GET routes
    get_routes = [
        ('/', 'Home'),
        ('/chatbot', 'Chatbot'),
        ('/planner', 'Planner'),
        ('/quiz', 'Quiz'),
        ('/summarizer', 'Summarizer'),
    ]

    errors = []

    for route, name in get_routes:
        response = client.get(route)
        status = response.status_code
        if status == 200:
            print(f"  [PASS] GET {route} ({name}) - Status: {status}")
        else:
            print(f"  [FAIL] GET {route} ({name}) - Status: {status}")
            errors.append(f"GET {route} returned {status}")

    # Test POST routes
    print("\n--- Testing POST routes ---")

    # Test chatbot ask
    response = client.post('/chatbot/ask',
                          json={'message': 'hello'},
                          content_type='application/json')
    if response.status_code == 200:
        data = response.get_json()
        print(f"  [PASS] POST /chatbot/ask - Reply: {data['reply'][:50]}...")
    else:
        print(f"  [FAIL] POST /chatbot/ask - Status: {response.status_code}")
        errors.append("POST /chatbot/ask failed")

    # Test planner generate
    response = client.post('/planner/generate',
                          data={'subjects': 'Math, Science', 'total_hours': '10', 'days': '5'})
    if response.status_code == 200:
        print(f"  [PASS] POST /planner/generate - Status: 200")
    else:
        print(f"  [FAIL] POST /planner/generate - Status: {response.status_code}")
        errors.append("POST /planner/generate failed")

    # Test quiz start
    response = client.post('/quiz/start',
                          data={'topic': 'Mathematics', 'num_questions': '3'})
    if response.status_code == 200:
        print(f"  [PASS] POST /quiz/start - Status: 200")
    else:
        print(f"  [FAIL] POST /quiz/start - Status: {response.status_code}")
        errors.append("POST /quiz/start failed")

    # Test summarizer generate
    test_text = "Python is a programming language. It is very popular. Many developers use it. It has simple syntax. Python supports multiple paradigms."
    response = client.post('/summarizer/generate',
                          data={'text': test_text, 'num_sentences': '2'})
    if response.status_code == 200:
        print(f"  [PASS] POST /summarizer/generate - Status: 200")
    else:
        print(f"  [FAIL] POST /summarizer/generate - Status: {response.status_code}")
        errors.append("POST /summarizer/generate failed")

    # Summary
    print("\n" + "=" * 50)
    if errors:
        print(f"RESULT: {len(errors)} ERRORS FOUND!")
        for err in errors:
            print(f"  - {err}")
    else:
        print("RESULT: ALL TESTS PASSED!")
    print("=" * 50)

    return len(errors) == 0


if __name__ == '__main__':
    success = test_all_routes()
    sys.exit(0 if success else 1)
