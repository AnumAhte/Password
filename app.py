import streamlit as st
import re

# --- Streamlit UI Customization ---
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .main-container {
            background: #ffffff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .stButton>button {
            background: linear-gradient(45deg, #6a11cb, #2575fc);
            color: white;
            font-size: 16px;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 8px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #2575fc, #6a11cb);
        }
        .strong {color: green; font-weight: bold;}
        .moderate {color: orange; font-weight: bold;}
        .weak {color: red; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# --- Password Strength Function ---
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

# --- Streamlit UI ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("🔒 Password Strength Checker")

# Password Input
password = st.text_input("Enter your password", type="password")

# Check Button
if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)
        
        # Determine strength
        if score == 4:
            st.success("✅ Strong Password!")
            st.markdown("<p class='strong'>Your password meets all security criteria! 🔒</p>", unsafe_allow_html=True)
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
            st.markdown("<p class='moderate'>Try improving it using the suggestions below. 🛠️</p>", unsafe_allow_html=True)
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")
            st.markdown("<p class='weak'>Your password is missing key security elements. 🚨</p>", unsafe_allow_html=True)
        
        # Display feedback
        for msg in feedback:
            st.write(msg)
    else:
        st.error("⚠️ Please enter a password to check its strength!")

st.markdown('</div>', unsafe_allow_html=True)
