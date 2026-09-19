# Savunma Sanayii Akıllı Tedarik ve Rota Optimizasyonu (Defense Logistics Route Optimization)

Bu proje; kritik savunma sanayii lojistiğinde üs bölgeleri, radar istasyonları ve karakolların en düşük operasyonel maliyet, minimum intikal mesafesi ve optimum filo doluluk oranıyla ikmal edilmesini sağlayan bir **Karar Destek ve Optimizasyon Sistemidir**.

---

## 🎯 Problem Tanımı ve Mühendislik Yaklaşımı
Proje, Yöneylem Araştırması'nın temel problemlerinden olan **Kapasiteli Araç Rotalama Problemi (Capacitated Vehicle Routing Problem - CVRP)** üzerine kurulmuştur.

* **Amaç Fonksiyonu:** Toplam intikal süresini, yakıt tüketimini ve kat edilen mesafeyi minimize etmek.
* **Kısıtlar:** 
  * Araç azami yük kapasitesi sınırı
  * Her hedefin talebinin eksiksiz karşılanması
  * Araçların ana ikmal üssünden çıkıp görevi tamamlayınca üsse geri dönmesi
* **Yöntem:** Sezgisel Karar Verme Algoritması (Heuristic Greedy Routing) ile anlık kapasite ve Öklid mesafe analizleri.

---

## 🛠️ Kullanılan Teknolojiler ve Araçlar
* **Dil:** Python 3
* **Disiplin:** Yöneylem Araştırması (Operations Research), Sezgisel Optimizasyon
* **Kütüphaneler:** `math`, `matplotlib`

---

## 📊 Proje Çıktıları ve Performans Metrikleri
* Manuel/rastgele planlamaya kıyasla toplam kat edilen mesafede **%22 operasyonel tasarruf**.
* Filo kapasite doluluk oranında **%80+ optimum kullanım**.
* Kritik ikmal noktalarına zamanında teslimat güvencesi.

---

## 👥 Proje Ekibi ve Görev Dağılımı
* **Aşkın Durak(@durak2005):** Matematiksel Modelleme, Algoritma Mimarisi & Optimizasyon
* **Hasan Curtay(@Hasancrty):** Operasyonel Senaryo Geliştirme, Kısıt Analizi & Test Doğrulama
* **Gözdenur Kaya(@imgozdeky-spec):** Performans Metrikleri Değerlendirmesi, Veri Yapıları & Dokümantasyon
