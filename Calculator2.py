import streamlit as st
import math

st.title("🧮 Aayla's Smart Calculator")

# 1. Initialize state variables
if "expression" not in st.session_state:
    st.session_state.expression = ""

def press_equals():
    try:
        expr = st.session_state.get("user_input", st.session_state.expression)
        
        # Auto-close missing parentheses if forgotten (e.g., 'sin(30' -> 'sin(30)')
        open_b = expr.count("(")
        close_b = expr.count(")")
        if open_b > close_b:
            expr += ")" * (open_b - close_b)

        # Custom allowed math context
        allowed_globals = {
            "sin": lambda deg: math.sin(math.radians(deg)),
            "cos": lambda deg: math.cos(math.radians(deg)),
            "tan": lambda deg: math.tan(math.radians(deg)),
            "log": math.log10,
            "factorial": math.factorial,
            "pi": math.pi,
            "e": math.e,
            "math": math,
        }

        result = eval(expr, allowed_globals)
        
        if isinstance(result, float):
            result = round(result, 6)
            
        st.session_state.result = result
        st.session_state.expression = str(result)
        st.session_state.user_input = str(result)
    except Exception:
        st.session_state.result = "Invalid Expression"

# Sync typed input with buttons
def sync_input():
    st.session_state.expression = st.session_state.user_input

# Text input for keyboard typing + Enter key support
st.text_input(
    "Enter your calculation:",
    value=st.session_state.expression,
    key="user_input",
    on_change=press_equals,
)

if "result" in st.session_state:
    st.write("### Result:", st.session_state.result)

# Helper function to append values safely for BOTH state keys
def add_val(val):
    st.session_state.expression += str(val)
    st.session_state.user_input = st.session_state.expression

def do_clear():
    st.session_state.expression = ""
    st.session_state.user_input = ""

def do_backspace():
    st.session_state.expression = st.session_state.expression[:-1]
    st.session_state.user_input = st.session_state.expression

# 5 Columns Layout
col1, col2, col3, col4, col5 = st.columns([4, 4, 4, 4, 4])

with col1:
    st.button("7", use_container_width=True, on_click=lambda: add_val("7"))
    st.button("4", use_container_width=True, on_click=lambda: add_val("4"))
    st.button("1", use_container_width=True, on_click=lambda: add_val("1"))
    st.button("0", use_container_width=True, on_click=lambda: add_val("0"))
    st.button("sin", use_container_width=True, on_click=lambda: add_val("sin("))
    st.button("exp", use_container_width=True, on_click=lambda: add_val("**"))

with col2:
    st.button("8", use_container_width=True, on_click=lambda: add_val("8"))
    st.button("5", use_container_width=True, on_click=lambda: add_val("5"))
    st.button("2", use_container_width=True, on_click=lambda: add_val("2"))
    st.button("(", use_container_width=True, on_click=lambda: add_val("("))
    st.button("log", use_container_width=True, on_click=lambda: add_val("log("))
    st.button("cos", use_container_width=True, on_click=lambda: add_val("cos("))

with col3:
    st.button("9", use_container_width=True, on_click=lambda: add_val("9"))
    st.button("6", use_container_width=True, on_click=lambda: add_val("6"))
    st.button("3", use_container_width=True, on_click=lambda: add_val("3"))
    st.button(")", use_container_width=True, on_click=lambda: add_val(")"))
    st.button("tan", use_container_width=True, on_click=lambda: add_val("tan("))
    st.button("C", use_container_width=True, on_click=do_clear)

with col4:
    st.button("/", use_container_width=True, on_click=lambda: add_val("/"))
    st.button("*", use_container_width=True, on_click=lambda: add_val("*"))
    st.button("-", use_container_width=True, on_click=lambda: add_val("-"))
    st.button("+", use_container_width=True, on_click=lambda: add_val("+"))
    st.button("%", use_container_width=True, on_click=lambda: add_val("%"))
    st.button("=", use_container_width=True, on_click=press_equals)

with col5:
    st.button("⌫", use_container_width=True, on_click=do_backspace)
    st.button("x!", use_container_width=True, on_click=lambda: add_val("factorial("))
    st.button("π", use_container_width=True, on_click=lambda: add_val("pi"))
    st.button("e", use_container_width=True, on_click=lambda: add_val("e"))
    st.button("1/x", use_container_width=True, on_click=lambda: add_val("1/("))
    st.button("mod", use_container_width=True, on_click=lambda: add_val(" % "))
