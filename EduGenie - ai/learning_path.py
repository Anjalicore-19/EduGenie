from transformers import pipeline

def get_learning_recommendations(topic: str) -> str:
    try:
        roadmap_pipeline = pipeline("text2text-generation", model="MBZUAI/LaMini-Flan-T5-783M")
        prompt = f"Provide a step-by-step roadmap to learn {topic} from beginner to advanced."
        result = roadmap_pipeline(prompt, max_length=350, do_sample=True, temperature=0.7)
        return result[0]['generated_text']
    except Exception as e:
        return f"⚠️ Learning Path Error: {e}"