# **Graf İşleme ve Kısayol Hesaplama Algoritması**

## 1. Ön İşleme Fonksiyonu: `preprocess`

Fonksiyonun amacı, bir grafın düğümleri arasındaki kısayolları önceden hesaplayarak daha hızlı yol sorgulama yapılmasını sağlamaktır.

```python
def preprocess(self):
    node_pq = self.get_node_order_edge_difference()
    order = 0

    while node_pq:
        _, v = heapq.heappop(node_pq)

        new_dif = self.edge_difference(v)
        if node_pq and new_dif > node_pq[0][0]:
            heapq.heappush(node_pq, (new_dif, v))
            continue

        order += 1
        if order % 500 == 0:
            print(f"..........Contracting {order}/4397 nodes..........")

        self.order_of[v] = order
        self.node_order[order] = v

        for u in list(self.G.predecessors(v)):
            if u in self.order_of:
                continue

            P = {}
            for w in list(self.G.neighbors(v)):
                if w in self.order_of:
                    continue
                P[w] = self.times_all[u][v] + self.times_all[v][w]

            if not P:
                continue

            P_max = max(P.values())
            D = self.local_dijkstra_without_v(u, v, P_max)

            for w in list(self.G.neighbors(v)):
                if w in self.order_of:
                    continue

                if D[w] > P[w]:
                    if self.G.has_edge(u, w):
                        self.G.get_edge_data(u, w)[0]['shortcut_node'] = v
                    else:
                        self.G.add_edge(u, w, shortcut_node=v)
                        self.times_all[u][w] = P[w]

    print('Preprocess Done!')
```

### Detaylı Açıklama:
1. **Düğüm Öncelik Sırası (`node_pq`)**:
   - Bu yapı, düğümlerin işlenme sırasını belirlemek için bir öncelik sırasıdır.
   - `get_node_order_edge_difference` fonksiyonu, her düğümün bağlantı farkını hesaplar.

2. **Düğüm İşleme**:
   - Her düğüm için `heapq` kullanılarak işlem yapılır.
   - Eğer düğümün bağlantı farkı değişmişse, düğüm yeniden sıraya eklenir.

3. **Kısayol Hesaplama**:
   - Bir düğüm işlenirken, tüm komşuları arasındaki en kısa yollar hesaplanır.
   - Komşular arasındaki kısayollar güncellenir veya yeni kenarlar eklenir.

4. **Çıktılar**:
   - Her 500 düğümde bir ilerleme durumu kullanıcıya yazdırılır.
   - İşlem tamamlandığında "Preprocess Done!" mesajı verilir.

---

## 2. En Kısa Yol Hesaplama Fonksiyonu: `get_shortest_path_CH`

Bu fonksiyon, ön işleme tamamlandıktan sonra iki düğüm arasındaki en kısa yolu hesaplamak için kullanılır.

```python
def get_shortest_path_CH(self, source_node, target_node):
    t1 = time.time()
    self.preprocess()
    t2 = time.time()
    print("Preprocessing time:", t2 - t1)

    t, p = self.bidirectional_dijkstra(source_node, target_node)
    t3 = time.time()
    print('Query time: ', t3 - t2)

    if not p:
        print(f'No path found from {source_node} to {target_node}!')
        return 0, p

    print(t, p)
    return t, p
```

### Detaylı Açıklama:
1. **Zaman Ölçümleri**:
   - İlk olarak ön işleme (`preprocess`) süresi ölçülür.
   - Daha sonra sorgu süresi hesaplanır.

2. **İki Yönlü Dijkstra Algoritması**:
   - Hem başlangıç hem de hedef düğümden algoritma çalıştırılarak süre kısaltılır.

3. **Hata Durumu**:
   - Eğer hedef düğüme ulaşılamazsa, kullanıcıya "No path found" mesajı verilir.

4. **Çıktılar**:
   - En kısa yolun süresi ve rota üzerindeki düğümler döndürülür.


