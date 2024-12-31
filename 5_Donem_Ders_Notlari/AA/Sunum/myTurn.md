# Dijkstra Algoritması ve En Kısa Yol Hesaplama Fonksiyonları

## Dijkstra Algoritması Hakkında
Dijkstra algoritması, bir graf üzerindeki düğümler arasında en kısa yolları hesaplamak için kullanılan bir algoritmadır. Ağırlıklı graflar üzerinde çalışan bu algoritma, özellikle yönlendirilmiş ve pozitif ağırlıklara sahip grafiklerde oldukça etkilidir. 

## 1. Dijkstra Fonksiyonu
### Amaç:
Bu fonksiyon, bir graf üzerindeki tüm düğümlere olan en kısa yolları ve ilgili ebeveyn bilgilerini hesaplar.

### Kod:
```python
def dijkstra(self, start_vertex):
    vertices = list(self.G.nodes())

    visited = set()
    parents = {}
    adj = {v: [] for v in vertices}
    exist = {v: 0 for v in vertices}
    D = {v: float('inf') for v in vertices}

    parents[start_vertex] = start_vertex
    D[start_vertex] = 0
    exist[start_vertex] = 1
    pq = [(0, start_vertex)]

    while pq:
        current_cost, current_vertex = heapq.heappop(pq)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        current_neighbors = list(self.G[current_vertex])
        for neighbor in current_neighbors:
            old_cost = D[neighbor]
            new_cost = D[current_vertex] + self.times_all[current_vertex][neighbor]
            if new_cost < old_cost:
                parents[neighbor] = current_vertex
                exist[neighbor] = exist[current_vertex]
                if neighbor not in adj[current_vertex]:
                    adj[current_vertex].append(neighbor)
                D[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    self.shortest_adj[start_vertex] = adj
    self.shortest_cnt[start_vertex] = exist
    return D, parents
```

### Adımlar:
1. **Graf Bilgilerinin Hazırlanması:**
   - `vertices`: Grafın tüm düğümlerini alır.
   - `visited`: Ziyaret edilen düğümlerin kaydı tutulur.
   - `parents`: Her düğüm için bir önceki düğüm bilgisi saklanır.
   - `D`: Başlangıç düğümünden diğer düğümlere olan mesafeleri temsil eder.

2. **Başlangıç Değerleri Ayarlama:**
   - Başlangıç düğümü için maliyet `0` olarak ayarlanır.
   - Öncelikli kuyruk (priority queue) başlatılır.

3. **Ana Döngü:**
   - Kuyruktaki en düşük maliyetli düğüm işlenmek üzere çıkarılır.
   - Düğümün komşuları kontrol edilir ve daha düşük maliyetli yollar bulunursa bu bilgiler güncellenir.

4. **Sonuç:**
   - En kısa mesafeler `D` ve ebeveyn bilgileri `parents` olarak döndürülür.

---

## 2. get_shortest_path_dijkstra Fonksiyonu
### Amaç:
Bu fonksiyon, bir graf üzerinde iki düğüm arasındaki en kısa yolu ve toplam maliyetini bulur.

### Kod:
```python
def get_shortest_path_dijkstra(self, start_stop, end_stop):
    shortest_time, parents = self.dijkstra(start_stop)
    path = self.get_path(end_stop, parents)
    if not path:
        print(f'No path found from {start_stop} to {end_stop}!')
        return 0, path
    # print(shortest_time[end_stop], path)
    return shortest_time[end_stop], path
```

### Adımlar:
1. **Dijkstra Fonksiyonunu Çağırma:**
   - `self.dijkstra(start_stop)`, başlangıç düğümünden diğer düğümlere olan en kısa mesafeleri ve ebeveyn bilgilerini hesaplar.

2. **Yolun Belirlenmesi:**
   - `self.get_path(end_stop, parents)`, ebeveyn bilgilerini kullanarak başlangıçtan bitişe giden yolu oluşturur.

3. **Yol Kontrolü:**
   - Eğer bir yol bulunamazsa, uygun bir mesaj yazdırılır ve toplam maliyet `0` olarak döndürülür.

4. **Sonuç:**
   - Toplam maliyet ve izlenecek yol döndürülür.

---

## Genel Kullanım Alanları:
- Bu fonksiyonlar, bir graf üzerindeki rotaları analiz etmek ve belirli düğümler arasındaki en kısa yolu bulmak için kullanılır.
- **Uygulama Alanları:** Harita uygulamaları, ağ analizleri, lojistik planlamaları, trafik yönetimi ve rota optimizasyonudur.

---

## Notlar:
- Kod yapısı Python programlama diline özgüdür ve `heapq` modülü kullanılarak öncelikli kuyruk işlemleri gerçekleştirilmiştir.
- Gerçek hayatta kullanılacak grafik verileri, ağırlık bilgileriyle birlikte doğru bir şekilde modele entegre edilmelidir.

