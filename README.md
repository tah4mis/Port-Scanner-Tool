# Port Scanner Tool

**Port Scanner Tool**, Python ile yazılmış gelişmiş bir TCP/UDP port tarayıcı ve servis tespit aracıdır.  
Bu proje **eğitim ve siber güvenlik öğrenimi amacıyla geliştirilmiş**, tamamen güvenli ve izinsiz kullanım dışı bir araçtır.

---

## 🚀 Özellikler

- **TCP ve UDP Port Tarama**: Ağınızdaki cihazların hangi portlarının açık olduğunu hızlıca tespit edin.  
- **Banner Grabbing**: Açık TCP portlarda servis ve sürüm bilgisi toplar.  
- **Renkli Terminal Çıktısı**: Açık portlar yeşil, kapalı portlar kırmızı olarak gösterilir.  
- **Kapalı Port Özetleme**: Terminalde gereksiz bilgi yerine kapalı portların toplam sayısı özetlenir.  
- **CSV Kaydı**: Tarama sonuçlarını detaylı şekilde `tarama_sonucu.csv` dosyasına kaydeder.  
- **Port Listesi Seçenekleri**: Common ports veya tüm port aralığı (1-1024) taraması yapabilirsiniz.  
- **Multithreading Desteği**: Hızlı ve verimli tarama için birden fazla thread kullanılabilir.

---

## ⚙️ Kullanım

1. Python 3 yüklü olmalıdır.  
2. Terminalden aşağıdaki komutla çalıştırın:

```bash
python port_scanner.py
Hedef IP/domain, port listesi ve tarama protokolünü seçin.

Tarama tamamlandığında açık portlar terminalde görüntülenir ve tüm sonuçlar CSV dosyasına kaydedilir.

🛡️ Lisans
Bu proje GNU General Public License v3 (GPLv3) ile lisanslanmıştır.
Kodunuzu alabilir, geliştirebilir ve dağıtabilirsiniz, ancak GPLv3 şartlarına uymanız gerekir.
Detaylar için LICENSE dosyasına bakın.

⚠️ Uyarı / Disclaimer
Bu araç yalnızca eğitim ve test amaçlıdır.

Başka kişilerin sistemlerine izinsiz erişim yapmak yasa dışıdır ve ciddi hukuki sonuçlar doğurabilir.

Bu proje ile oluşabilecek herhangi bir zarardan yazar sorumlu değildir.

Aracı yalnızca kendi sisteminizde veya izniniz olan test ortamlarında kullanın.

💡 Öneriler
Sanal makinelerde veya özel test ağlarında denemeler yapın.

GitHub’da paylaşırken README’deki disclaimer ve lisans bilgisini mutlaka koruyun.

Kod üzerinde değişiklik yaparak öğrenme ve test amaçlı geliştirmeler yapabilirsiniz.