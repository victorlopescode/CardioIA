# Classificador de Risco Cardiológico - Parte 2

## 📋 Descrição do Projeto

Este projeto faz parte da **Fase 2** da disciplina e consiste no desenvolvimento de um **classificador básico de texto** capaz de analisar frases com sintomas relatados por pacientes e classificá-las automaticamente como **"alto risco"** ou **"baixo risco"**.

O objetivo é simular, de forma simplificada, sistemas automatizados de triagem clínica utilizados para priorizar atendimentos com base na gravidade dos sintomas.

## 💻Link do vídeo no youtube

Esse é o link do vídeo onde o código da Parte 2 do trabalho (Classificador básico de texto) é excecutado
https://youtu.be/9P_L5L4ze7c

## 🛠️ Tecnologias Utilizadas

- Python 3
- Pandas
- Scikit-learn
- TF-IDF (vetorização de texto)
- Logistic Regression
- Matplotlib + Seaborn (visualizações)

## 📊 Datasets

**Analisador (`analisador_cardio.py`):**
- `dados/mapa_pares_sintomas_doencas.csv` — mapa de sintomas e doenças associadas
- `dados/frases_sintomas_2000.txt` — 2.000 frases sintéticas de pacientes

**Classificador (`classificador_risco.ipynb`):**
- `dados/base_rotulada_risco_15000.csv` — 15.000 frases rotuladas como `alto_risco` ou `baixo_risco`
- Balanceamento: 7.500 por classe

## 📈 Resultados Obtidos

- **Modelo**: Logistic Regression + TF-IDF (até 500 termos)
- **Divisão**: 12.000 treino / 3.000 teste (80/20, estratificado)
- **Generalização**: boa discriminação entre sintomas graves e leves em frases novas

## 📁 Estrutura da Fase 2
fase2/
├── analisador_cardio.py
├── classificador_risco.ipynb
├── README.md
└── dados/
    ├── mapa_pares_sintomas_doencas.csv
    ├── frases_sintomas_2000.txt
    └── base_rotulada_risco_15000.csv
