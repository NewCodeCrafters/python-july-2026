# Individual OOP Exercises for 8 Trainees

## Exercise 1: The Blueprint Designer
**Create a blueprint (class) for a "Smartphone" with the following:**
- Attributes: brand, model, storage_capacity, battery_percentage, is_5g_enabled
- Methods:
  - A way to initialize the phone with all attributes
  - A method to charge the battery (increases percentage)
  - A method to use the phone (decreases percentage based on usage)
  - A method to upgrade storage (increases capacity)
  - A method to toggle 5G on/off

**Tasks:**
1. Design the blueprint with proper attributes and methods
2. Create 3 different phone objects with varying specifications
3. Test all methods on each phone
4. Display phone information in a user-friendly format

---

## Exercise 2: The Bank Account System
**Create a bank account system with:**
- Attributes: account_holder, account_number, balance, account_type, interest_rate
- Methods:
  - Initialize account with holder name and initial deposit
  - Deposit money (with validation for positive amounts)
  - Withdraw money (with validation for sufficient balance)
  - Apply interest (based on account type)
  - Get account statement (showing all transactions)
  - Transfer money to another account

**Tasks:**
1. Design the class structure
2. Create checking and savings accounts
3. Perform multiple transactions (deposits, withdrawals, transfers)
4. Show how interest is calculated differently for each account type
5. Generate a mini bank statement

---

## Exercise 3: The Fitness Tracker
**Create a workout tracking system:**
- Attributes: user_name, daily_goal, current_steps, distance_covered, calories_burned, workout_history
- Methods:
  - Initialize with user name and daily step goal
  - Log steps (adds to current_steps)
  - Calculate distance (based on steps taken)
  - Calculate calories burned (based on steps and user weight)
  - Check daily goal progress (shows percentage)
  - Reset daily tracker
  - Save workout to history

**Tasks:**
1. Design the fitness tracker class
2. Create two different user profiles
3. Track steps over a week for each user
4. Show daily progress and weekly summary
5. Identify which user met their goals more often

---

## Exercise 4: The Course Registration System
**Create a university course management system with:**
- Attributes: course_code, course_name, credits, max_students, enrolled_students, instructor
- Methods:
  - Initialize course with code, name, credits, and capacity
  - Enroll a student (check for capacity)
  - Drop a student
  - Check available seats
  - Assign/change instructor
  - Get class roster
  - Calculate course load for instructor

**Tasks:**
1. Design the course class
2. Create 3 different courses
3. Simulate enrollment process (enroll 10+ students)
4. Handle enrollment capacity limits
5. Show class rosters and availability

---

## Exercise 5: The Hotel Booking System
**Create a hotel room management system:**
- Attributes: room_number, room_type, price_per_night, is_available, max_occupancy, current_guest
- Methods:
  - Initialize room with number, type, price, and capacity
  - Book room (assign guest, mark unavailable)
  - Check-out (mark available, clear guest)
  - Check availability
  - Calculate stay cost (for multiple nights)
  - Change price (with validation)
  - Get room status

**Tasks:**
1. Design the hotel room class
2. Create rooms of different types (single, double, suite)
3. Simulate booking and check-out process
4. Handle booking conflicts
5. Generate daily revenue report

---

## Exercise 6: The Shopping Cart System
**Create an e-commerce shopping system:**
- Attributes: cart_id, customer_name, items_list, total_price, tax_rate, discount_code
- Methods:
  - Initialize cart with customer name
  - Add item (item name, price, quantity)
  - Remove item
  - Update quantity
  - Calculate subtotal
  - Apply tax
  - Apply discount code (percentage or fixed amount)
  - Calculate final total
  - Checkout (clears cart, generates receipt)

**Tasks:**
1. Design the shopping cart class
2. Add multiple items to cart
3. Apply different discount codes
4. Calculate final prices with tax
5. Generate receipt-like summary
6. Test with different item combinations

---

## Exercise 7: The Time Management System
**Create a task management system:**
- Attributes: task_id, title, description, priority, due_date, status, assigned_to, time_spent
- Methods:
  - Initialize task with title, description, and due date
  - Update status (To Do, In Progress, Review, Complete)
  - Assign to a person
  - Log time spent
  - Check if task is overdue
  - Get priority level
  - Generate task summary

**Tasks:**
1. Design the task management class
2. Create various tasks with different priorities
3. Simulate work process (status changes, time logging)
4. Identify overdue tasks
5. Generate project status report
6. Show tasks by priority level

---

## Exercise 8: The Weather Station System
**Create a weather monitoring system:**
- Attributes: location, temperature, humidity, pressure, wind_speed, weather_condition, historical_data
- Methods:
  - Initialize with location
  - Update weather readings
  - Convert temperature (Celsius to Fahrenheit)
  - Determine weather condition (based on readings)
  - Calculate weather trend (comparing to previous readings)
  - Save historical data
  - Generate weather report
  - Compare to another location

**Tasks:**
1. Design the weather station class
2. Create stations for different cities
3. Simulate weather changes over time
4. Track and display historical data
5. Compare weather between cities
6. Generate user-friendly weather reports
7. Identify weather patterns

---

## Exercise 9: The Employee Management System (Bonus)
**Create an employee management system with:**
- Attributes: employee_id, full_name, position, department, salary, hire_date, performance_rating
- Methods:
  - Initialize employee details
  - Promote (change position and salary)
  - Give raise (percentage or fixed amount)
  - Update performance rating
  - Calculate years of service
  - Determine bonus eligibility
  - Generate employee summary
  - Transfer department

**Tasks:**
1. Design the employee class
2. Create employees in different departments
3. Simulate promotions and raises
4. Calculate bonuses based on performance
5. Generate department reports
6. Show employee growth over time

---

## Exercise 10: The Blog Post System (Bonus)
**Create a content management system for blog posts:**
- Attributes: post_id, title, content, author, publish_date, tags, view_count, comment_list
- Methods:
  - Initialize post with title and author
  - Add content
  - Publish (sets date)
  - Add tags
  - Increment view count
  - Add comment (with commenter name and text)
  - Get comment count
  - Search by tag
  - Generate post preview (truncated content)
  - Calculate engagement score

**Tasks:**
1. Design the blog post class
2. Create multiple blog posts
3. Simulate viewing and commenting
4. Add and search by tags
5. Show most viewed/popular posts
6. Generate author statistics

---

## Assessment Criteria for Each Exercise:
1. **Design Quality** (30%) - Is the blueprint well-thought-out?
2. **Method Implementation** (30%) - Are all methods logical and useful?
3. **Testing/Demo** (20%) - Are you showing your code works?
4. **OOP Principles** (20%) - Are you using encapsulation, proper attributes, etc.?

## Instructions:
- Each trainee should pick **3 exercises** to complete
- Submit as separate Python files with clear comments
- Include test cases showing your blueprint works
- Demonstrate understanding of OOP principles
- Use proper naming conventions and organization