# Projenin Adi : Finansal Veri Analizi ve Tahmin Projesi


# Projenin amacı
finansal veriler üzerinde analiz yaparak, belirli bir hisse senedinin kapanış değerini etkileyen faktörleri anlamak, bu faktörler arasındaki ilişkileri görselleştirmek ve bu veri analizi sonucunda regresyon modeli kullanarak gelecekteki kapanış değerini tahmin etmeye çalışmaktır.

# Ana Hedefler
   Finansal veri analizi: Proje, çeşitli finansal veri kaynaklarından elde edilen verileri çeker ve analiz eder.
   İlişkisel analiz: Faktörler arasındaki ilişkileri belirlemek için korelasyon matrisleri ve grafikler kullanılır.
   Görselleştirme: Matplotlib ve Seaborn gibi kütüphaneler kullanılarak veriler görselleştirilir, analiz sonuçları kullanıcı dostu grafiklerle sunulur.
   Regresyon modeli: Scikit-learn kütüphanesi ile bir regresyon modeli oluşturulur ve eğitilir.
   Tahmin ve Değerlendirme: Oluşturulan model kullanılarak gelecekteki hisse senedi kapanış değerleri tahmin edilir ve modelin performansı değerlendirilir

# Projenin Adımları : 
1 - Hisse senedi verilerinin toplanması ve kullanılabilir hale getirilmesi.
(selenium kütüphanesi kullanmıştır veri çekme aşamasının kodu github hesabımda mevcutur)
2 - Veri ön işleme adımları ile null değerlerin temizlenmesi ve verilerin normalizasyonu.
3 - İlişki analizi ile değişkenler arasındaki bağlantıların anlaşılması.(Görselleştirme)
4 - Regresyon modeli kullanarak gelecekteki kapanış değerini tahmin etme.


# Kod Açıklamaları:

1.  hisse_senedi_regresyon_analizi.ipynb: 
    -Finansal verilerin analizi için kullanılan dosya.
   - Veri temizleme, düzenleme bu dosyada yapıldı
   - Korelasyon matrisleri ve grafiklerle ilişkiler gösterilir.
   - Matplotlib ve Seaborn gibi görselleştirme kütüphaneleri kullanılır.
   - Veri seti üzerinde istatistiksel analizler yapıldı.
    Gelecekteki kapanış değerini tahmin etmek için regresyon modeli oluşturuldu .
   - Veri seti üzerinde eğitim ve test verisi ayrılır.
   - Makine öğrenimi modeli, örneğin sklearn kütüphanesi kullanılarak oluşturulur.
   - Model performansı değerlendirilir.
   - modelin verdiği sonuçlar gerçek sonuçlarla ve veri setinde olmayan diğer verilerle kıyaslandı

2. hisse.py dosyasında
   - hisse senedinini verileri bir web sitesinden çekilmiş ve   03-09-2020 / 09-11-2023 arasındak borsa verilerini kapsamakatadır veri seti Hüseyin Erol tarafından oluşturulmuştur.



## Kullanılan Kütüphaneler

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [seaborn](https://seaborn.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [tensorflow](https://www.tensorflow.org/)
- [selenium](https://www.selenium.dev/)


# Geliştirici : Hüseyin Erol
# huseyineroll2434@gmail.com bana gmail hesabımdan ulaşabilirsiniz
