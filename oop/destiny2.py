
# Create a class called `User` with:
# - Attributes: user_id, name, age, weight, and `_workout_log` (private list)
# - Methods:
#   - `add_workout(workout)` - adds workout to log
#   - `get_total_calories()` - returns total calories for all workouts
#   - `get_workout_stats()` - returns statistics (count by type, average duration)
#   - `display_progress()` - returns formatted workout history with dates

class User:
    def __init__(self, user_id, name, age, weight):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.weight = weight
        self._workout_log = []

    def add_workout(self, workout):
        self._workout_log.append(workout)
        return workout

    def get_total_calories(self):
        total = 0
        for workout in self._workout_log:
            total += workout.get("calories", 0)
        return total

    def get_workout_stats(self):
        if not self._workout_log:
            return {"count_by_type": {}, "average_duration": 0}

        count_by_type = {}
        total_duration = 0

        for workout in self._workout_log:
            workout_type = workout.get("type", "unknown")
            count_by_type[workout_type] = count_by_type.get(workout_type, 0) + 1
            total_duration += workout.get("duration_minutes", 0)

        average_duration = total_duration / len(self._workout_log)
        return {"count_by_type": count_by_type, "average_duration": average_duration}

    def display_progress(self):
        if not self._workout_log:
            return f"{self.name} has no workouts logged yet."

        history = []
        for workout in self._workout_log:
            date = workout.get("date", "Unknown date")
            workout_type = workout.get("type", "Workout")
            duration = workout.get("duration_minutes", 0)
            calories = workout.get("calories", 0)
            history.append(f"{date} | {workout_type} | {duration} min | {calories} cal")

        return "\n".join(history) 


# Create a class called `Student` (inherits from User) with:
# - Additional attributes: `_quiz_history` (private list)
# - Additional methods:
#   - `take_quiz(quiz)` - takes quiz and records results
#   - `get_average_score()` - calculates average of all quizzes taken
    

class student(User):
    def __init__(self, user_id, name, age, weight):
        super().__init__(user_id, name, age, weight)
        self._quiz_history = []

    def take_quiz(self, quiz):
        self._quiz_history.append(quiz)
        return quiz

    def get_average_score(self):
        if not self._quiz_history:
            return 0

        total_score = sum(quiz.get("score", 0) for quiz in self._quiz_history)
        average_score = total_score / len(self._quiz_history)
        return average_score

student1 = student("S001", "Alice", 20, 55)
student1.take_quiz({"quiz_id": "QZ001", "score": 85})
student1.take_quiz({"quiz_id": "QZ002", "score": 90})
average_score = student1.get_average_score()
print(f"{student1.name}'s average quiz score: {average_score}")  # Output
