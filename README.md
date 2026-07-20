# 🧮 Aayla's Smart Calculator

## Description

Aayla's Smart Calculator is a calculator application built using **Python** and **Streamlit**. It provides a simple and user-friendly interface for performing both basic arithmetic and scientific calculations.

The calculator supports keyboard input as well as on-screen buttons, allowing users to either type mathematical expressions directly or build them using the calculator interface.

## Features

* ➕ Basic arithmetic operations

  * Addition (`+`)
  * Subtraction (`-`)
  * Multiplication (`*`)
  * Division (`/`)
  * Exponent (`**`)
  * Modulus (`%`)

* 📐 Scientific functions

  * `sin()`
  * `cos()`
  * `tan()`
  * `log()`

* 🔢 Supports brackets for complex expressions.

* 🧮 Automatically follows the correct order of operations (BODMAS/DMAS) when evaluating expressions.

* ⌨️ **Keyboard-controlled** – users can type expressions directly into the input field.

* 🖱️ **Button-controlled** – expressions can also be created using the on-screen calculator buttons.

* 🧹 Clear button to reset the current expression.

* ⚠️ Displays an error message for invalid expressions.

## Technologies Used

* Python
* Streamlit
* Math Module

## How to Run

1. Clone this repository.
2. Install Streamlit:

   ```bash
   pip install streamlit
   ```
3. Run the application:

   ```bash
   streamlit run calculator.py
   ```

## Example Expressions

```text
25 + 15
(10 + 5) * 3
math.sin(1.57)
math.cos(0)
math.tan(0.5)
math.log(100)
2 ** 5
50 % 6
```

## Project Purpose

This project was created to practice Python programming, Streamlit UI development, session state management, event handling with buttons, and expression evaluation. It demonstrates how to build an interactive scientific calculator with both keyboard and button-based input.

