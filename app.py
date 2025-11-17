import streamlit as st
from agent import ask_gemini as get_career_advice

st.set_page_config(page_title="Career Path Advisor AI", page_icon="🎯", layout="wide")

# -------------------- CSS --------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1c1f26, #2b2f3a);
    color: white;
}
.chat-box {
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 12px;
    max-width: 80%;
}
.user-msg {
    background: #4b82f2;
    margin-left: auto;
    color: white;
}
.ai-msg {
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(6px);
}
.header {
    font-size: 32px;
    text-align: center;
    font-weight: 700;
    padding: 10px;
    color: white;
    background: linear-gradient(90deg, #007bff, #00d4ff);
    border-radius: 12px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- Header --------------------
st.markdown('<div class="header">🎯 Career Path Advisor AI</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:18px;color:#cccccc;'>Your Personal AI Mentor for Smart Career Decisions</p>", unsafe_allow_html=True)

# -------------------- Chat Storage --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------- Input Handler --------------------
def send_message():
    user_text = st.session_state.career_input.strip()

    if user_text == "":
        return

    # User message store
    st.session_state.messages.append(("user", user_text))

    with st.spinner("AI thinking..."):
        ai_reply = get_career_advice(user_text)

    st.session_state.messages.append(("ai", ai_reply))

    # Clear input safely
    st.session_state.career_input = ""

# -------------------- Input Box --------------------
st.text_area(
    "Ask anything about your career...",
    key="career_input",
    height=80
)

st.button("🚀 Ask AI", on_click=send_message)

# -------------------- Chat Display --------------------
for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(
            f"<div class='chat-box user-msg'><b>🧑 You:</b><br>{msg}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='chat-box ai-msg'><b>🤖 AI:</b><br>{msg}</div>",
            unsafe_allow_html=True
        )
