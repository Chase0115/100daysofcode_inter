from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_game = QuizBrain(question_bank)

while quiz_game.still_has_question():
    quiz_game.next_question()

print("You've complete quiz")
print(f"Your final score is {quiz_game.score}/{len(question_bank)}")
