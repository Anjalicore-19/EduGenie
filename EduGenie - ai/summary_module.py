from transformers import pipeline

def summarize_text(text: str) -> str:
    try:
        summarizer_pipeline = pipeline("text2text-generation", model="MBZUAI/LaMini-Flan-T5-783M")
        prompt = f"Summarize the following text into key bullet points:\n{text}"
        result = summarizer_pipeline(prompt, max_length=200, do_sample=True, temperature=0.5)
        return result[0]['generated_text']
    except Exception as e:
        return f"⚠️ Summarizer Error: {e}"