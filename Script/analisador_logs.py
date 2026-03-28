import re
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple

def gerar_log_de_exemplo(caminho_arquivo: Path) -> None:
    """Gera um arquivo de log fictício para teste."""
    linhas_log = [
        "[2023-10-25 10:00:01] [INFO] Sistema iniciado com sucesso.\n",
        "[2023-10-25 10:05:12] [WARNING] Uso de memória acima de 70%.\n",
        "[2023-10-25 10:15:30] [INFO] Usuário 'admin' fez login.\n",
        "[2023-10-25 10:20:45] [ERROR] Falha na conexão com o banco de dados!\n",
        "[2023-10-25 10:21:00] [INFO] Tentando reconectar...\n",
        "[2023-10-25 10:21:05] [ERROR] Timeout ao aguardar resposta da API.\n",
        "[2023-10-25 10:30:00] [INFO] Backup diário concluído.\n",
    ]
    # Criando um arquivo
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(linhas_log)
        print(f"Arquivo de log '{caminho_arquivo.name}' gerado para teste.")
    
def analisar_log(caminho_arquivo: Path) -> Tuple[Dict[str, int], List[str]]:
    """Lê o arquivo de log, conta os níveis de severidade e extrai os erros"""
    padrao_nivel = re.compile(r"\[INFO|WARNING|ERROR|DEBUG\]")
    contagem_niveis = Counter()
    linhas_com_erro = []

    try:
        # Lendo o arquivo linha por linha
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                match = padrao_nivel.search(linha)
                if match:
                    nivel = match.group(1)
                    contagem_niveis[nivel] += 1

                    if nivel == "ERROR":
                        linhas_com_erro.append[linha.strip()]

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Erro de I/O ao ler o arquivo: {e}", file=sys.stderr)

    return dict(contagem_niveis), linhas_com_erro

def gerar_relatorio(caminho_saida: Path, contagem: Dict[str, int], erros: List[str]) -> None:
    """Escreve o relatório final em um arquivo de texto."""
    try:
        """Escrevendo o relatório final."""
        with open(caminho_saida, 'w', encoding='utf-8') as arquivo:
            arquivo.write("=== RELATÓRIO DE ANÁLISE DE LOGS ===")
            arquivo.write("Resumo de eventos:\n")
            for nivel, total in sorted(contagem.items()):
                arquivo.write(f" - {nivel}: {total} ocorrência(s)\n")

            arquivo.write("\n=== LINHAS DE ERROS ENCONTRADAS ===\n")
            if erros:
                for erro in erros:
                    arquivo.write(f"{erro}\n")
            else:
                arquivo.write("Nenhum erro foi encontrado no log.\n")
        print(f"Sucesso! Relatório salvo em: '{caminho_saida.name}'.")

    except IOError as e:
        print(f"Erro ao salvar o relatório: {e}", file=sys.stderr)

def main():
    # Definindo os caminhos com PathLib
    diretorio_atual = Path(__file__).parent
    arquivo_log = diretorio_atual / "sistema.log"
    arquivo_relatorio = diretorio_atual / "relatorio_erros.txt"

    # Gerar Log de Teste
    gerar_log_de_exemplo(arquivo_log)

    # Analisar o arquivo
    print("Analisando o arquivo de log ...")
    contagem, erros = analisar_log(arquivo_log)

if __name__ == "__main__":
    main()