# CardioIA — pacote simplificado de dados

## Objetivo
Este pacote foi simplificado para ficar alinhado com a divisão do grupo: **reunir os dados** e entregar material pronto para que outros integrantes façam código, separação treino/validação/teste e modelagem.

## Arquivos finais do pacote

### 1) `parte1_frases_sintomas_ampliadas_2000.txt`
Arquivo texto com **2.000 frases sintéticas** em linguagem de paciente.
Uso: testar leitura de frases, extração de sintomas e sugestão inicial de diagnóstico.

### 2) `parte1_mapa_pares_sintomas_doencas.csv`
Arquivo principal da **Parte 1**.
Foi o escolhido porque fica **mais próximo do enunciado**, no formato de associação entre sintomas e doença.

Colunas:
- `condicao_id`: identificador interno da condição
- `sintoma_1`: primeiro sintoma/expressão
- `sintoma_2`: segundo sintoma/expressão
- `doenca_associada`: hipótese diagnóstica associada
- `risco_sugerido`: risco sugerido pela combinação
- `fontes_ids`: rastreabilidade das fontes clínicas usadas

### 3) `parte2_base_rotulada_risco_15000.csv`
Arquivo principal da **Parte 2**.
Contém **15.000 frases rotuladas** como `alto_risco` ou `baixo_risco`.

Além da frase e do rótulo, também inclui variáveis estruturadas úteis para análise e auditoria, como:
- dor_toracica
- irradiacao
- dispneia
- sudorese
- nausea
- tontura
- sincope
- palpitacoes
- edema
- ortopneia
- fadiga
- confusao
- hipotensao
- pulso_fraco
- oliguria
- hipertensao
- diabetes
- colesterol_alto
- fumante
- historico_familiar

Essas colunas ajudam o integrante responsável pelo modelo a:
- entender por que a frase foi rotulada;
- analisar padrões clínicos;
- separar treino, validação e teste com mais critério.

## Decisão sobre o arquivo da Parte 1
Entre os dois arquivos antigos da Parte 1, o escolhido para entrega foi:

**`parte1_mapa_pares_sintomas_doencas.csv`**

Motivo:
- combina melhor com o formato pedido no enunciado;
- facilita a explicação na apresentação;
- é mais simples para o colega que vai implementar a lógica;
- ainda mantém rastreabilidade por fonte.

O arquivo `parte1_mapa_conhecimento_expandido.csv` era mais “normalizado” e técnico, mas não é necessário para esta etapa.

## Metodologia resumida
A base foi construída a partir de:
1. sinais e sintomas cardiológicos descritos em fontes clínicas oficiais;
2. regras de combinação entre sintomas, contexto temporal, impacto funcional e fatores de risco;
3. geração de frases sintéticas em português;
4. rotulagem heurística para fins acadêmicos.

## Limitação importante
Esta base é **forte para trabalho acadêmico e prototipagem**, mas **não deve ser apresentada como pronta para uso clínico real** sem validação com dados reais, especialistas e protocolo regulatório.

## Fontes clínicas usadas
- **S01 — American Heart Association**: Warning Signs of a Heart Attack. Uso no projeto: sintomas de infarto/ACS: dor ou desconforto torácico, irradiação, dispneia, suor frio, náusea, tontura. URL: https://www.heart.org/en/health-topics/heart-attack/warning-signs-of-a-heart-attack
- **S02 — American Heart Association**: Heart Failure Signs and Symptoms. Uso no projeto: insuficiência cardíaca: dispneia, fadiga, edema, ortopneia, piora noturna. URL: https://www.heart.org/en/health-topics/heart-failure/warning-signs-of-heart-failure
- **S03 — American Heart Association**: Symptoms, Diagnosis and Monitoring of Arrhythmia. Uso no projeto: arritmias: palpitações, tontura, síncope, fraqueza, dispneia, dor/pressão no peito. URL: https://www.heart.org/en/health-topics/arrhythmia/symptoms-diagnosis--monitoring-of-arrhythmia
- **S04 — American Heart Association**: Aortic Stenosis Overview. Uso no projeto: estenose aórtica: dor torácica, falta de ar, palpitações, tontura/síncope, queda do nível de atividade. URL: https://www.heart.org/en/health-topics/heart-valve-problems-and-disease/heart-valve-problems-and-causes/problem-aortic-valve-stenosis
- **S05 — American Heart Association**: Angina (Chest Pain). Uso no projeto: angina: pressão ou aperto no peito, possível irradiação, dispneia, fadiga. URL: https://www.heart.org/en/health-topics/heart-attack/angina-chest-pain
- **S06 — American Heart Association**: Stable Angina. Uso no projeto: angina estável: dor previsível com esforço ou estresse, melhora com repouso/nitrato. URL: https://www.heart.org/en/health-topics/heart-attack/angina-chest-pain/angina-pectoris-stable-angina
- **S07 — American Heart Association**: Unstable Angina. Uso no projeto: angina instável/alto risco: dor nova, piorando, persistente, inclusive em repouso. URL: https://www.heart.org/en/health-topics/heart-attack/angina-chest-pain/unstable-angina
- **S08 — NHLBI/NIH**: Heart Attack - Symptoms. Uso no projeto: infarto: dor/heaviness no peito, irradiação, dispneia, sudorese, fadiga incomum. URL: https://www.nhlbi.nih.gov/health/heart-attack/symptoms
- **S09 — NHLBI/NIH**: Coronary Heart Disease - Symptoms. Uso no projeto: doença coronariana/angina: sintomas com esforço, sob estresse, melhoram em repouso. URL: https://www.nhlbi.nih.gov/health/coronary-heart-disease/symptoms
- **S10 — NHLBI/NIH**: Arrhythmias - Symptoms. Uso no projeto: arritmias: ansiedade, dor torácica, dificuldade para respirar, tontura, síncope, fraqueza. URL: https://www.nhlbi.nih.gov/health/arrhythmias/symptoms
- **S11 — NHLBI/NIH**: Atrial Fibrillation - Symptoms. Uso no projeto: fibrilação atrial: fadiga, palpitações, falta de ar, dor torácica, tontura/desmaio. URL: https://www.nhlbi.nih.gov/health/atrial-fibrillation/symptoms
- **S12 — NHLBI/NIH**: Heart Valve Diseases - Symptoms. Uso no projeto: doença valvar: dispneia ao esforço, angina, tontura/desmaio, fadiga, batimento irregular. URL: https://www.nhlbi.nih.gov/health/heart-valve-diseases/symptoms
- **S13 — NHLBI/NIH**: Cardiomyopathy - Symptoms. Uso no projeto: cardiomiopatia: dispneia, dor torácica após esforço, fadiga, síncope, palpitações, edema. URL: https://www.nhlbi.nih.gov/health/cardiomyopathy/symptoms
- **S14 — NHLBI/NIH**: Cardiogenic Shock - Symptoms. Uso no projeto: choque cardiogênico: hipotensão, confusão, pulso fraco, pele fria/pegajosa, pouca urina, dispneia intensa. URL: https://www.nhlbi.nih.gov/health/cardiogenic-shock/symptoms
- **S15 — CDC**: About Heart Attack Symptoms, Risk, and Recovery. Uso no projeto: infarto: dor/desconforto torácico, dispneia, dor em mandíbula/pescoço/costas/braço, náusea, tontura, fadiga. URL: https://www.cdc.gov/heart-disease/about/heart-attack.html
- **S16 — CDC**: About Heart Disease. Uso no projeto: resumo de sinais: infarto, arritmia, insuficiência cardíaca. URL: https://www.cdc.gov/heart-disease/about/index.html
- **S17 — UCI Machine Learning Repository**: Heart Disease Dataset. Uso no projeto: variáveis estruturadas clássicas: idade, sexo, tipo de dor torácica, PA, colesterol, glicemia, ECG, FC máxima, angina induzida por exercício, etc.. URL: https://archive.ics.uci.edu/dataset/45/heart+disease
- **S18 — PhysioNet**: PTB-XL. Uso no projeto: grande base pública de ECG com 21.799 exames e 71 declarações eletrocardiográficas. URL: https://physionet.org/content/ptb-xl/1.0.3/
- **S19 — PhysioNet**: MIMIC-IV / MIMIC-IV-ED. Uso no projeto: base hospitalar real desidentificada; mais de 65 mil pacientes de UTI e mais de 200 mil admissões em ED. URL: https://physionet.org/content/mimiciv/
- **S20 — PhysioNet**: MIETIC - MIMIC-IV-Ext Triage Instruction Corpus. Uso no projeto: corpus de triagem com 9.629 casos ESI; acesso restrito/credenciado. URL: https://physionet.org/content/mietic/1.0.0/
- **S21 — FDA**: Clinical Decision Support Software - Guidance. Uso no projeto: referência regulatória para CDS; reforça necessidade de validação, contexto de uso e supervisão clínica. URL: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software

## Bases públicas relevantes para evolução futura
- **UCI Heart Disease** (estruturado tabular): 303 instâncias; 13 atributos principais. Acesso: aberto. Uso recomendado: benchmark inicial para modelos tabulares de risco cardíaco. Referência interna: S17.
- **PTB-XL** (ECG 12 derivações): 21.799 ECGs de 18.869 pacientes. Acesso: aberto. Uso recomendado: classificação de ECG e validação multimodal futura. Referência interna: S18.
- **MIMIC-IV** (prontuário eletrônico hospitalar): mais de 65 mil pacientes de UTI e mais de 200 mil admissões em ED. Acesso: credenciado. Uso recomendado: validação clínica real com sinais vitais, histórico, exames e desfechos. Referência interna: S19.
- **MIMIC-IV-ED** (emergency department): ~425 mil passagens em pronto atendimento. Acesso: credenciado. Uso recomendado: triagem e classificação de prioridade com dados reais. Referência interna: S19.
- **MIETIC** (corpus textual de triagem): 9.629 casos com ESI. Acesso: credenciado. Uso recomendado: futuro fine-tuning de triagem com texto clínico real. Referência interna: S20.
