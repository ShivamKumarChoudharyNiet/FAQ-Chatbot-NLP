from flask import Flask, render_template, request, jsonify
import re
import math
from collections import Counter

app = Flask(__name__)

# 1. Dataset: FAQs Collection
FAQ_DATA = [
    {
        "intent": "admission",
        "questions": ["how to take admission", "admission process", "what is the procedure for admission", "how can i apply for college"],
        "answer": "You can apply online through our official college portal. The process involves registration, document upload, and application fee payment."
    },
    {
        "intent": "courses",
        "questions": ["which courses are available", "btech branches", "what courses do you offer", "list of streams"],
        "answer": "We offer B.Tech programs in Computer Science (CSE), Artificial Intelligence (AI), Data Science, Electronics, and Mechanical Engineering."
    },
    {
        "intent": "fees",
        "questions": ["what is the fee structure", "college fees details", "hostel fee", "how much is the course fee"],
        "answer": "The annual tuition fee for B.Tech is approximately INR 1,25,000. Hostel and mess charges are separate, amounting to around INR 85,000 per year."
    },
    {
        "intent": "placement",
        "questions": ["how is the placement", "average package", "top recruiters", "placement statistics"],
        "answer": "Our college has an excellent placement record with a 90%+ placement rate. The average package is INR 5-6 LPA, and top recruiters include TCS, Wipro, and Infosys."
    },
    {
        "intent": "greetings",
        "questions": ["hello", "hi", "hey", "good morning", "anyone there"],
        "answer": "Hello! I am your College Assistant Bot. How can I help you today regarding admissions, fees, courses, or placements?"
    }
]

# 2. NLP Preprocessing Function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text) 
    tokens = text.split()               
    stopwords = {'what', 'is', 'the', 'for', 'a', 'an', 'how', 'do', 'you', 'in', 'to', 'i', 'can', 'are', 'which'}
    cleaned_tokens = [word for word in tokens if word not in stopwords]
    return cleaned_tokens

# 3. Vectorization & Cosine Similarity Algorithm
def get_cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

# 4. Intent Matching Engine
def find_best_matching_faq(user_query):
    user_tokens = preprocess_text(user_query)
    user_vector = Counter(user_tokens)
    
    best_match_answer = "I'm sorry, I couldn't find an exact answer to that. Please contact the college helpdesk for more detailed information."
    highest_similarity = 0.0
    threshold = 0.25 

    for faq in FAQ_DATA:
        for question in faq["questions"]:
            question_tokens = preprocess_text(question)
            question_vector = Counter(question_tokens)
            
            similarity = get_cosine_similarity(user_vector, question_vector)
            
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match_answer = faq["answer"]
                
    if highest_similarity >= threshold:
        return best_match_answer
    return "I am still learning! Could you please rephrase your question about admissions, fees, or placements?"

# --- Flask Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    if not user_message.strip():
        return jsonify({"reply": "Please type a valid question."})
        
    bot_reply = find_best_matching_faq(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True, port=5000)