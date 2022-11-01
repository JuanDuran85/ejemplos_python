"""
Let's summarize a paragraph using One AI's Pipeline API
"""

import oneai
from dotenv import load_dotenv
import os

load_dotenv()

oneai.api_key = os.getenv("API_KEY_TWO") or ''
text_to_send: str = '''Insane - Am I the only motherfucker with a brain? I'm hearing voices but all they do is complain. How many times have you wanted to kill Everything and everyone - Say you'll do it but never will. You can't see California without Marlon Brando's eyes Can't see California without Marlon Brando's eyes. You can't see California without Marlon Brando's eyes'''

pipeline: oneai.Pipeline = oneai.Pipeline(
    steps = [
        oneai.skills.Topics(),
        oneai.skills.Numbers(),
        oneai.skills.Summarize(),
        oneai.skills.Sentiments(),
        oneai.skills.Emotions(),
        oneai.skills.DetectLanguage(),
        oneai.skills.Highlights(),
        oneai.skills.Names(),
        oneai.skills.Proofread(),
        oneai.skills.Pricing()
    ]
)

output_ai = pipeline.run(text_to_send)
print(output_ai)