import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx

# Görevler ve süreleri (hafta cinsinden)
tasks = {
    "Planlama": 1,
    "Veri İşleme": 3,
    "Model Geliştirme": 5,
    "Uygulama Geliştirme": 6,
    "Test": 3,
    "Sistem Yayına Alma": 1  # Yayına alma kısa bir süreç olarak varsayılmıştır.
}

# Bağımlılıklar (Hangi görevler hangisinden sonra başlar)
dependencies = {
    "Planlama": [],
    "Veri İşleme": ["Planlama"],
    "Model Geliştirme": ["Veri İşleme"],
    "Uygulama Geliştirme": ["Model Geliştirme"],
    "Test": ["Uygulama Geliştirme"],
    "Sistem Yayına Alma": ["Test"]
}

# Ağı oluştur
G = nx.DiGraph()

# Düğümleri ekle (Görevler ve süreleri ile birlikte)
for task, duration in tasks.items():
    G.add_node(task, duration=duration)

# Bağlantıları ekle (Bağımlılıklar)
for task, prereqs in dependencies.items():
    for prereq in prereqs:
        G.add_edge(prereq, task)

# Kritik yolu hesapla
critical_path = nx.algorithms.dag.dag_longest_path(G, weight="duration")
critical_path_duration = sum(tasks[task] for task in critical_path)

# Sonuçları döndür
critical_path, critical_path_duration
# Gantt Chart için görevlerin başlangıç ve bitiş zamanlarını hesapla
start_times = {}
end_times = {}
current_time = 0

for task in critical_path:
    start_times[task] = current_time
    end_times[task] = current_time + tasks[task]
    current_time = end_times[task]

# Gantt Chart verisi oluştur
df = pd.DataFrame({
    "Görev": critical_path,
    "Başlangıç": [start_times[task] for task in critical_path],
    "Bitiş": [end_times[task] for task in critical_path],
    "Süre": [tasks[task] for task in critical_path]
})

# Gantt Chart çiz
fig, ax = plt.subplots(figsize=(10, 5))
for i, row in df.iterrows():
    ax.barh(row["Görev"], row["Süre"], left=row["Başlangıç"], color="skyblue", edgecolor="black")

ax.set_xlabel("Haftalar")
ax.set_ylabel("Görevler")
ax.set_title("Proje Gantt Chart")
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.show()

# PERT Chart çiz
plt.figure(figsize=(10, 5))
pos = nx.spring_layout(G, seed=42)  # Düğümleri düzenle

# Düğümleri ve kenarları çiz
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=10, font_weight="bold")

# Kenarlara süreleri ekle
edge_labels = {(u, v): tasks[v] for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

plt.title("PERT Chart (Görev Bağımlılıkları)")
plt.show()

roles = {
    "Veri Bilimciler": {"sayı": 2, "ücret": 1000},
    "Geliştiriciler": {"sayı": 3, "ücret": 800},
    "Test Mühendisleri": {"sayı": 2, "ücret": 700}
}

total_weeks = critical_path_duration  # 25 hafta
server_and_licenses = 5000  # Sabit maliyet

# Toplam iş gücü maliyetini hesapla
total_labor_cost = sum(role["sayı"] * role["ücret"] * total_weeks for role in roles.values())

# Toplam proje maliyeti
total_cost = total_labor_cost + server_and_licenses
total_cost