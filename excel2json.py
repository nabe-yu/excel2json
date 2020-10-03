import pandas as pd

out_path = 'profile.json'

df = pd.read_excel('src_profile.xlsx', sheet_name=0)  # sheet_nameはシート名を文字列あるいはn枚目の整数で指定する
with open(out_path, 'w', encoding='utf-8') as file:
    # 文字のエスケープを無効にする
    df.to_json(file, orient='records', force_ascii=False)