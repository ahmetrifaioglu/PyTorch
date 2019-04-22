import pandas as pd

df_sonuc = pd.read_csv("/Users/trman/Desktop/round_2_template_submitted.csv")
#print(df_sonuc.columns)
df_predictions = pd.read_csv("/Users/trman/Desktop/round2_preds.txt")
#print(df_predictions)
columns = list(df_sonuc.columns)
columns.append("pKd_[M]_pred")

print(",".join(columns))
for ind, row in df_sonuc.iterrows():
    comp_name, uni_id = row["Compound_Name"], row["UniProt_Id"]
    for ind2, row2 in df_predictions.iterrows():
        if row2["Comp_ID"]==comp_name and row2["Tar_ID"]==uni_id:
            final_list = list(row)
            final_list.append(row2["Prediction"])
            final_list = [str(item) for item in final_list]
            print(",".join(final_list))
            break