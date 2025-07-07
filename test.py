import streamlit as st

# 간단한 단어 기반 규칙 정의
ai_keywords = ["인공지능", "AI", "알고리즘", "효율", "자동화", "기술", "데이터", "산업", "생산성"]
human_keywords = ["나는", "생각한다", "느꼈다", "기억", "추억", "즐겁다", "감정", "우리", "행복"]

def simple_rule_based_predict(text):
    text = text.lower()
    ai_score = sum(text.count(word) for word in ai_keywords)
    human_score = sum(text.count(word) for word in human_keywords)

    if ai_score > human_score:
        return "AI", ai_score / (ai_score + human_score + 1e-5)
    elif human_score > ai_score:
        return "human", human_score / (ai_score + human_score + 1e-5)
    else:
        return "unknown", 0.5

# UI
st.title("✍️ 이 글, 사람이 썼을까? AI가 썼을까?")
text_input = st.text_area("아래에 글을 입력해보세요:")

if st.button("분석하기"):
    if not text_input.strip():
        st.warning("글을 입력해주세요!")
    else:
        pred, prob = simple_rule_based_predict(text_input)
        prob_percent = f"{prob:.2%}"

        if pred == "human":
            st.success(f"✅ 이 글은 **사람이 쓴 글**일 가능성이 높아요! ({prob_percent})")
        elif pred == "AI":
            st.error(f"🤖 이 글은 **AI가 쓴 글**일 가능성이 높아요! ({prob_percent})")
        else:
            st.info("🤔 AI인지 사람인지 판단하기 어려워요.")

