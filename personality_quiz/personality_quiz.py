def welcome():
    print("✨ Welcome to the Python Personality Quiz! ✨")
    print("Answer the following questions honestly to find out your personality type.\n")

def ask_question(question, options):
    print(question)
    for key, value in options.items():
        print(f"{key}: {value['text']}")
    choice = input("\nYour choice (A/B/C): ").upper()
    while choice not in options:
        choice = input("❌ Invalid choice! Please enter A, B, or C: ").upper()
    print()
    return options[choice]["score"]

def calculate_personality(score):
    if score <= 5:
        return "🌱 The Dreamer – You are imaginative and see beauty in everything."
    elif score <= 10:
        return "🔥 The Go-Getter – You are ambitious, confident, and full of energy!"
    else:
        return "🌊 The Thinker – You are calm, logical, and deeply introspective."

def start_quiz():
    welcome()
    total_score = 0

    questions = [
        {
            "question": "1️⃣ What’s your ideal weekend?",
            "options": {
                "A": {"text": "Reading a good book", "score": 4},
                "B": {"text": "Exploring a new place", "score": 7},
                "C": {"text": "Working on personal goals", "score": 10}
            }
        },
        {
            "question": "2️⃣ How do you handle challenges?",
            "options": {
                "A": {"text": "Take time to think", "score": 5},
                "B": {"text": "Face them head-on!", "score": 10},
                "C": {"text": "Look for creative solutions", "score": 7}
            }
        },
        {
            "question": "3️⃣ Which word describes you best?",
            "options": {
                "A": {"text": "Calm", "score": 4},
                "B": {"text": "Curious", "score": 6},
                "C": {"text": "Driven", "score": 9}
            }
        },
        {
            "question": "4️⃣ What motivates you the most?",
            "options": {
                "A": {"text": "Peace of mind", "score": 3},
                "B": {"text": "Adventure", "score": 7},
                "C": {"text": "Success", "score": 10}
            }
        },
        {
            "question": "5️⃣ How do you relax?",
            "options": {
                "A": {"text": "Meditate or daydream", "score": 3},
                "B": {"text": "Hang out with friends", "score": 7},
                "C": {"text": "Plan your next big thing", "score": 9}
            }
        }
    ]

    for q in questions:
        total_score += ask_question(q["question"], q["options"])

    result = calculate_personality(total_score)
    print("🔮 Your Personality Result 🔮\n")
    print(result)
    print("\nThanks for playing! ✨")

# Run quiz
if __name__ == "__main__":
    start_quiz()
