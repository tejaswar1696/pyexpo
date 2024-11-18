import streamlit as st
import random

def display_portfolio():
    st.header("Portfolio")
    st.write("Welcome to my portfolio!")
    st.write("I'm excited to share my projects and experiences with you.")
    st.write("About me:")
    st.write("Myself Tejaswar K from Btech IT")
    st.write("Highly motivated and detail-oriented individual with a passion for IoT.")
    st.write("Skills:")
    st.write("* Python")
    st.write("* Internet of Things")

def display_guessing_game():
    st.header("Guessing Game")
    mode = st.selectbox("Select Game Mode", ["User Guessing", "Machine Guessing"])

    if mode == "User Guessing":
        display_user_guessing_game()
    elif mode == "Machine Guessing":
        display_machine_guessing_game()

def display_user_guessing_game():
    st.subheader("User Guessing Mode")
    st.write("Rules:")
    st.write("* I'll think of a number between 1 and 100")
    st.write("* You'll have to guess the number")
    st.write("* After each guess, I'll tell you if your guess is higher or lower than the number")
    st.write("* Your goal is to guess the number in as few attempts as possible")

    if 'user_guessing_number' not in st.session_state:
        st.session_state.user_guessing_number = random.randint(1, 100)
        st.session_state.user_guessing_attempts = 0
        st.session_state.user_guessing_min_val = 1
        st.session_state.user_guessing_max_val = 100

    guess = st.number_input("Guess a number", min_value=st.session_state.user_guessing_min_val, max_value=st.session_state.user_guessing_max_val)

    if st.button("Submit Guess"):
        st.session_state.user_guessing_attempts += 1

        if guess < st.session_state.user_guessing_number:
            st.write("Too low!")
            st.session_state.user_guessing_min_val = max(guess + 1, st.session_state.user_guessing_min_val)
        elif guess > st.session_state.user_guessing_number:
            st.write("Too high!")
            st.session_state.user_guessing_max_val = min(guess - 1, st.session_state.user_guessing_max_val)
        else:
            st.write(f"Congratulations! You guessed the number in {st.session_state.user_guessing_attempts} attempts.")
            if st.button("Play Again"):
                reset_user_guessing_game()

def reset_user_guessing_game():
    st.session_state.user_guessing_number = random.randint(1, 100)
    st.session_state.user_guessing_attempts = 0
    st.session_state.user_guessing_min_val = 1
    st.session_state.user_guessing_max_val = 100


def display_machine_guessing_game():
    st.subheader("Machine Guessing Mode")
    st.write("Rules:")
    st.write("* You'll think of a number between 1 and 100")
    st.write("* I'll try to guess the number using binary search")
    st.write("* After each guess, you'll tell me if my guess is higher or lower than the number")


    if 'machine_guessing_min_val' not in st.session_state:
        reset_machine_guessing_game()

    guess = (st.session_state.machine_guessing_min_val + st.session_state.machine_guessing_max_val) // 2
    st.write(f"My guess is: {guess}")

    feedback = st.selectbox("Is my guess:", ["Too low", "Too high", "Correct"])

    if feedback == "Too low":
        st.session_state.machine_guessing_min_val = guess + 1
        st.session_state.machine_guessing_attempts += 1
    elif feedback == "Too high":
        st.session_state.machine_guessing_max_val = guess - 1
        st.session_state.machine_guessing_attempts += 1
    elif feedback == "Correct":
        st.write(f"Yay! I guessed the number in {st.session_state.machine_guessing_attempts} attempts.")
        if st.button("Play Again"):
            reset_machine_guessing_game()

def reset_machine_guessing_game():
    st.session_state.machine_guessing_min_val = 1
    st.session_state.machine_guessing_max_val = 100
    st.session_state.machine_guessing_attempts = 0

def main():
    display_portfolio()
    display_guessing_game()

if __name__=="__main__":
     main()