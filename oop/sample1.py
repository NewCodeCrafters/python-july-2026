# Polymorphism in Python

class Dog:
    species = "Canis familiaris"
    def speak(self):
        return "Woof!"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.teeth = 42

class DomesticAnimal:
    def speak(self):
        return "I am a domestic animal!"

class Ekuke(DomesticAnimal, Dog):
    # def speak(self):
    #     return "Growl Bark Scowl!"
    def __init__(self, name, age):
        super().__init__(name, age)  # Call the constructor of the first parent class (Dog)
        self.species = "Ekuke Familiaris"  # Override the species attribute


# jack = Ekuke("Jack", 5)
# jack.species = "Ekuke Familaris"
# print(jack.speak())  # Output: Growl Bark Scowl!
# print(jack.species)

# ## Ore: Online Quiz System

# Create a class called `Question` with:
# - Attributes: question_id, text, options (list), correct_answer, and `_difficulty` (private)
# - Methods:
#   - `check_answer(choice)` - returns True if correct
#   - `get_difficulty()` - returns difficulty level
#   - `display_question()` - returns formatted question with options

# Create a class called `Quiz` with:
# - Attributes: quiz_id, title, questions (list), and `_score` (private)
# - Methods:
#   - `add_question(question)` - adds question
#   - `remove_question(question_id)` - removes question
#   - `take_quiz()` - simulates taking quiz (answers provided by user)
#   - `get_score()` - returns current score
#   - `get_percentage()` - returns percentage score
#   - `display_results()` - returns detailed results

# Create a class called `Student` (inherits from User) with:
# - Additional attributes: `_quiz_history` (private list)
# - Additional methods:
#   - `take_quiz(quiz)` - takes quiz and records results
#   - `get_average_score()` - calculates average of all quizzes taken

class Question:
    def __init__(self, question_id:str, text:str, options:list, correct_answer:str, difficulty:str):
        self.question_id = question_id
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self._difficulty = difficulty

    def check_answer(self, answer):
        if answer == self.correct_answer:
            return True
        else:
            return False


    def get_difficulty(self):
        return self._difficulty

    def display_question(self):
        formatted_options = "\n".join(f"{i + 1}. {option}" for i, option in enumerate(self.options))
        return f"Q{self.question_id}: {self.text}\n{formatted_options}"

sample = Question(question_id="123a", text="Best food in Nigeria", options=["Rice", "Beans", "Garri"], correct_answer="Garri", difficulty="Easy")

print(sample.check_answer("Rice"))
print(sample.get_difficulty())

print(sample.display_question())