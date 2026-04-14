import csv

def processar_diagnostico(caminho_txt, caminho_csv):
    # 1. Carrega o Mapa de Conhecimento
    mapa = []
    
    # CORREÇÃO: 'utf-8-sig' remove caracteres invisíveis no início do arquivo (BOM)
    # e delimiter=',' garante que o Python separe as colunas corretamente.
    with open(caminho_csv, mode='r', encoding='utf-8-sig') as f_csv:
        leitor = csv.DictReader(f_csv, delimiter=',')
        for linha in leitor:
            mapa.append({
                'termos': [linha['sintoma_1'].lower(), linha['sintoma_2'].lower()],
                'doenca': linha['doenca_associada']
            })

    # 2. Processa as frases
    print(f"{'ID':<4} | {'RELATO DO PACIENTE':<60} | {'DIAGNÓSTICO SUGERIDO'}")
    print("-" * 110)

    with open(caminho_txt, mode='r', encoding='utf-8') as f_txt:
        for i, linha in enumerate(f_txt, 1):
            frase = linha.strip().lower()
            if not frase: continue
            
            sugestao = "Análise Inconclusiva"
            
            # Busca por correspondência de termos
            for item in mapa:
                if any(termo in frase for termo in item['termos'] if termo):
                    sugestao = item['doenca']
                    break
            
            # Formata a saída truncando a frase para não quebrar a tabela
            resumo_frase = (frase[:57] + '..') if len(frase) > 57 else frase
            print(f"{i:02d}   | {resumo_frase:<60} | {sugestao}")

if __name__ == "__main__":
    MAPA_CSV = 'fase2/dados/mapa_pares_sintomas_doencas.csv'
    FRASES_TXT = 'fase2/dados/frases_sintomas_2000.txt'
    
    processar_diagnostico(FRASES_TXT, MAPA_CSV)