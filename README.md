# Customer Service Chatbot

This repository contains a **Customer Service Chatbot** powered by a **LoRA fine-tuned LLaMA model**. The chatbot is designed to handle queries in the **retail banking** domain using a fine-tuned language model and placeholder-value replacement strategy for realistic conversation flows.


## Overview

- Fine-tuned LLaMA model using **LoRA (Low-Rank Adaptation)** techniques.
- Trained using the [Bitext Retail Banking LLM Chatbot Training Dataset](https://huggingface.co/datasets/bitext/Bitext-retail-banking-llm-chatbot-training-dataset).
- Dataset was preprocessed to replace **placeholders** (e.g., `{{Full Name}}`) with realistic values.
- Model was trained on **Google Colab**, then quantized to **4-bit GGUF format** for efficient local inference with Ollama.
- Streamlit app allows users to interact with the chatbot in a simple web interface.


## Directory Structure
```
CustomerService-Chatbot/  
│
├── chatbot.py                                                              # Streamlit app to run the chatbot    
│
├── placeholder_checking_script.py                                          # Detects placeholders and writes them to placeholders.txt    
│
├── placeholder_replacement_script.py                                       # Replaces placeholders with actual values    
│
├── placeholder_values.py                                                   # Stores placeholder-value mapping     
│
├── requirements.txt                                                        # Python dependencies  
```

## Resources

- **Google Colab (Model Fine-Tuning)**:  
  [Colab Notebook](https://colab.research.google.com/drive/1VHqkPcDDCdZsfBxjsa9oOrTSeQoSKBaO?usp=sharing)

- **Dataset (HuggingFace)**:  
  [Bitext Retail Banking Dataset](https://huggingface.co/datasets/bitext/Bitext-retail-banking-llm-chatbot-training-dataset)


## Prerequisites
- Python 3.12.4
- Ollama 0.6.1 or above

## Installation & Setup

> Ensure you have [Ollama](https://ollama.com/) installed to run the Llama model.

### 1. Clone the Repository

```
git clone https://github.com/HafsaManan1/CustomerService-Chatbot.git
cd CustomerService-Chatbot
```

### 2. Create Virtual Environment

    
    python -m venv venv

### 3. Activate Virtual Environment

    venv\Scripts\activate (Windows)

    source venv/bin/activate (macOS/ Linux)

### 4. Install the requirements 

    pip install -r requirements.txt

### 5. Pull Ollama custom model

    ollama pull hafsamanan/chatbot2.0

### 6. Run Streamlit Chatbot

    streamlit run chatbot.py