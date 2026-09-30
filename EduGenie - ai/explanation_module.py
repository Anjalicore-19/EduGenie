from transformers import pipeline

def get_explanation(concept: str) -> str:
    try:
        explainer_pipeline = pipeline("text2text-generation", model="MBZUAI/LaMini-Flan-T5-783M")
        prompt = f"Explain the concept of '{concept}' simply with an example for a student."
        result = explainer_pipeline(prompt, max_length=300, do_sample=True, temperature=0.7)
        return result[0]['generated_text']
    except Exception as e:
        return f"⚠️ Explanation Error: {e}"