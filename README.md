# MCQ Quiz Maker & Solver in Python

This is a command-line tool to:
- Create your own multiple-choice questions
- Store them in memory
- Interactively solve them with feedback and scoring

## Features
- Duplicate question detection  
- Input validation (for question and answer options)  
- Custom class (`Question`) to store each MCQ  
- Works with **any number of options** (not just 3).  
- Flexible input: options are numbered (1, 2, 3, …) instead of fixed a/b/c.  
- Interactive solver with detailed feedback (`Correct` / `Incorrect`).  

## Changelog

- **v1.1**
  - Added support for n options in Question Maker.
  - Improved input validation (no duplicate/empty options).
  - Question Solver updated to accept numeric answers.
  - Enhanced feedback messages and scoring system.

- **v1.0**
  - Initial release.
  - Supported 3-option (a, b, c) format only.
  - Duplicate detection and basic input validation.

## Planned Features
- Save questions to a file  
- Load and resume quizzes  