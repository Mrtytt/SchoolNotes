import pandas as pd
import numpy as np
import random

# Rastgele veri üretmek için sabitler
num_rows = 100000  # 100 bin satır oluştur
platforms = ["ios", "android"]
genders = ["male", "female"]
countries = ["USA", "BRA", "DEU", "FRA", "TUR", "JPN", "IND", "RUS", "ESP", "GBR"]  # 3 harfli ülke kodları

# Rastgele verileri oluştur
data = {
    "id": np.arange(1, num_rows + 1),
    "fiyat": np.random.randint(1, 52, num_rows),
    "platform": [random.choice(platforms) for _ in range(num_rows)],
    "cinsiyet": [random.choice(genders) for _ in range(num_rows)],
    "ülke": [random.choice(countries) for _ in range(num_rows)],
    "yaş": np.random.randint(18, 66, num_rows)  # 18 ile 65 arasında rastgele yaş
}

# DataFrame oluştur
df = pd.DataFrame(data)

# CSV olarak kaydet
df.to_csv("random_data.csv", index=False)

print("100,000 satırlık rastgele veri oluşturuldu ve 'random_data.csv' olarak kaydedildi.")
