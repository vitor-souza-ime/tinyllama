!pip install --upgrade transformers accelerate

import torch
from transformers import pipeline

# Carregar o modelo
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    torch_dtype=torch.bfloat16,  # usa menos memória
    device_map="auto"            # usa GPU se disponível
)

# Histórico do chat
messages = [
    {"role": "system", "content": "Você é um assistente amigável e prestativo."}
]

def conversar(pergunta):
    # Adiciona a fala do usuário
    messages.append({"role": "user", "content": pergunta})

    # Monta o prompt no formato correto de chat
    prompt = pipe.tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

    # Gera resposta
    output = pipe(
        prompt,
        max_new_tokens=500,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        top_k=50
    )

    # Pega só a parte nova do texto (a resposta)
    resposta = output[0]["generated_text"][len(prompt):].strip()

    # Adiciona resposta ao histórico
    messages.append({"role": "assistant", "content": resposta})

    return resposta


# Loop interativo
print("=== Chat com TinyLlama-1.1B-Chat ===")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat. Até mais!")
        break
    resposta = conversar(pergunta)
    print(f"TinyLlama: {resposta}\n")
