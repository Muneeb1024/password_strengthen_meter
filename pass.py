import re
import streamlit as st

# app styling
st.set_page_config(page_title="Password Strength Meter By Muneeb Lodhi", page_icon="🔑", layout="centered")

st.markdown("""
            <style>
            .main {text-align: center;}
            .stTextInput {width: 60% !important; margin:auto }
            .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px; }
            </style>
            """, unsafe_allow_html=True)
            # .stButton button:hover {background-color: ;}

# page Title ond description
st.title("🔐Password Strength Meter")
st.write("Enter your password below to check its security level.🔍")

# function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score +=1 #increase score by 1
    else: 
        feedback.append("❌ Password should contain atleast 8 character")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include upper and lowercase (a-z)")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain atleast one number")    

    #special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include atleast one special character")     

#dispay password result

    if score == 4:
        st.success("✅ Strong Password - Your Password is Secure.") 
    elif score ==3:
        st.info("⚠️ Moderate Password - Consider improving security by adding moere feature")
    else:
        st.error("❌ Weak Password - Follow the suggestion below to strength it.")

    #feedback
    if feedback:
        with st.expander("🔍 Improve Your Password"):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter Your Password:", type= "password", help = "Ensure Your Password is strong 🔒")

#Button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️Please enter a password first") #show warning if password is empty    
