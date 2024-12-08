import pandas as pd
import re
from Narrateur import Narrateur, load_narrateurs
import arabic_reshaper
from bidi.algorithm import get_display

file_path1 = 'annexe2_2hadith2.xlsx'
file_path2 = 'anexe2_1_hadith1.xlsx'

df_narrators = pd.read_excel(file_path1)
df_chains = pd.read_excel(file_path2, header=None, usecols=[0])

narrators = load_narrateurs(file_path1)
print("Narrator Dictionary: ", narrators)

def prepare_chains(df):
    chains = {}
    current_chain = []
    current_key = 1

    for _, row in df.iterrows():
        text = row[0]

        if isinstance(text, str):
            if "سلسلة رواة الحديث عدد" in text:
                if current_chain:
                    chains[current_key] = current_chain
                    current_chain = []
                    current_key += 1
            else:
                cleaned_text = re.sub(r'^\d+\.\s*', '', text.strip()) 
                current_chain.append(cleaned_text)

    if current_chain:
        chains[current_key] = current_chain

    for key, value in chains.items():
        chains[key] = [narrator.replace('\xa0', ' ').strip() for narrator in value]

    return chains


chains = prepare_chains(df_chains)
print("\nHadith Chains: ", chains)

