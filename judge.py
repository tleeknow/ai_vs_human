import streamlit as st
import joblib
import joblib

# 모델 불러오기
model = joblib.load("text_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("✍️ 이 글, 사람이 썼을까? AI가 썼을까?")

text_input = st.text_area("아래에 글을 입력해보세요:")

if st.button("분석하기"):
    X = vectorizer.transform([text_input])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X).max()

    if pred == "human":
        st.success(f"✅ 이 글은 **사람이 쓴 글**일 가능성이 높아요! ({prob:.2%})")
    else:
        st.error(f"🤖 이 글은 **AI가 쓴 글**일 가능성이 높아요! ({prob:.2%})")
