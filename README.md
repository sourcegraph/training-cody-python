# cody_workshop
Basic to Advanced Cody AI Workshop Content

## Installation Instructions

### Install the VS Code extension
You can install VS Code directly from the [VS Code extension marketplace listing](https://marketplace.visualstudio.com/items?itemName=sourcegraph.cody-ai) or by following these steps directly within VS Code:

1. Open VS Code editor on your local machine
2. Click the Extensions icon in the Activity Bar on the side of VS Code, or use the keyboard shortcut Cmd+Shift+X (macOS) or Ctrl+Shift+X (Windows/Linux)
3. Type Cody AI in the search bar and click the Install button
4. After installing, you may be prompted to reload VS Code to activate the extension

### Setting up with mise (recommended)
1. Install mise tool manager following instructions at [mise.jdx.dev](https://mise.jdx.dev)
2. Clone this repository and navigate to the project directory
3. Run `mise install` to automatically install Python and uv package manager
4. Run `uv pip install -e ".[dev]"` to install the project and development dependencies

### Setting up without mise
1. Install Python 3.8 or newer
2. Clone this repository and navigate to the project directory
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -e ".[dev]"`

# Cody Training Workshop Plan

## Overview
This workshop is designed to provide hands-on training for engineers on using Cody, Sourcegraph's AI coding assistant. The session progresses from basic concepts to advanced techniques, ensuring participants leave with practical experience they can immediately apply to their daily work.

## Exercise Repository Structure

The repository contains progressive exercises in the following categories:

1. **Beginner Exercises**
   - Basic prompt formulation
   - Code explanation
   - Simple code generation
   - Documentation assistance

2. **Intermediate Exercises**
   - Debugging workflows
   - Test generation
   - Code refactoring

3. **Advanced Exercises**
   - Code refactoring - pt 2
   - Security vulnerability detection
   - Performance optimization suggestions


## Project structure
```
├── 1_beginner
│   ├── exercise_1_code_explanation
│   │   ├── README.md
│   │   └── sample_code.py
│   ├── exercise_2_documentation
│   │   ├── README.md
│   │   └── undocumented_code.py
│   └── exercise_3_simple_generation
│       ├── generate_function.py
│       └── README.md
├── 2_intermediate
│   ├── exercise_1_debugging
│   │   ├── buggy_code.py
│   │   └── README.md
│   ├── exercise_2_test_generation
│   │   ├── code_to_test.py
│   │   └── README.md
│   └── exercise_3_refactoring
│       ├── README.md
│       └── refactor_me.py
├── 3_advanced
│   ├── exercise_1_complex_refactoring
│   │   ├── complex_app.py
│   │   └── README.md
│   ├── exercise_2_security_review
│   │   ├── README.md
│   │   ├── security_review.py
│   │   ├── setup_users_db.py
│   │   └── users.db
│   └── exercise_3_performance
│       ├── optimise_me.py
│       └── README.md
```
