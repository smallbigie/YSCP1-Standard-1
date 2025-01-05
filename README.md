# YSCP1-Standard-1
A Python project to explore debugging and error handling using Visual Studio Code and GitHub Codespaces

# Vending Machine Debugging Project

## **Overview**
This project simulates a simple vending machine and involves writing, running, and debugging Python code using Visual Studio Code in GitHub Codespaces.

---

## **Errors and Debugging**

### **1. Syntax Error**
- **Error**: Missing parentheses in `vending_machine()` call.
- **How to Identify**: IDE flagged the missing parentheses.
- **Solution**: Add parentheses to fix the syntax error.

### **2. Run-Time Error**
- **Error**: (Introduce a run-time error, e.g., divide by zero or KeyError.)
- **How to Identify**: Program crashed during execution.
- **Solution**: (Explain how the error was fixed.)

### **3. Logic Error**
- **Error**: Incorrect change calculation in the `calculate_change` function.
- **How to Identify**: Incorrect output for the change.
- **Solution**: Fixed the subtraction logic by removing `- 0.10`.

---

## **Reflection**

### **1. Interpreted vs. Compiled Languages**
- **Python (Interpreted)**: Executes code line-by-line, no need to compile before running.
- **C++ (Compiled)**: Requires compiling source code into machine code before execution, which improves performance.

### **2. High-Level vs. Low-Level Languages**
- **High-Level (Python)**: Easier to write and understand, closer to human language.
- **Low-Level (Assembly)**: Directly interacts with hardware, more complex but faster.

---

## **Key Takeaways**
- Syntax errors are easy to identify with the IDE.
- Run-time errors require testing to uncover.
- Logic errors are the hardest and need careful debugging and testing.
