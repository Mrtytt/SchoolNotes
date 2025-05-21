# Resume Ranker – UML Diyagramları Sunum Notları

## 🎤 Giriş

Herkese merhaba arkadaşlar. Bugün sizlere geliştirmekte olduğumuz **“Resume Ranker”** projesinin yazılım mimarisi kapsamında oluşturduğumuz bir sunum gerçekleştireceğiz.

Kısaca hatırlatmak gerekirse, Resume Ranker, yapay zeka ve doğal dil işleme teknolojileri kullanarak CV’leri iş ilanlarıyla karşılaştıran, adayları objektif şekilde puanlayan ve işe alım sürecini hızlandırmayı hedefleyen bir sistemdir.

---

## 🧩 Use Case Diyagramı

Bu diyagram, sistemimizin dış aktörlerle nasıl etkileşim kurduğunu ve hangi işlevleri sunduğunu görsel olarak modellememizi sağlar.

### Aktörler
- **Aday (Candidate):** Sisteme CV yükleyen, başvuru yapan ve geri bildirim alan kullanıcı.
- **İşveren (Employer):** İş ilanı oluşturan, kriter belirleyen ve aday raporlarını inceleyen aktör.
- **Sistem (Resume Ranker):** CV analizini, uygunluk puanlamasını ve raporlamayı gerçekleştiren AI tabanlı platform.

## 🧱 Class Diyagramı
Bu diyagram, sistemin iç yapısını ve sınıflar arasındaki ilişkileri gösterir.

### Başlıca Sınıflar
- **User:** Tüm kullanıcıların (aday ve işveren) ortak özelliklerini barındırır.
- **Candidate:** User sınıfından türeyen ve yüklediği CV ile profil bilgilerini içeren alt sınıf.
- **Employer:** User sınıfından türeyen, iş ilanı oluşturan ve kriter belirleyen kullanıcı.

### Diğer Sınıflar
- **JobPosting:** İş ilanlarının başlık, açıklama ve kriter bilgilerini tutar.
- **Criteria:** İşverenin belirlediği ölçütleri ve ağırlıklarını içerir.
- **CVFile:** Adayın yüklediği özgeçmiş dosyasını temsil eder.
- **EvaluationEngine:** Yapay zeka motorudur; analiz ve puanlama işlemlerini yapar.

### Sınıflar Arası İlişkiler
- `Candidate` → `CVFile`: Birebir ilişki
- `Employer` → `JobPosting`: Bire-çok ilişki
- `JobPosting` → `Criteria`: Kompozisyon (birlikte var olurlar)
- `EvaluationEngine` → `CVFile`, `JobPosting`, `Criteria`: Bağımlılık ilişkisi

---

## 🔚 Kapanış

Özetle, bu iki diyagram sistemin hem kullanıcı etkileşimlerini hem de iç yapısını detaylı ve anlaşılır bir şekilde modellememizi sağlamıştır. Projemizin ölçeklenebilir, sürdürülebilir ve geliştirilebilir olması için bu diyagramlardan büyük ölçüde yararlanıyoruz.

**Dinlediğiniz için teşekkür ederim. Şimdi sizlere Use-Case'leri detaylıca anlatması için sözü Mehmet arkadaşıma bırakıyorum**
