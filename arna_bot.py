import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

api_key = st.secrets["API_KEY"]
st.set_page_config(page_title="Titli AI⭐🌟🌍👽🤖☄", page_icon="💩")
st.markdown("<h1 class=hdr>Cutie AI</h1>", True)

model = ChatGoogleGenerativeAI(google_api_key=api_key, model="gemini-1.5-pro")
st.markdown("#### Meowww 😺.")

msgg = st.text_input("What's the matter ????")

if len(msgg) > 0:
    prompt = ChatPromptTemplate([("Ummm So Let me help youuuu"),
                                 ("Here is my message:{msg}")])
    chain = ({"msg": RunnablePassthrough()} | prompt | model | StrOutputParser())
    reply = chain.invoke(msgg)
    st.write(reply)

# CSS for color-changing background
background_style = """
<style>
    @keyframes gradient {
        0% { background-color: #ff0000; }
        25% { background-color: #00ff00; }
        50% { background-color: #0000ff; }
        75% { background-color: #ffff00; }
        100% { background-color: #ff0000; }
    }
    body {
        animation: gradient 15s ease infinite;
    }
    .hdr {
        text-shadow: 0px 0px 15px red;
        animation: colranim 15s ease infinite;
    }
    @keyframes colranim {
        0% {
            text-shadow: 0px 0px 15px red;
        }
        10% {
            text-shadow: 0px 0px 15px cyan;
        }
        20% {
            text-shadow: 0px 0px 15px green;
        }
        30% {
            text-shadow: 0px 0px 15px blue;
        }
        40% {
            text-shadow: 0px 0px 15px yellow;
        }
        50% {
            text-shadow: 0px 0px 15px magenta;
        }
        60% {
            text-shadow: 0px 0px 15px hotpink;
        }
        70% {
            text-shadow: 0px 0px 15px orange;
        }
        80% {
            text-shadow: 0px 0px 15px smokewhite;
        }
        90% {
            text-shadow: 0px 0px 15px purple;
        }
        100% {
            text-shadow: 0px 0px 15px red;
        }
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .st-emotion-cache-z5fcl4 {display: none;}
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: rgb(20, 20, 20);
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        box-shadow: 0 -4px 5px rgba(200, 100, 100, 0.1);
    }
</style>
<div class="footer">
    👨‍💻 Developed by <a style="text-decoration:none;color:red" href="" target="_blank">Prithwish Ganguly</a> | 
    📧 <a style="text-decoration:none;color:red" href="mailto:prithwishg@icloud.com">Contact Us</a>
</div>
"""

st.markdown(background_style, True)
