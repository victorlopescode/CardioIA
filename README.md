# CardioIA
Projeto Acadêmico que simula o ecossistema de uma cardiologia moderna

# Projeto de Inteligência Artificial voltado à Saúde 🩺
## Parte 1 - Análise de Dados Numéricos (IoT)

Este repositório contém o dataset e a documentação técnica para a primeira etapa da atividade acadêmica de análise de dados aplicados à saúde. O foco aqui é a identificação de padrões e fatores de risco para doenças cardíacas.

---

### 📂 Acesso ao Dataset
O arquivo de dados está hospedado externamente para facilitar o consumo em larga escala:

* **Link para o Dataset:** (https://drive.google.com/file/d/1DU6tLje42IBXtSELJ9fdpNJkyNmAWmIE/view?usp=sharing)
* **Formato:** `.csv`
* **Quantidade de registros:** 1.025 linhas.

---

### 🔍 Origem e Descrição dos Dados
Os dados utilizados neste projeto são **reais** e provêm do **UCI Machine Learning Repository** (Dataset: *Heart Disease*). 

O conjunto de dados original foi coletado de quatro instituições médicas:
1. Cleveland Clinic Foundation
2. Hungarian Institute of Cardiology, Budapest
3. V.A. Medical Center, Long Beach, CA
4. University Hospital, Zurich, Switzerland

Ele é composto por 14 variáveis principais, incluindo idade, sexo, pressão arterial em repouso, colesterol, frequência cardíaca máxima e sintomas de dor no peito.

---

### 🏥 Relevância Clínica das Variáveis
Para um diagnóstico assistido por IA, selecionei as seguintes variáveis como as mais críticas:

1.  **Pressão Arterial em Repouso (`trestbps`):** Clinicamente, a hipertensão é o principal fator de risco para acidentes vasculares e infartos. Para a IA, essa variável serve como um indicador contínuo de estresse no sistema circulatório.
2.  **Colesterol Sérico (`chol`):** Níveis elevados de colesterol estão diretamente ligados à formação de placas de ateroma (obstrução arterial). É um dado vital para modelos preditivos de longo prazo.
3.  **Frequência Cardíaca Máxima (`thalach`):** Mede a capacidade de resposta do coração ao esforço. Valores baixos em situações de estresse podem indicar insuficiência ou danos no tecido cardíaco.

---

### 🤖 Importância para Projetos de IA em Saúde
A utilização de datasets estruturados como este permite que algoritmos de **Machine Learning** (como Regressão Logística ou Random Forest) aprendam a identificar correlações que podem não ser óbvias em uma análise rápida:

* **Triagem Automatizada:** Identificação rápida de pacientes de alto risco em prontos-socorros.
* **Medicina Preventiva:** Previsão da probabilidade de um evento cardíaco com base no histórico clínico, permitindo intervenções precoces.
* **Redução de Erros:** Apoio à decisão clínica, servindo como uma "segunda opinião" baseada em dados históricos globais.

