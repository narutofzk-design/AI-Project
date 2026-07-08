"""
Text Summarizer Logic Module
Uses extractive summarization: scores sentences by word frequency
and returns the highest-scoring sentences.
This is a classic simple NLP algorithm - no external libraries needed.
"""


# Common English stopwords - these words are too common to be meaningful
STOPWORDS = {
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
    'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
    'could', 'should', 'may', 'might', 'shall', 'can', 'need', 'dare',
    'this', 'that', 'these', 'those', 'it', 'its', 'he', 'she', 'they',
    'we', 'you', 'i', 'me', 'him', 'her', 'us', 'them', 'my', 'your',
    'his', 'our', 'their', 'what', 'which', 'who', 'whom', 'where',
    'when', 'why', 'how', 'all', 'each', 'every', 'both', 'few', 'more',
    'most', 'other', 'some', 'such', 'no', 'not', 'only', 'own', 'same',
    'so', 'than', 'too', 'very', 'just', 'because', 'as', 'until',
    'while', 'about', 'between', 'through', 'during', 'before', 'after',
    'above', 'below', 'up', 'down', 'out', 'off', 'over', 'under',
    'again', 'further', 'then', 'once', 'here', 'there', 'also', 'if',
}


def summarize_text(text, num_sentences=3):
    """
    Performs extractive summarization on the input text.

    Algorithm:
    1. Split text into sentences
    2. Calculate word frequency (excluding stopwords)
    3. Score each sentence based on its word frequencies
    4. Return top N highest-scoring sentences in original order

    Args:
        text (str): The input text to summarize
        num_sentences (int): Number of sentences to include in summary (default 3)

    Returns:
        str: The summarized text (top sentences joined together)
    """
    # Step 1: Split text into sentences
    sentences = split_into_sentences(text)

    if len(sentences) <= num_sentences:
        # Text is already short enough, return as-is
        return text.strip()

    # Step 2: Calculate word frequency
    word_freq = calculate_word_frequency(text)

    # Step 3: Score each sentence
    sentence_scores = []
    for i, sentence in enumerate(sentences):
        score = score_sentence(sentence, word_freq)
        sentence_scores.append((i, sentence, score))

    # Step 4: Get top N sentences by score
    # Sort by score (highest first)
    sorted_sentences = sorted(sentence_scores, key=lambda x: x[2], reverse=True)
    top_sentences = sorted_sentences[:num_sentences]

    # Re-sort by original position to maintain text flow
    top_sentences.sort(key=lambda x: x[0])

    # Join the selected sentences
    summary = ' '.join(sentence.strip() for _, sentence, _ in top_sentences)

    return summary


def split_into_sentences(text):
    """
    Splits text into sentences using period, exclamation mark, and question mark.

    Args:
        text (str): Input text

    Returns:
        list: List of sentence strings
    """
    # Replace multiple sentence-ending punctuation with just period for splitting
    text = text.replace('!', '.')
    text = text.replace('?', '.')

    # Split on period
    raw_sentences = text.split('.')

    # Clean up: strip whitespace, remove empty strings
    sentences = [s.strip() for s in raw_sentences if s.strip()]

    # Add periods back to sentences for readability
    sentences = [s + '.' if not s.endswith('.') else s for s in sentences]

    return sentences


def calculate_word_frequency(text):
    """
    Calculates the frequency of each word in the text, excluding stopwords.

    Args:
        text (str): Input text

    Returns:
        dict: {word: frequency_count}
    """
    # Clean text: lowercase and remove punctuation
    clean_text = text.lower()
    for char in '.,!?;:()[]{}"\'-':
        clean_text = clean_text.replace(char, ' ')

    # Split into words
    words = clean_text.split()

    # Count word frequency (skip stopwords and very short words)
    word_freq = {}
    for word in words:
        if word not in STOPWORDS and len(word) > 2:
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


def score_sentence(sentence, word_freq):
    """
    Scores a sentence based on the frequency of its words.
    Higher score = sentence contains more important (frequent) words.

    Args:
        sentence (str): A single sentence
        word_freq (dict): Word frequency dictionary

    Returns:
        float: The sentence score (normalized by sentence length)
    """
    # Clean sentence
    clean = sentence.lower()
    for char in '.,!?;:()[]{}"\'-':
        clean = clean.replace(char, ' ')

    words = clean.split()

    if not words:
        return 0

    # Sum up the frequency scores of words in this sentence
    score = 0
    for word in words:
        if word in word_freq:
            score += word_freq[word]

    # Normalize by sentence length to avoid bias toward longer sentences
    # But don't penalize too much - use square root for balance
    normalized_score = score / (len(words) ** 0.5)

    return normalized_score
