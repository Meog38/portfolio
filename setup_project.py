import os
import shutil
import sys

def create_directory_structure():
    # Criar diretórios necessários
    directories = [
        'portfolio',
        'portfolio/core',
        'portfolio/portfolio',
        'portfolio/templates',
        'portfolio/templates/core',
        'portfolio/static',
        'portfolio/static/css',
        'portfolio/static/js',
        'portfolio/static/images',
        'portfolio/media',
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Diretório criado: {directory}")

def main():
    create_directory_structure()
    print("\nEstrutura de diretórios criada com sucesso!")
    print("\nAgora você pode copiar os arquivos do código para os diretórios correspondentes.")
    print("Exemplo: core/models.py deve ser copiado para portfolio/core/models.py")

if __name__ == "__main__":
    main()