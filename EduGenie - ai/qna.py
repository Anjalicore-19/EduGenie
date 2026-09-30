from transformers import pipeline

print("Loading Q&A Model into memory...")
qa_pipeline = pipeline("text-generation", model="google/flan-t5-small")
print("Q&A Model loaded successfully!")

def answer_question(question: str) -> str:
    try:
        prompt = f"Answer this question in detail: {question}"
        result = qa_pipeline(prompt, max_length=256, do_sample=True, temperature=0.7)
        return result[0]['generated_text']
    except Exception as e:
        return f"⚠️ Q&A Error: {e}"