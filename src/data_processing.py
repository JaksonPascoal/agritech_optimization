import pandas as pd

def load_and_clean_data(file_path):
    """
    Carrega o dataset e realiza a limpeza inicial.

    Args:
        file_path (str): O caminho para o arquivo CSV.

    Returns:
        pd.DataFrame: O DataFrame limpo e pronto para análise.
    """
    df = pd.read_csv(file_path)

    # Converte a coluna 'Data' para o formato datetime
    df['Data'] = pd.to_datetime(df['Data'])

    return df



if __name__ == "__main__":
    
    data_path = 'data/dataset_simulado.csv'    
    df_clean = load_and_clean_data(data_path)
    
    print("DataFrame processado com sucesso!")
    print("\nInformações sobre o DataFrame (após processamento):")
    df_clean.info()