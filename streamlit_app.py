import streamlit as st
import requests

def get_answer(question):
    url = "https://api.afforai.com/api/api_completion"
    payload = {
        "apikey": "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e",
        "sessionid": "65489d7c9ad727940f2ab26f",
        "history": [{"role": "user", "content": question}],
        "powerful": False,
        "google": True
    }
    response = requests.post(url, json=payload)
    return response.json()["suggestedUserResponses"][0]

def main():
    st.title("Guatemala Legislation QA App")
    question = st.text_input("Ask a question")
    if st.button("Ask"):
        if question:
            answer = get_answer(question)
            st.write("Answer:", answer)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()
