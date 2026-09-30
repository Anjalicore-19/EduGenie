from transformers import pipeline

def generate_quiz(topic: str) -> str:
    try:
        quiz_pipeline = pipeline("text2text-generation", model="MBZUAI/LaMini-Flan-T5-783M")
        prompt = f"Create a quiz with 3 questions about {topic} with answers."
        result = quiz_pipeline(prompt, max_length=300, do_sample=True, temperature=0.7)
        return result[0]['generated_text']
    except Exception as e:
        return f"⚠️ Quiz Error: {e}"