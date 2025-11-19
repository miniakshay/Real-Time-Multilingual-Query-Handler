import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

@st.cache_resource
def load_model():
    model_name = "Helsinki-NLP/opus-mt-mul-en"  
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

st.title("🌐 Real-Time Multilingual Query Handler")

text = st.text_area("Enter your query:")

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        inputs = tokenizer(text, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=200)
        english = tokenizer.decode(outputs[0], skip_special_tokens=True)

        st.subheader("🟦 Translation (English)")
        st.success(english)
