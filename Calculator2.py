import streamlit as st
import math

st.title("🧮 Aayla's Smart Calculator")

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
    except Exception:
        st.session_state.result = "Invalid Expression"

# Added key and on_change to support Keyboard ENTER
user_input = st.text_input(
    "Enter your calculation:",
    value=st.session_state.expression,
    key="user_input",
    on_change=press_equals,
)

if "result" in st.session_state:
    st.write("### Result:", st.session_state.result)

# Expanded to 5 columns to cleanly accommodate all new functions
col1, col2, col3, col4, col5 = st.columns([4, 4, 4, 4, 4])

with col1:
    def press_7():
        st.session_state.expression += "7"
    st.button("7", use_container_width=True, on_click=press_7)
    
    def press_4():
        st.session_state.expression += "4"
    st.button("4", use_container_width=True, on_click=press_4)
    
    def press_1():
        st.session_state.expression += "1"
    st.button("1", use_container_width=True, on_click=press_1)
    
    def press_0():
        st.session_state.expression += "0"
    st.button("0", use_container_width=True, on_click=press_0)
    
    def press_sin():
        st.session_state.expression += "sin("
    st.button("sin", use_container_width=True, on_click=press_sin)
    
    def press_exp():
        st.session_state.expression += "**"
    st.button("exp", use_container_width=True, on_click=press_exp)

with col2:
    def press_8():
        st.session_state.expression += "8"
    st.button("8", use_container_width=True, on_click=press_8)
    
    def press_5():
        st.session_state.expression += "5"
    st.button("5", use_container_width=True, on_click=press_5)
    
    def press_2():
        st.session_state.expression += "2"
    st.button("2", use_container_width=True, on_click=press_2)
    
    def press_opening_bracket():
        st.session_state.expression += "("
    st.button("(", use_container_width=True, on_click=press_opening_bracket)
    
    def press_log():
        st.session_state.expression += "log("
    st.button("log", use_container_width=True, on_click=press_log)
    
    def press_cos():
        st.session_state.expression += "cos("
    st.button("cos", use_container_width=True, on_click=press_cos)

with col3:
    def press_9():
        st.session_state.expression += "9"
    st.button("9", use_container_width=True, on_click=press_9)
    
    def press_6():
        st.session_state.expression += "6"
    st.button("6", use_container_width=True, on_click=press_6)
    
    def press_3():
        st.session_state.expression += "3"
    st.button("3", use_container_width=True, on_click=press_3)
    
    def press_open_bracket():
        st.session_state.expression += ")"
    st.button(")", use_container_width=True, on_click=press_open_bracket)
    
    def press_tan():
        st.session_state.expression += "tan("
    st.button("tan", use_container_width=True, on_click=press_tan)
    
    def press_clear():
        st.session_state.expression = ""
    st.button("C", use_container_width=True, on_click=press_clear)

with col4:
    def press_divide():
        st.session_state.expression += "/"
    st.button("/", use_container_width=True, on_click=press_divide)

    def press_multiply():
        st.session_state.expression += "*"
    st.button("*", use_container_width=True, on_click=press_multiply)

    def press_minus():
        st.session_state.expression += "-"
    st.button("-", use_container_width=True, on_click=press_minus)

    def press_plus():
        st.session_state.expression += "+"
    st.button("+", use_container_width=True, on_click=press_plus)

    def press_percentage():
        st.session_state.expression += "%"
    st.button("%", use_container_width=True, on_click=press_percentage)

    st.button("=", use_container_width=True, on_click=press_equals)

# NEW 5th Column for Backspace, Factorial, Pi, e, Reciprocal, Mod
with col5:
    def press_backspace():
        st.session_state.expression = st.session_state.expression[:-1]
    st.button("⌫", use_container_width=True, on_click=press_backspace)

    def press_factorial():
        st.session_state.expression += "factorial("
    st.button("x!", use_container_width=True, on_click=press_factorial)

    def press_pi():
        st.session_state.expression += "pi"
    st.button("π", use_container_width=True, on_click=press_pi)

    def press_e():
        st.session_state.expression += "e"
    st.button("e", use_container_width=True, on_click=press_e)

    def press_reciprocal():
        st.session_state.expression += "1/("
    st.button("1/x", use_container_width=True, on_click=press_reciprocal)

    def press_mod():
        st.session_state.expression += " % "
    st.button("mod", use_container_width=True, on_click=press_mod)












