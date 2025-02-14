from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create question bank
question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data]

# Initialize Quiz Brain
quiz = QuizBrain(question_bank)

# Start GUI (No need for while loop)
quiz_ui = QuizInterface(quiz)


# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
