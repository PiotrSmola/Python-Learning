import pandas as pd
import datetime
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

# Wczytanie plików z ograniczeniem do 2 milionów rekordów
file_paths = {
    "item_properties_part1": "item_properties_part1.csv",
    "item_properties_part2": "item_properties_part2.csv",
    "events": "events.csv",
    "category_tree": "category_tree.csv",
}

item_properties_part1 = pd.read_csv(file_paths["item_properties_part1"], nrows=2000000)
item_properties_part2 = pd.read_csv(file_paths["item_properties_part2"], nrows=2000000)
events = pd.read_csv(file_paths["events"], nrows=2000000)
category_tree = pd.read_csv(file_paths["category_tree"])  # Ten plik jest mały, dlatego wczytujemy cały

# Konwersja timestampów do formatu datetime dla czytelności
events['timestamp'] = pd.to_datetime(events['timestamp'], unit='ms', origin='unix')
item_properties_part1['timestamp'] = pd.to_datetime(item_properties_part1['timestamp'], unit='ms', origin='unix')
item_properties_part2['timestamp'] = pd.to_datetime(item_properties_part2['timestamp'], unit='ms', origin='unix')

# Łączenie danych z item_properties
item_properties = pd.concat([item_properties_part1, item_properties_part2], ignore_index=True)

# Usunięcie duplikatów z item_properties
item_properties = item_properties.drop_duplicates()

# Kolumna 'value' może zawierać prefiks 'n', różne wartości, czasem wiele liczb.
# Na potrzeby łączenia z category_tree utrzymamy ją jako string.
# Usuwamy jedynie literę 'n', która może występować w wartościach.
item_properties["value"] = item_properties["value"].astype(str)
item_properties["value"] = item_properties["value"].str.replace('n', '', regex=False)

# Łączenie danych z eventami na bazie itemid
merged_data = pd.merge(events, item_properties, on="itemid", how="left")

# Konwersja categoryid w category_tree na string
category_tree["categoryid"] = category_tree["categoryid"].astype(str)

# Łączenie z hierarchią kategorii na bazie kolumny 'value'
# Ponieważ 'value' może reprezentować categoryid, oba pola są teraz stringami
merged_data = pd.merge(
    merged_data,
    category_tree,
    left_on="value",
    right_on="categoryid",
    how="left"
)

# Ograniczenie do 2 mln rekordów po połączeniu
merged_data = merged_data.head(2000000)

# Eksport połączonych danych do pliku CSV
merged_data.to_csv("merged_data.csv", index=False)

# ---- Normalizacja i standaryzacja ----

data = pd.read_csv("merged_data.csv")

# Uzupełnianie braków medianą dla kolumn numerycznych
data.fillna(data.median(numeric_only=True), inplace=True)

# Wybór kolumn numerycznych do skalowania, wykluczając kolumny czasowe i niewłaściwe:
columns_to_exclude = ["timestamp_x", "timestamp_y", "property", "value", "categoryid", "parentid"]
numerical_columns = [col for col in data.select_dtypes(include=["float64", "int64"]).columns if col not in columns_to_exclude]

# Min-Max Scaling
min_max_scaler = MinMaxScaler()
data_min_max_scaled = data.copy()
data_min_max_scaled[numerical_columns] = min_max_scaler.fit_transform(data[numerical_columns])

# Z-Score Standardization
z_score_scaler = StandardScaler()
data_z_score_scaled = data.copy()
data_z_score_scaled[numerical_columns] = z_score_scaler.fit_transform(data[numerical_columns])

# Robust Scaling
robust_scaler = RobustScaler()
data_robust_scaled = data.copy()
data_robust_scaled[numerical_columns] = robust_scaler.fit_transform(data[numerical_columns])

# Eksport wyników ograniczony do 2 mln rekordów
data_min_max_scaled.head(2000000).to_csv("data_min_max_scaled.csv", index=False)
data_z_score_scaled.head(2000000).to_csv("data_z_score_scaled.csv", index=False)
data_robust_scaled.head(2000000).to_csv("data_robust_scaled.csv", index=False)
