class Question:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, answer_index):
        return answer_index == self.correct_option


class Quiz:
    def __init__(self, category, questions):
        self.category = category
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        print(f"\nStarting quiz in category: {self.category}\n")
        for i, question in enumerate(self.questions, 1):
            print(f"Q{i}: {question.question_text}")
            for idx, option in enumerate(question.options):
                print(f"  {idx + 1}. {option}")

            while True:
                try:
                    answer = int(input("Your answer (1-4): ")) - 1
                    if 0 <= answer < len(question.options):
                        break
                    else:
                        print("Invalid option. Try again.")
                except ValueError:
                    print("Please enter a valid number.")

            if question.is_correct(answer):
                print("Correct!\n")
                self.score += 1
            else:
                correct_answer = question.options[question.correct_option]
                print(f"Wrong! The correct answer was: {correct_answer}\n")

    def show_result(self):
        total_questions = len(self.questions)
        percentage = (self.score / total_questions) * 100
        print(f"Quiz Completed!\nYour Score: {self.score}/{total_questions}")
        print(f"Percentage: {percentage:.2f}%")

        if percentage >= 80:
            feedback = "Excellent!"
        elif percentage >= 50:
            feedback = "Good effort, but try again."
        else:
            feedback = "Better luck next time."
        print(f"Feedback: {feedback}\n")


class QuizManager:
    def __init__(self):
        self.categories = {
            "Science": [
                {
                    "question_text": "What is the chemical symbol for water?",
                    "options": ["H2O", "CO2", "O2", "NaCl"],
                    "correct_option": 0
                },
                {
                    "question_text": "How many planets are in the solar system?",
                    "options": ["7", "8", "9", "10"],
                    "correct_option": 1
                }
            ],
            "History": [
                {
                    "question_text": "Who was the first President of the United States?",
                    "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"],
                    "correct_option": 1
                },
                {
                    "question_text": "In which year did World War II end?",
                    "options": ["1945", "1939", "1918", "1965"],
                    "correct_option": 0
                }
            ]
        }

    def start(self):
        print("Welcome to QuizMaster – OOP Terminal Quiz Game!\n")
        print("Available Categories:")
        for idx, category in enumerate(self.categories.keys(), 1):
            print(f"{idx}. {category}")

        while True:
            try:
                choice = int(input("\nSelect a category (number): ")) - 1
                if 0 <= choice < len(self.categories):
                    selected_category = list(self.categories.keys())[choice]
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")

        questions_data = self.categories[selected_category]
        questions = [
            Question(q['question_text'], q['options'], q['correct_option'])
            for q in questions_data
        ]

        quiz = Quiz(selected_category, questions)
        quiz.start_quiz()
        quiz.show_result()


if __name__ == "__main__":
    manager = QuizManager()
    manager.start()
