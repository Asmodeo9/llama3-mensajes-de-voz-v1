from gtts import gTTS
import os
from groq import Groq

print("Mensaje: ")
message = input()

client = Groq(
    api_key="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"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": message,
        }
    ],
    model="llama3-70b-8192",
)

# Asigna la respuesta del modelo a llm_response
llm_response = chat_completion.choices[0].message.content
print(llm_response)

# Configura el idioma a español
language = "es"

# Convierte el texto a voz usando gTTS
speech = gTTS(text=str(llm_response), lang=language, slow=False)

# Guarda el archivo de audio
speech.save("texto.mp3")

# Reproduce el archivo de audio
os.system("start texto.mp3")  # Para Windows
# Para macOS usa: os.system("afplay texto.mp3")
# Para Linux usa: os.system("mpg321 texto.mp3")






        






