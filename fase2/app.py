"""
CardioIA – Interface de Análise de Risco Cardiológico
Combina análise por regras clínicas com modelo de Machine Learning (TF-IDF + Regressão Logística).

Uso: streamlit run fase2/app.py
"""

import csv
from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# ── Configuração da página (deve ser a primeira chamada Streamlit) ──────────
st.set_page_config(
    page_title="CardioIA – Análise de Risco",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Caminhos ────────────────────────────────────────────────────────────────
DADOS_DIR = Path(__file__).parent / "dados"
CSV_MAPA  = DADOS_DIR / "mapa_pares_sintomas_doencas.csv"
CSV_BASE  = DADOS_DIR / "base_rotulada_risco_15000.csv"

# ── CSS – tema escuro, cards gradiente, badges ───────────────────────────────
CSS = """
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #0e1117;
    color: #e0e0e0;
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] {
    background-color: #161b27;
    border-right: 1px solid #2a2f3d;
}

/* Banner de emergência */
.emergency-banner {
    background: linear-gradient(135deg, #7f0000 0%, #c0392b 100%);
    border-left: 5px solid #ff1744;
    border-radius: 10px;
    padding: 14px 20px;
    margin-bottom: 20px;
    font-weight: 600;
    font-size: 0.95rem;
    color: #fff;
    letter-spacing: 0.02em;
}

/* Cards de resultado */
.card {
    border-radius: 14px;
    padding: 22px 26px;
    height: 100%;
    box-sizing: border-box;
}
.card-alto  { background: linear-gradient(135deg, #3d0000 0%, #1a0a0a 100%); border: 1px solid #c0392b; }
.card-baixo { background: linear-gradient(135deg, #003d1a 0%, #0a1a0f 100%); border: 1px solid #27ae60; }
.card-neutro{ background: linear-gradient(135deg, #1a2035 0%, #0e1117 100%); border: 1px solid #3d4a6b; }

.card h3 {
    margin: 0 0 6px 0;
    font-size: 0.82rem;
    color: #8892b0;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}
.result-label {
    font-size: 1.55rem;
    font-weight: 700;
    margin: 6px 0 14px 0;
    line-height: 1.2;
}
.label-alto   { color: #ff6b6b; }
.label-baixo  { color: #55efc4; }
.label-neutro { color: #74b9ff; }

/* Badge/pill */
.badge {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    margin-left: 8px;
    vertical-align: middle;
    position: relative;
    top: -3px;
}
.badge-alto  { background: #c0392b; color: #fff; }
.badge-baixo { background: #27ae60; color: #fff; }
.badge-ml    { background: #2d3561; color: #74b9ff; border: 1px solid #74b9ff55; }
.badge-regra { background: #2d4531; color: #55efc4; border: 1px solid #55efc455; }

/* Barra de probabilidade */
.prob-wrap {
    background: #1e2533;
    border-radius: 999px;
    height: 16px;
    overflow: hidden;
    margin: 6px 0 8px 0;
}
.bar-alto  { height: 100%; border-radius: 999px; background: linear-gradient(90deg, #c0392b, #ff6b6b); }
.bar-baixo { height: 100%; border-radius: 999px; background: linear-gradient(90deg, #27ae60, #55efc4); }
.prob-text { font-size: 0.85rem; color: #a0a8bb; margin-bottom: 2px; }

/* Inconclusivo */
.inconclusivo {
    font-style: italic;
    color: #74b9ff;
    font-size: 1.1rem;
    margin: 6px 0 10px 0;
}
.sub-text { color: #6b7280; font-size: 0.85rem; margin-top: 8px; }

/* Separador de seção */
.section-title {
    font-size: 0.85rem;
    font-weight: 700;
    color: #8892b0;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin: 24px 0 10px 0;
    border-bottom: 1px solid #2a2f3d;
    padding-bottom: 5px;
}

/* Rodapé disclaimer */
.disclaimer {
    margin-top: 44px;
    padding: 16px 20px;
    background: #161b27;
    border-radius: 10px;
    border: 1px solid #2a2f3d;
    font-size: 0.80rem;
    color: #6b7280;
    line-height: 1.7;
}
</style>
"""

# ── Dados e modelo em cache ──────────────────────────────────────────────────

@st.cache_resource(show_spinner="Carregando mapa de conhecimento clínico…")
def carregar_mapa_regras():
    mapa = []
    with open(CSV_MAPA, mode="r", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f, delimiter=","):
            mapa.append({
                "termos": [row["sintoma_1"].lower(), row["sintoma_2"].lower()],
                "doenca": row["doenca_associada"],
                "risco":  row["risco_sugerido"],
            })
    return mapa


@st.cache_resource(show_spinner="Treinando modelo de IA (TF-IDF + Regressão Logística)…")
def treinar_modelo():
    df = pd.read_csv(CSV_BASE, usecols=["frase", "situacao"])

    # Divide os textos brutos ANTES de vetorizar (evita data leakage)
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        df["frase"], df["situacao"], test_size=0.20, random_state=42, stratify=df["situacao"]
    )

    # TF-IDF ajustado APENAS no treino — mesmo parâmetro do classificador_risco.ipynb
    tfidf = TfidfVectorizer(
        max_features=500,
        stop_words=None,
        lowercase=True,
    )
    X_train = tfidf.fit_transform(X_train_raw)
    X_test  = tfidf.transform(X_test_raw)

    modelo = LogisticRegression(
        max_iter=1000, random_state=42, class_weight="balanced", C=1.5
    )
    modelo.fit(X_train, y_train)
    acuracia = modelo.score(X_test, y_test)
    return tfidf, modelo, acuracia


# ── Funções de análise ────────────────────────────────────────────────────────

def analisar_regras(texto: str, mapa: list) -> dict:
    texto_lower = texto.lower()
    for item in mapa:
        if any(termo in texto_lower for termo in item["termos"] if termo):
            return {"doenca": item["doenca"], "risco": item["risco"], "inconclusivo": False}
    return {"doenca": "Análise Inconclusiva", "risco": None, "inconclusivo": True}


def analisar_ml(texto: str, tfidf, modelo) -> dict:
    vetor = tfidf.transform([texto])
    predicao = modelo.predict(vetor)[0]
    proba    = modelo.predict_proba(vetor)[0]
    idx_alto = list(modelo.classes_).index("alto_risco")
    return {"predicao": predicao, "prob_alto": float(proba[idx_alto])}


# ── Componentes de UI ─────────────────────────────────────────────────────────

def render_card_ml(res: dict):
    is_alto     = res["predicao"] == "alto_risco"
    card_cls    = "card-alto"  if is_alto else "card-baixo"
    label_cls   = "label-alto" if is_alto else "label-baixo"
    badge_risco = "badge-alto" if is_alto else "badge-baixo"
    label_txt   = "ALTO RISCO" if is_alto else "BAIXO RISCO"
    bar_cls     = "bar-alto"   if is_alto else "bar-baixo"
    pct         = int(res["prob_alto"] * 100)

    st.markdown(
        f'<div class="card {card_cls}">'
        f'  <h3>Modelo de Machine Learning <span class="badge badge-ml">IA</span></h3>'
        f'  <div class="result-label {label_cls}">'
        f'    {label_txt} <span class="badge {badge_risco}">{pct}%</span>'
        f'  </div>'
        f'  <p class="prob-text">Probabilidade de alto risco</p>'
        f'  <div class="prob-wrap"><div class="{bar_cls}" style="width:{pct}%"></div></div>'
        f'  <p class="sub-text">TF-IDF + Regressão Logística · 15.000 frases de treino</p>'
        f'</div>',
        unsafe_allow_html=True,
    )


def render_card_regra(res: dict):
    if res["inconclusivo"]:
        st.markdown(
            '<div class="card card-neutro">'
            '  <h3>Análise por Regras Clínicas <span class="badge badge-regra">REGRAS</span></h3>'
            '  <div class="inconclusivo">⚠️ Análise Inconclusiva</div>'
            '  <p class="sub-text">Nenhum sintoma mapeado foi identificado no texto. '
            '  Tente descrever com mais detalhes.</p>'
            '</div>',
            unsafe_allow_html=True,
        )
    else:
        is_alto   = res["risco"] == "alto_risco"
        card_cls  = "card-alto"  if is_alto else "card-baixo"
        label_cls = "label-alto" if is_alto else "label-baixo"
        badge_cls = "badge-alto" if is_alto else "badge-baixo"
        badge_txt = "ALTO RISCO" if is_alto else "BAIXO RISCO"

        st.markdown(
            f'<div class="card {card_cls}">'
            f'  <h3>Análise por Regras Clínicas <span class="badge badge-regra">REGRAS</span></h3>'
            f'  <div class="result-label {label_cls}">{res["doenca"]}</div>'
            f'  <span class="badge {badge_cls}">{badge_txt}</span>'
            f'  <p class="sub-text" style="margin-top:14px">'
            f'  Mapa de 1.168 pares sintoma–doença · 8 condições cardiológicas</p>'
            f'</div>',
            unsafe_allow_html=True,
        )


def render_sidebar(acuracia: float):
    with st.sidebar:
        st.markdown("# 🫀 CardioIA")
        st.markdown("**Assistente Acadêmico de Triagem Cardiológica**")
        st.divider()

        st.markdown("### Como usar")
        st.markdown(
            "1. Descreva os sintomas do paciente em linguagem natural\n"
            "2. Clique em **Analisar**\n"
            "3. Veja os resultados de dois métodos independentes\n"
            "4. Use o consenso como orientação"
        )
        st.divider()

        st.markdown("### Métricas do Modelo")
        st.metric("Acurácia (conjunto de teste)", f"{acuracia:.2%}")
        st.caption("Treino: 12.000 frases · Teste: 3.000 frases")
        st.divider()

        st.markdown("### Condições Monitoradas")
        for c in [
            "Síndrome Coronariana Aguda / Infarto",
            "Insuficiência Cardíaca",
            "Arritmia / Fibrilação Atrial",
            "Angina Estável / Doença Coronariana",
            "Cardiomiopatia",
            "Choque Cardiogênico",
            "Doença Valvar / Estenose Aórtica",
            "Bradiarritmia / Bloqueio de Condução",
        ]:
            st.markdown(f"• {c}")

        st.divider()
        st.markdown("### Tecnologias")
        st.markdown(
            "- Python 3 + Streamlit\n"
            "- Scikit-learn (TF-IDF + LR)\n"
            "- Pandas\n"
            "- Dataset: 15.000 frases sintéticas"
        )
        st.caption("CardioIA v1.0 · Projeto Acadêmico · Fase 2")


# ── App principal ─────────────────────────────────────────────────────────────

def main():
    st.markdown(CSS, unsafe_allow_html=True)

    mapa   = carregar_mapa_regras()
    tfidf, modelo, acuracia = treinar_modelo()

    render_sidebar(acuracia)

    # Cabeçalho
    st.markdown("# 🫀 CardioIA — Análise de Risco Cardiológico")
    st.markdown(
        "Descreva os sintomas em linguagem natural. O sistema aplicará **dois métodos independentes** "
        "para estimar o nível de risco cardiológico: análise por regras clínicas e um modelo de IA."
    )

    # Banner de emergência
    st.markdown(
        '<div class="emergency-banner">'
        "🚨 EMERGÊNCIA: Dor no peito intensa, falta de ar súbita ou desmaio? "
        "Ligue imediatamente para o SAMU <strong>192</strong> ou vá ao pronto-socorro. "
        "Este sistema é <strong>exclusivamente educacional</strong> e não substitui atendimento médico."
        "</div>",
        unsafe_allow_html=True,
    )

    # Área de entrada
    st.markdown('<div class="section-title">Relato de Sintomas</div>', unsafe_allow_html=True)

    texto_input = st.text_area(
        label="sintomas",
        label_visibility="collapsed",
        placeholder=(
            "Exemplo: Paciente masculino de 58 anos com dor no peito que irradia para o braço esquerdo, "
            "falta de ar, suor frio e tontura há 2 horas..."
        ),
        height=140,
    )

    analisar_btn = st.button("🔍  Analisar Sintomas", type="primary", use_container_width=True)

    # Resultados
    if analisar_btn:
        texto = texto_input.strip()

        if not texto:
            st.warning("Descreva os sintomas antes de analisar.")
            st.stop()
        if len(texto) < 10:
            st.warning("Relato muito curto. Forneça mais detalhes para uma análise precisa.")
            st.stop()

        st.markdown('<div class="section-title">Resultados da Análise</div>', unsafe_allow_html=True)

        with st.spinner("Analisando…"):
            res_ml    = analisar_ml(texto, tfidf, modelo)
            res_regra = analisar_regras(texto, mapa)

        col_ml, col_regra = st.columns(2, gap="large")
        with col_ml:
            render_card_ml(res_ml)
        with col_regra:
            render_card_regra(res_regra)

        # Consenso
        ml_alto    = res_ml["predicao"] == "alto_risco"
        regra_alto = (not res_regra["inconclusivo"]) and res_regra["risco"] == "alto_risco"

        st.markdown("")
        if ml_alto and regra_alto:
            st.error(
                "⚠️ **Consenso: ALTO RISCO** — Ambos os métodos identificaram indicadores graves. "
                "Recomenda-se avaliação médica **urgente**."
            )
        elif ml_alto or regra_alto:
            st.warning(
                "⚡ **Atenção** — Um dos métodos identificou indicadores de risco elevado. "
                "Considere consultar um médico para avaliação."
            )
        elif not res_regra["inconclusivo"]:
            st.success(
                "✅ **Consenso: BAIXO RISCO** — Ambos os métodos indicam baixo risco imediato. "
                "Continue o monitoramento clínico regular."
            )
        else:
            st.info(
                "ℹ️ O modelo de IA classificou o texto. A análise por regras não encontrou "
                "correspondência direta — tente descrever os sintomas com outras palavras."
            )

    # Rodapé
    st.markdown(
        '<div class="disclaimer">'
        "<strong>⚕️ Aviso Legal e Acadêmico:</strong> Este sistema é um protótipo desenvolvido "
        "exclusivamente para fins educacionais como parte do projeto CardioIA (Fase 2). "
        "Os resultados são baseados em dados sintéticos e regras heurísticas, sem validação clínica. "
        "<strong>Nunca use este sistema como substituto de diagnóstico médico profissional.</strong> "
        "Em situações de emergência: SAMU 192 · Bombeiros 193 · UPA mais próxima."
        "</div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
