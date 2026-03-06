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

---
## Parte 2 - Dados Textuais (NLP)
Este repositório também inclui análises de textos médicos relacionados a cardiologia, estes textos foram selecionados com o propósito de serem utilizados para extrair insights clínicos relevantes através de técnicas de Processamento de Linguagem Natural (NLP).

### 📄 Arquivo de texto: Estratégia Fármaco-Invasiva no Infarto do Miocárdio: Análise Descritiva, Apresentação de Sintomas Isquêmicos e Preditores de Mortalidade

O texto médico sobre infarto do miocárdio será processado por NLP para:

- **Extração de entidades (NER)**: Identificar sintomas (dor típica/atípica, dispneia), subgrupos (mulheres, idosos, diabéticos) e preditores (Killip-Kimball, ORs).

- **Classificação de tópicos**: Separar seções como resumo, métodos, resultados e conclusão para análise estruturada.

- **Análise de sentimentos**: Detectar tons positivos/negativos em achados (ex: disparidades em mulheres).

- **Sumarização**: Gerar resumos automáticos de resultados chave, como mortalidade 5,6% e atrasos em subgrupos.

---
**Relevancia na analise desse texto para o projeto:**
Essas análises com NLP pegam informações importantes do texto (sintomas, grupos de risco, atrasos no tratamento) e transformam em dados que a inteligência artificial entende rápido. No CardioIA, isso ajuda a:
- detectar sintomas de infarto mais cedo (mesmo os atípicos em mulheres ou idosos),
- prever quem tem mais risco de complicações,
- reduzir atrasos no atendimento,
- melhorar triagem, diagnósticos e alertas automáticos no sistema.

---
### 📄 Arquivo de texto: Revisão Sistemática sobre a Eficácia de Metas Intensivas do Tratamento Anti-Hipertensivo: Recomendação da Sociedade Brasileira de Cardiologia (SBC)

O texto sobre revisão sistemática da SBC será explorado por algoritmos de NLP para:

- **Extração de entidades (NER)**: Identificar metas de pressão (<130/80 mmHg vs ≥130/80), desfechos (infarto, AVC, mortalidade, doença renal), medicamentos e fatores (idade, fragilidade, risco CV).
- **Classificação de tópicos**: Separar resumo, métodos (ECRs, metanálise, GRADE), resultados (redução 13-17%) e conclusão (individualização do tratamento).
- **Extração de relações**: Ligar metas intensivas → redução de eventos CV (13-17%), sem impacto na mortalidade total.
- **Sumarização automática**: Gerar resumo curto dos achados principais (ex: evidência alta para redução de infarto/AVC).
- **Análise de recomendações**: Detectar frases de orientação clínica (individualizar metas, priorizar adesão).

---
**Relevancia na analise desse texto para o projeto:**

Essas análises com NLP pegam do texto coisas úteis como metas de pressão, redução de riscos (infarto, AVC) e recomendações da SBC.  
No CardioIA, isso ajuda a:  
- entender melhor como controlar a pressão alta para prevenir problemas cardíacos,  
- identificar automaticamente as melhores metas de tratamento para cada paciente,  
- alertar sobre riscos e adesão ao remédio de forma rápida,  
- melhorar triagem, prevenção e decisões no sistema de cardiologia.

## Parte 3 – Dados Visuais (Visão Computacional)

Para esta etapa do projeto foram utilizadas imagens de **Eletrocardiograma (ECG)** obtidas a partir de um dataset público de exames cardíacos.

As imagens representam **batimentos cardíacos individuais extraídos de registros de ECG**, permitindo analisar os padrões elétricos do coração por meio de técnicas de **Visão Computacional**.

### Fonte do Dataset

Dataset utilizado:
https://www.kaggle.com/datasets/erhmrai/ecg-image-data

As imagens foram organizadas em diferentes classes que representam padrões distintos de atividade elétrica cardíaca.

### Classes utilizadas

O conjunto de dados contém as seguintes categorias:

- **N (Normal)** – Batimento cardíaco normal  
- **S (Supraventricular)** – Batimentos originados acima dos ventrículos  
- **V (Ventricular)** – Batimentos originados nos ventrículos  
- **F (Fusion Beat)** – Combinação entre batimento normal e ventricular  
- **Q (Unknown)** – Batimentos não classificados ou com ruído  
- **M (Myocardial Infarction)** – Padrões associados ao infarto do miocárdio  

Para garantir diversidade e equilíbrio no conjunto de dados, foram selecionadas **50 imagens de cada classe**, totalizando **300 imagens de ECG** utilizadas no projeto.

### Link para acesso às imagens

As imagens utilizadas neste projeto estão disponíveis no link abaixo:

(https://drive.google.com/drive/folders/1qGjUlAX4pEP6hlwazyKVyHfKU7NDyixx?usp=drive_link)

### Aplicação em Visão Computacional

As imagens de ECG podem ser analisadas por algoritmos de **Visão Computacional** para identificar padrões elétricos cardíacos presentes nas ondas do eletrocardiograma, como:

- **Onda P**
- **Complexo QRS**
- **Onda T**

A partir dessas características, modelos de Inteligência Artificial podem ser treinados para:

- detectar arritmias
- identificar padrões anormais de batimentos
- classificar diferentes tipos de alterações cardíacas
- auxiliar no diagnóstico precoce de doenças cardiovasculares

Esse tipo de abordagem tem grande relevância na área da saúde, pois permite desenvolver sistemas capazes de apoiar médicos na análise de exames cardíacos e melhorar a eficiência do diagnóstico clínico.