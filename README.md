# TinyLlama Chatbot 🚀

Este repositório contém um exemplo de chatbot utilizando o modelo **[TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)** através da biblioteca [Transformers](https://huggingface.co/docs/transformers/index) da Hugging Face.  

O código foi desenvolvido em **Python** e permite conversas interativas em linha de comando, aproveitando GPU (se disponível) para acelerar a inferência.

---

## 📌 Requisitos

Antes de rodar o projeto, certifique-se de ter instalado:

- Python 3.9+  
- [PyTorch](https://pytorch.org/) com suporte a CUDA (opcional, mas recomendado)  
- Pacotes necessários:
  ```bash
  pip install --upgrade torch transformers accelerate
````

---

## 📂 Estrutura do Repositório

```
tinyllama/
│── main.py      # Código principal do chatbot
│── README.md    # Documentação
```

---

## ▶️ Como Executar

Clone o repositório:

```bash
git clone https://github.com/vitor-souza-ime/tinyllama.git
cd tinyllama
```

Execute o chatbot:

```bash
python main.py
```

---

## 💻 Uso

Quando rodar o programa, você verá algo assim:

```
=== Chat com TinyLlama-1.1B-Chat ===
Digite 'sair' para encerrar.
```

Depois basta digitar suas perguntas:

```
Você: O que é machine learning?
TinyLlama: Machine learning é uma área da inteligência artificial que ensina computadores a aprenderem a partir de dados...
```

Para encerrar o chat:

```
Você: sair
Encerrando o chat. Até mais!
```

---

## ⚡ Recursos Técnicos

* **Modelo:** TinyLlama-1.1B-Chat-v1.0
* **Geração de texto:** `transformers.pipeline`
* **Histórico de mensagens:** suporte a múltiplas interações no estilo chat
* **Aceleração:** utiliza GPU automaticamente se disponível (`device_map="auto"`)
* **Eficiência:** roda em `torch_dtype=torch.bfloat16` para reduzir uso de memória

---

## 📊 Verificar Instalação do PyTorch

Para confirmar se sua instalação do PyTorch reconhece a GPU, rode:

```python
import torch
print("Versão do PyTorch:", torch.__version__)
print("CUDA disponível:", torch.cuda.is_available())
print("Versão do CUDA:", torch.version.cuda)
```

---

## 📜 Licença

Este projeto é apenas para fins de estudo e demonstração. O modelo TinyLlama é disponibilizado pela comunidade de pesquisa, consulte a [licença oficial](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) para detalhes.

