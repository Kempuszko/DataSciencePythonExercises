import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def basic_report(df: pd.DataFrame, target: str = 'churned') -> dict:
    return {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': int(df.isna().sum().sum()),
        'target_distribution': df[target].value_counts().to_dict() if target in df.columns else {}
    }


if __name__ == '__main__':
    # Dane lokalne z repo kursu (nie wymagają internetu). Uruchom z folderu ai_workshop:
    #   python analyze_heart_data.py
    data = load_data('../../../data/churn.csv')
    print(basic_report(data))
