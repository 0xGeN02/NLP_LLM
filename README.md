# GalegoPro: Translation & Correction App

This application [repo](https://github.com/0xGeN02/NLP_LLM) rewrites text from any language into normative Galician. It uses:

- **Ollama3.1** as local LLM engine for advanced linguistic processing
- [`src.translator`](./src/translator.py) to detect and translate the text
- [`src.corrector`](./src/corrector.py) to correct grammatical issues in the translated text
- [`src.config`](./src/config.py) to configure and style the Streamlit interface

## Features

1. **Language Detection**  
   Uses [`detectar_idioma`](src/translator.py) to identify the source language automatically.

2. **Translation**  
   Leverages the [`obtener_traductor`](./src/translator.py) function to translate any input text into Galician.

3. **Correction**  
   Applies [`obtener_corrector`](./src/corrector.py) and [`corregir_texto`](./src/corrector.py) to refine grammar and syntax after translation.

## How to Use

### Install Dependencies  

```sh
   poetry install
   poetry shell
```

### Run the app

```sh
streamlit run main.py --server.fileWatcherType none
```

### Usage

1. Enter or paste the text you want to translate.
2. Click “Procesar texto” to run detection, translation, and correction.
3. Review the final output in Galician.

## Features

1. **Local LLM Processing**  
   Uses [`Ollama`](https://ollama.ai/) with custom-trained Galician language models for:
   - Context-aware translations
   - Grammatical nuance correction
   - Style adaptation to normative Galician

2. **Language Detection**  
   Uses [`detectar_idioma`](src/translator.py) with fallback to LLM when confidence < 75%

3. **Hybrid Correction System**  
   Combines:
   - Rule-based checks from `language_tool_python`
   - LLM-powered contextual corrections via Ollama

## Architecture

```mermaid
graph TD
    A[User Input] --> B(Language Detection)
    B --> C{Translation}
    C -->|Helsinki-NLP| D[Raw Galician]
    C -->|Ollama Fallback| D[Raw Galician]
    D --> E[Hybrid Correction]
    E --> F[Rule-Based Checks]
    E --> G[LLM Refinement]
    G --> H[Final Output]
```

### Visual

![Galeopro1](./static/galeopro1.png)

![Galeopro2](./static/galeopro2.png)

![Galeopro3](./static/galeopro3.png)

![Ollama3.1](./static/ollama3.1.png)

![Mermaid Graph](./static/mermaid.png)
