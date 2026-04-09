## Project 1

### [User info program](../Projects/user-info-program.py)
    - Take input: (name, age, height)
    - Convet types properly
    - Print output using f-string

**Topics Covered**
- Variables
- Data Types
- Input & Output
- Type conversion
- f-string

## Project 2

### [BMI Calculator](../Projects/BMI-calculator.py)
    - Take input: (name, age, height(cm), weight(kg))
    - Find BMI
        BMI = Weight / (height_in_meter)^2
            < 18.5 → Underweight
            18.5 – 24.9 → Normal
            25 – 29.9 → Overweight
            30+ → Obese
    - Check age and show result
            If age < 18 AND BMI > 25 → print warning
            If age > 60 OR BMI < 18 → health caution
    - Output:
                 BMI Result
            Name: 
            Age:
            Weight(kg):
            Height(cm): 

            BMI: xxxx -> result

            


**Topics Covered**
- Operators
- Conditional statement
## 📌 Project 3: 
### [Smart Number System](../Projects/smart-number-system.py)

* Infinite loop using `while True`
* Show menu → take input → execute → repeat
* Exit only when user selects option 4

---

## 📋 Menu Options

### 1. Range Analyzer

**Input:**

* Start (int)
* End (int)

**Rules:**

* If start > end → swap OR show error

**For each number:**

* Even / Odd
* Prime (only for n > 1)
* Divisible by:

  * 3
  * 5
  * both

**Control Flow:**

* If divisible by 7 → `continue`
* If number > 100 → ask for input again 

---

### 2. Number Pattern

**Input:**

* Positive integer `n`

**Output:**

```
1
1 2
1 2 3
...
```

**Rules:**

* If n <= 0 → ask for input again 

---

### 3. Single Number Check

**Input:**

* Integer

**Output:**

* Even / Odd
* Prime / Not (n > 1)
* Factorial:

  * Only if n >= 0
  * If negative → ask for input again 

---

### 4. Exit

* Break main loop