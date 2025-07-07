import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("ai_vs_human.csv")  # 파일명 확인
    return df

df = load_data()

# 모델 학습 함수
@st.cache_resource
def train_model(df):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["text"])
    y = df["label"]  # 'human' 또는 'AI'로 구성되어 있어야 함
    model = LogisticRegression()
    model.fit(X, y)
    return model, vectorizer

model, vectorizer = train_model(df)

# UI 구성
st.title("✍️ 이 글, 사람이 썼을까? AI가 썼을까?")
text_input = st.text_area("아래에 글을 입력해보세요:")

if st.button("분석하기"):
    if not text_input.strip():
        st.warning("글을 입력해주세요!")
    else:
        X_input = vectorizer.transform([text_input])
        pred = model.predict(X_input)[0]
        prob = model.predict_proba(X_input).max()

        if pred == "human":
            st.success(f"✅ 이 글은 **사람이 쓴 글**일 가능성이 높아요! ({prob:.2%})")
        else:
            st.error(f"🤖 이 글은 **AI가 쓴 글**일 가능성이 높아요! ({prob:.2%})")
