# Month-Year Checker

A Python application that calculates the number of days in a month and determines whether a year is a leap year.

## Features

- Leap year detection
- Days in month calculation
- Tkinter graphical interface
- Input validation
- Exception handling
- Unit tests
- Type hints
- Git version control

## Technology Stack

- Python 3
- Tkinter
- unittest
- Git
- GitHub

## Application Architecture

```mermaid
flowchart TD

A[User Interface - Tkinter]

B[Input Validation]

C[get_days_in_month]

D[is_leap_year]

E[Result Display]

A --> B
B --> C
C --> D
C --> E
D --> E
```

## Business Logic Flow

```mermaid
flowchart TD

A[User Enters Month]
B[User Enters Year]

C[get_days_in_month]

D{Month Type?}

E[Return 31 Days]
F[Return 30 Days]

G[February]

H[is_leap_year]

I[Return 29 Days]
J[Return 28 Days]

K[Display Result]

A --> C
B --> C

C --> D

D -->|31-Day Month| E
D -->|30-Day Month| F
D -->|February| G

G --> H

H -->|Leap Year| I
H -->|Not Leap Year| J

E --> K
F --> K
I --> K
J --> K
```

## Project Structure

```mermaid
flowchart TD

A[month-year-checker]

B[app.py]
C[test_app.py]
D[README.md]
E[.gitignore]

A --> B
A --> C
A --> D
A --> E
```

## Function Relationships

```mermaid
flowchart TD

A[main]

B[get_days_in_month]

C{February?}

D[is_leap_year]

A --> B
B --> C
C -->|Yes| D
```

## Testing Coverage

The unit tests verify:

- Leap year calculations
- Non-leap year calculations
- February day calculations
- 30-day month calculations
- 31-day month calculations
- Invalid month handling

## Run Application

```bash
python app.py
```

## Run Tests

```bash
python -m unittest test_app.py
```

## Future Enhancements

- Calendar view
- Export results to CSV
- Theme support (Dark Mode)
- Date calculations
- Packaging as a desktop executable


## Author

Vikram Raju K

```
