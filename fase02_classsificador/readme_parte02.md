# Classificador de Risco Cardiológico - Parte 2

## 📋 Descrição do Projeto

Este projeto faz parte da **Fase 2** da disciplina e consiste no desenvolvimento de um **classificador básico de texto** capaz de analisar frases com sintomas relatados por pacientes e classificá-las automaticamente como **"alto risco"** ou **"baixo risco"**.

O objetivo é simular, de forma simplificada, sistemas automatizados de triagem clínica utilizados para priorizar atendimentos com base na gravidade dos sintomas.

## 🛠️ Tecnologias Utilizadas

- Python 3
- Pandas
- Scikit-learn
- TF-IDF (vetorização de texto)
- Logistic Regression
- Matplotlib + Seaborn (visualizações)

## 📊 Dataset

- **Nome do arquivo**: `frases_risco.csv`
- **Quantidade de frases**: 60
- **Balanceamento**: 30 frases de "alto risco" + 30 frases de "baixo risco"
- As frases simulam sintomas cardiológicos graves e leves do dia a dia.

## 📈 Resultados Obtidos

- **Acurácia no conjunto de teste**: **100%**
- **Precisão, Recall e F1-score**: 1.00 para ambas as classes
- **Desempenho em frases novas**: Excelente generalização
  - Frases graves → Probabilidade de alto risco entre 66% e 80%
  - Frases leves → Probabilidade de alto risco entre 23% e 33%

O modelo conseguiu identificar corretamente padrões importantes, como:
- Palavras associadas a alto risco: "dor forte", "falta de ar", "suor frio", "palpitações", "tontura"
- Palavras associadas a baixo risco: "leve", "dorzinha", "incômodo", "cansaço normal"

## 📁 Estrutura do Repositório
classificador-risco-cardio/ 
├── frases_risco.csv
├── classificador_risco.ipynb
└── README.md