# Python OOP Practice Exercises

## Resolved: Create a Library System

Create a class called `Book` with the following specifications:
- Attributes: title, author, isbn, publication_year, and `_is_borrowed` (private)
- Methods: 
  - `borrow()` - marks the book as borrowed if available
  - `return_book()` - marks the book as returned
  - `get_status()` - returns whether the book is available or borrowed
  - `display_info()` - returns a formatted string with all book details

Create three book objects and demonstrate borrowing and returning books.

## Exercise 2: Student Records System

Create a class called `Student` with:
- Attributes: student_id, name, courses (list), grades (dictionary), and `_gpa` (private)
- Methods:
  - `add_course(course_name, grade)` - adds a course and grade
  - `update_grade(course_name, new_grade)` - updates an existing grade
  - `calculate_gpa()` - calculates GPA based on grades
  - `get_transcript()` - returns a formatted transcript showing all courses and grades

Create at least three student objects with different course loads.

## Exercise 3: Banking Application

Create a class called `BankAccount` with:
- Attributes: account_number, account_holder, balance, and `_transaction_history` (private list)
- Methods:
  - `deposit(amount)` - adds money with validation
  - `withdraw(amount)` - removes money with validation (cannot overdraw)
  - `transfer(to_account, amount)` - transfers money to another account
  - `get_balance()` - returns current balance
  - `get_transaction_history()` - returns a formatted list of all transactions

Create two accounts and perform several deposits, withdrawals, and transfers.

## Muhammed: E-commerce Product System

Create a class called `Product` with:
- Attributes: product_id, name, price, stock_quantity, and `_reviews` (private list of dictionaries)
- Methods:
  - `update_stock(quantity)` - adjusts stock quantity
  - `add_review(customer_name, rating, comment)` - adds a review with validation
  - `get_average_rating()` - calculates average rating
  - `is_in_stock()` - returns boolean
  - `display_details()` - returns all product information including average rating

Create product objects with different categories and add multiple reviews to each.

## Exercise 5: Vehicle Fleet Management

Create a class called `Vehicle` with:
- Attributes: vehicle_id, make, model, year, mileage, and `_maintenance_log` (private list)
- Methods:
  - `drive(miles)` - adds miles with validation
  - `schedule_maintenance(date, description)` - adds maintenance record
  - `get_maintenance_history()` - returns formatted maintenance records
  - `needs_service()` - returns True if mileage exceeds 5000 since last maintenance

Create a class called `Truck` that inherits from Vehicle with:
- Additional attributes: cargo_capacity, current_load
- Additional methods:
  - `load_cargo(weight)` - adds cargo with capacity validation
  - `unload_cargo()` - removes all cargo
  - Override `needs_service()` to consider heavy loads

## Destiny: Restaurant Order System

Create a class called `MenuItem` with:
- Attributes: item_id, name, price, category, and `_preparation_time` (private)
- Methods:
  - `update_price(new_price)` - updates with validation
  - `get_prep_time()` - returns preparation time
  - `display()` - returns formatted item details

Create a class called `Order` with:
- Attributes: order_id, items (list of MenuItem objects), status, and `_total` (private)
- Methods:
  - `add_item(item, quantity)` - adds item with quantity
  - `remove_item(item_id)` - removes item from order
  - `calculate_total()` - calculates total with tax
  - `update_status(new_status)` - updates with valid statuses
  - `get_receipt()` - returns formatted receipt

Create menu items and process several orders with different items.

## Peter: University Course Management

Create a class called `Course` with:
- Attributes: course_code, title, credits, instructor, and `_enrolled_students` (private list)
- Methods:
  - `enroll_student(student_id)` - adds student
  - `drop_student(student_id)` - removes student
  - `get_enrollment_count()` - returns number of enrolled students
  - `is_full()` - returns True if enrollment reaches 30
  - `display_course_info()` - returns all course details

Create a class called `Instructor` with:
- Attributes: instructor_id, name, department, and `_assigned_courses` (private list)
- Methods:
  - `assign_course(course)` - adds course to assigned list
  - `remove_course(course_code)` - removes course
  - `get_teaching_load()` - returns number of courses
  - `display_schedule()` - returns formatted list of assigned courses

## AbdulRahman: Hotel Room Booking System

Create a class called `HotelRoom` with:
- Attributes: room_number, room_type, price_per_night, `_is_available` (private), and `_booking_history` (private list)
- Methods:
  - `book_room(guest_name, check_in, check_out)` - books if available
  - `cancel_booking(guest_name)` - cancels specific booking
  - `check_availability()` - returns availability status
  - `get_booking_history()` - returns formatted booking records
  - `calculate_stay_cost(nights)` - calculates total cost

Create a class called `Guest` with:
- Attributes: guest_id, name, email, and `_reservations` (private list)
- Methods:
  - `make_reservation(room, check_in, check_out)` - creates reservation
  - `cancel_reservation(room_number)` - cancels specific reservation
  - `get_active_reservations()` - returns current bookings
  - `display_reservation_history()` - returns all reservations

## Samuel: Fitness Tracker

Create a class called `Workout` with:
- Attributes: workout_id, type, duration, intensity, and `_calories_burned` (private)
- Methods:
  - `calculate_calories()` - calculates based on type, duration, and intensity
  - `get_calories()` - returns calculated calories
  - `display_summary()` - returns workout summary

Create a class called `User` with:
- Attributes: user_id, name, age, weight, and `_workout_log` (private list)
- Methods:
  - `add_workout(workout)` - adds workout to log
  - `get_total_calories()` - returns total calories for all workouts
  - `get_workout_stats()` - returns statistics (count by type, average duration)
  - `display_progress()` - returns formatted workout history with dates

## Ore: Online Quiz System

Create a class called `Question` with:
- Attributes: question_id, text, options (list), correct_answer, and `_difficulty` (private)
- Methods:
  - `check_answer(choice)` - returns True if correct
  - `get_difficulty()` - returns difficulty level
  - `display_question()` - returns formatted question with options

Create a class called `Quiz` with:
- Attributes: quiz_id, title, questions (list), and `_score` (private)
- Methods:
  - `add_question(question)` - adds question
  - `remove_question(question_id)` - removes question
  - `take_quiz()` - simulates taking quiz (answers provided by user)
  - `get_score()` - returns current score
  - `get_percentage()` - returns percentage score
  - `display_results()` - returns detailed results

Create a class called `Student` (inherits from User) with:
- Additional attributes: `_quiz_history` (private list)
- Additional methods:
  - `take_quiz(quiz)` - takes quiz and records results
  - `get_average_score()` - calculates average of all quizzes taken