import subprocess
import os

# Define o caminho para a pasta que você deseja abrir
caminho_pasta = "/home/gabriel/Documentos/Portifolio_Gabriel-br2/Matrix Generator/saved_anim"

# Abre o gerenciador de arquivos para exibir a pasta especificada
if os.name == 'nt':  # para o sistema operacional Windows
    subprocess.Popen(['explorer', caminho_pasta])
else:  # para o sistema operacional macOS ou Linux
    subprocess.Popen(['open', caminho_pasta])