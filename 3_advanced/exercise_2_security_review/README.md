# Exercise 2: Security Review

## Overview
In this advanced exercise, you will use Cody to conduct a security review of a Python script. The goal is to identify and fix security vulnerabilities, ensuring that the code adheres to best security practices. This exercise will enhance your ability to write secure code and protect applications from common vulnerabilities.

## Objectives
- Utilize Cody to identify potential security issues in the code.
- Understand common security vulnerabilities, such as SQL injection, insecure data handling, and inadequate authentication.
- Implement fixes to address identified vulnerabilities and secure the application.

## Instructions
1. Open the `security_review.py` file, which contains code with several security vulnerabilities.
2. Use Cody to analyze the code and identify the security flaws.
3. Refactor the code to mitigate the vulnerabilities, implementing security best practices.
4. Ensure that the code operates securely without compromising its functionality.

## Success Criteria
- Identify and fix all security vulnerabilities within `security_review.py`.
- Implement security best practices to prevent future vulnerabilities.
- Demonstrate a thorough understanding of potential security risks and mitigation strategies.

### Task for Participants:
- Use Cody to identify security vulnerabilities in `security_review.py`:
  - SQL injection risk in the `get_user_data` function.
  - Insecure data handling and lack of input validation in `main()`.
  
- Refactor the code to:
  - Use parameterized queries to prevent SQL injection.
  - Validate and sanitize user inputs properly.
  - Ensure secure handling and display of user data.
