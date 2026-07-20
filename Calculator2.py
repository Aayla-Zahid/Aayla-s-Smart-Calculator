import streamlit as st
import math

st.title("🧮Aayla's Smart Calculator")

if "expression" not in st.session_state:
    st.session_state.expression = ""
user_input = st.text_input("Enter your calculation:", value=st.session_state.expression)
st.session_state.expression = user_input
if "result" in st.session_state:
    st.write("### Result:", st.session_state.result)

col1,col2,col3,col4 = st.columns([4,4,4,4])
with col1:
    def press_7():
        st.session_state.expression += "7"
        pass
    st.button("7",use_container_width=True,on_click = press_7)
    def press_4():
        st.session_state.expression += "4"
        pass
    st.button("4",use_container_width=True,on_click = press_4)
    def press_1():
        st.session_state.expression += "1"
        pass
    st.button("1",use_container_width=True,on_click= press_1)
    def press_0():
        st.session_state.expression += "0"
        pass
    st.button("0",use_container_width=True,on_click = press_0)
    def press_sin():
        st.session_state.expression += "math.sin("

        pass
    st.button("sin",use_container_width=True,on_click= press_sin)
    def press_exp():
        st.session_state.expression += "**"
        pass
    st.button("exp",use_container_width=True,on_click= press_exp)
with col2:
    def press_8():
        st.session_state.expression += "8"
        pass
    st.button("8",use_container_width=True,on_click = press_8)
    def press_5():
        st.session_state.expression += "5"
        pass
    st.button("5",use_container_width=True,on_click = press_5)
    def press_2():
        st.session_state.expression += "2"
        pass
    st.button("2",use_container_width=True,on_click = press_2)
    def press_opening_bracket():
        st.session_state.expression += "("
        pass
    st.button("(",use_container_width=True,on_click = press_opening_bracket)
    def press_log():
        st.session_state.expression += "math.log("
        pass
    st.button("log",use_container_width=True,on_click=press_log)
    def press_cos():
        st.session_state.expression += "math.cos("
        pass
    st.button("cos",use_container_width=True,on_click=press_cos)
with col3:
    def press_9():
        st.session_state.expression += "9"
        pass
    st.button("9",use_container_width=True,on_click = press_9)
    def press_6():
        st.session_state.expression += "6"
        pass
    st.button("6",use_container_width=True,on_click = press_6)
    def press_3():
        st.session_state.expression += "3"
        pass
    st.button("3",use_container_width=True,on_click = press_3)
    def press_open_bracket():
        st.session_state.expression += ")"
        pass
    st.button(")",use_container_width=True,on_click = press_open_bracket)
    def press_tan():
        st.session_state.expression += "math.tan("
        pass
    st.button("tan",use_container_width=True,on_click = press_tan)
    def press_clear():
        st.session_state.expression = ""
        pass
    st.button("C",use_container_width=True,on_click = press_clear)
with col4:
    def press_divide():
        st.session_state.expression += "/"
    st.button("/",use_container_width=True,on_click = press_divide)

    def press_multiply():
        st.session_state.expression += "*"
        pass
    st.button("*",use_container_width=True,on_click = press_multiply)

    def press_minus():
        st.session_state.expression += "-"
        pass
    st.button("-",use_container_width=True,on_click = press_minus)

    def press_plus():
        st.session_state.expression += "+"
        pass
    st.button("+",use_container_width=True,on_click = press_plus)

    def press_percentage():
        st.session_state.expression += "%"
        pass
    st.button("%",use_container_width=True,on_click = press_percentage)


    def press_equals():
        try:
            st.session_state.result = eval(
                st.session_state.expression,
                {"math": math}
            )
        except Exception:
            st.session_state.result = "Invalid Expression"

    st.button("=", use_container_width=True, on_click=press_equals)












