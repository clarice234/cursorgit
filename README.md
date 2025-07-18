# Cursor AI Training Code Examples

This repository contains comprehensive code examples and exercises used throughout the Cursor AI full-day training program. Each session builds upon the previous one, providing hands-on experience with different aspects of AI-assisted development.

## 📚 Training Overview

This training is designed to help developers master Cursor AI for various programming tasks, from basic code generation to complex debugging and architecture decisions.

## 🗂️ Session Structure

### Session 1: Core Usage
**Location:** `Session_1_CoreUsage/`

**Learning Objectives:**
- Basic prompting techniques
- Code refactoring with AI assistance
- Understanding AI code generation patterns

**Files:**
- `example.py` - A simple discount calculation function demonstrating basic code structure

**Key Concepts:**
- Writing effective prompts
- Code generation from descriptions
- Basic refactoring operations

### Session 2: Intermediate Skills
**Location:** `Session_2_Intermediate/`

**Learning Objectives:**
- Writing comprehensive tests
- Generating documentation
- Code optimization with AI

**Files:**
- `palindrome.py` - A palindrome detection function for testing and documentation practice

**Key Concepts:**
- Test-driven development with AI
- Documentation generation
- Code review and improvement

### Session 3: Advanced Techniques
**Location:** `Session_3_Advanced/`

**Learning Objectives:**
- Multi-file refactoring
- Architecture decisions
- Complex code restructuring

**Files:**
- `app.py` - Flask web application with BMI calculation endpoint
- `utils.py` - Utility functions for BMI calculations

**Key Concepts:**
- Multi-file code organization
- API development with AI assistance
- Code separation and modularity

### Session 4: Debugging and Problem Solving
**Location:** `Session_4_Debugging/`

**Learning Objectives:**
- Identifying and fixing bugs
- Logic correction
- Code validation

**Files:**
- `buggy_max.py` - A function with intentional bugs for debugging practice

**Key Concepts:**
- Bug identification strategies
- Logic error correction
- Code validation techniques

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Cursor AI editor
- Basic understanding of Python programming

### Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd CursorAI_Training_Code
   ```

2. For Session 3 (Advanced), install Flask:
   ```bash
   pip install flask
   ```

### Running the Examples

#### Session 1: Core Usage
```bash
cd Session_1_CoreUsage
python example.py
```

#### Session 2: Intermediate
```bash
cd Session_2_Intermediate
python palindrome.py
```

#### Session 3: Advanced
```bash
cd Session_3_Advanced
python app.py
```
The Flask app will run on `http://localhost:5000`

#### Session 4: Debugging
```bash
cd Session_4_Debugging
python buggy_max.py
```

## 🧪 Testing

### Running All Tests
To run all unit tests across all sessions:
```bash
python run_tests.py
```

### Running Individual Session Tests

#### Session 1 Tests
```bash
cd Session_1_CoreUsage
python -m unittest test_example.py -v
```

#### Session 2 Tests
```bash
cd Session_2_Intermediate
python -m unittest test_palindrome.py -v
```

#### Session 3 Tests
```bash
cd Session_3_Advanced
python -m unittest test_utils.py -v
python -m unittest test_app.py -v
```

#### Session 4 Tests
```bash
cd Session_4_Debugging
python -m unittest test_buggy_max.py -v
```

### Test Coverage

Each session includes comprehensive unit tests:

- **Session 1**: Tests for discount calculation with edge cases
- **Session 2**: Tests for palindrome detection with various input types
- **Session 3**: Tests for BMI calculation and Flask API endpoints
- **Session 4**: Tests designed to identify bugs in the max function

**Note**: Session 4 tests are designed to fail intentionally to help identify bugs for debugging practice.

## 🎯 Learning Path

1. **Start with Session 1** to understand basic AI prompting
2. **Progress to Session 2** for testing and documentation skills
3. **Advance to Session 3** for multi-file and architectural concepts
4. **Complete with Session 4** for debugging and problem-solving

## 💡 Best Practices

### Prompting Tips
- Be specific about requirements
- Include context and constraints
- Ask for explanations when needed
- Iterate on AI suggestions

### Code Quality
- Always review generated code
- Test thoroughly
- Maintain consistent style
- Document your changes

### Debugging with AI
- Describe the problem clearly
- Include error messages
- Show expected vs actual behavior
- Use AI to explain complex issues

## 🔧 Troubleshooting

### Common Issues
1. **AI not understanding context**: Provide more specific prompts
2. **Generated code doesn't work**: Review and test thoroughly
3. **Complex refactoring fails**: Break down into smaller steps

### Getting Help
- Review the code examples in each session
- Practice with the provided exercises
- Experiment with different prompting strategies

## 📖 Additional Resources

- [Cursor AI Documentation](https://cursor.sh/docs)
- [Python Official Documentation](https://docs.python.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## 🤝 Contributing

This training material is designed for educational purposes. Feel free to:
- Experiment with the code examples
- Create your own variations
- Share your learnings with others

## 📄 License

This project is for educational purposes. Use the code examples to learn and practice with Cursor AI.

---

**Happy coding with Cursor AI! 🚀**
