import streamlit as st
import random

p_l = [

            "Are you a wifi signal? Because I'm feeling a strong connection.",
            "Do you have a name, or can I call you mine?",
            "Are you a camera? Because every time I see you, I smile.",
            "Is your name Google? Because you've got everything I'm searching for.",
            "Are you a magician? Because whenever I look at you, everyone else disappears.",
            "Do you have a map? I keep getting lost in your eyes.",
            "Excuse me, but I think you dropped something: MY JAW!",
            "Are you a bank loan? Because you have my interest!",
            "If you were a cat, you'd purr-fect.",
            "Excuse me, but I think the stars tonight are outshone by your smile.",
            "Is your name Wi-fi? Because I'm really feeling a connection.",
            "Are you French? Because Eiffel for you.",
            "Is your name Ariel? Because we mermaid for each other.",
            "Do you have a pencil? Because I want to erase your past and write our future.",
            "If you were a vegetable, you'd be a cute-cumber.",
            "Are you made of copper and tellurium? Because you're Cu-Te.",
            "Excuse me, but I think you owe me a drink. When I looked at you, I dropped mine.",
            "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
            "Are you a parking ticket? Because you've got 'Fine' written all over you.",
            "If beauty were time, you'd be an eternity.",
            "Do you have a sunburn, or are you always this hot?",
            "Is this the Hogwarts Express? Because it feels like you and I are headed somewhere magical.",
            "Do you believe in love at first sight, or should I walk by again?",
            "Is your name Ariel? Because we mermaid for each other.",
            "Do you have a pencil? Because I want to erase your past and write our future.",
            "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
            "Excuse me, do you have a name or can I call you mine?",
            "Is this the Hogwarts Express? Because it feels like you and I are headed somewhere magical.",
            "Are you a time traveler? Because I can't imagine my future without you.",
            "Do you have a sunburn, or are you always this hot?",
            "If you were a cat, you'd purr-fect.",
            "Excuse me, but I think the stars tonight are outshone by your smile.",
            "Is your name Wi-fi? Because I'm really feeling a connection.",
            "Are you French? Because Eiffel for you.",
            "Is your name Ariel? Because we mermaid for each other.",
            "Do you have a pencil? Because I want to erase your past and write our future.",
            "Are you a bank loan? Because you have my interest!",
            "Do you have a map? I keep getting lost in your eyes.",
            "Excuse me, but I think you dropped something: MY JAW!",
            "Is your name Google? Because you've got everything I'm searching for.",
            "Do you believe in love at first sight, or should I walk by again?",
            "If you were a vegetable, you'd be a cute-cumber.",
            "Are you made of copper and tellurium? Because you're Cu-Te.",
            "Excuse me, but I think you owe me a drink. When I looked at you, I dropped mine.",
            "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
            "Are you a parking ticket? Because you've got 'Fine' written all over you."
        ]

st.title("Random Pick Up Line Generator")

def generate_pul():
    rand_idx = random.randrange(len(p_l))
    random_num = p_l[rand_idx]
    st.write("Your Generated Pickup Line Is :\n", random_num)

pul_button = st.button("Generate PickUp Line")

if pul_button:
    generate_pul()