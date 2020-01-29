import numpy as np
from firebase import firebase
import cv2
import time

#                                                                                           CAMERA1
# firebase 'de oluşturduğumuz database linkini app_url değişkenine atıyoruz.
App_url = 'https://carcounting-a39b1.firebaseio.com/'
# firebase connection işlemleri
firebase = firebase.FirebaseApplication(App_url)


# elde edilen araba sayısını fonksiyon yardımı ile firebase'e gönderiyoruz.
# Ben ArabaSayac adında bir alan ve child olarak Sayac alanı eklemiştim.
def Aktar(sayi):
    result = firebase.put('/ArabaSayac', 'Sayac', sayi)


# Video_Yolu = input("Video Yolunu Yapıştırın (C:\\xx\\video.mp4):  ")
# Frame_Yolu = input("Frame Yolunu Yapıştırın (C:\\xx\\video.png):  ")
Giden_Araba_Sayisi = 0  # Araba sayılarını tutacagimiz degiskenimiz.
line = 500  # Arabalari saymak icin kontor farklari icin kullancagimiz ekrana cizdigimiz yatay cizgi uzunlugu
video = cv2.VideoCapture('C:/Users/murat/video1.mp4')  # video yu açıyoruz.

# -------------#cv2.bgsegm.createBackgroundSubtractorMOG()#----------------------
# alltaki mog nesnesi ve yukarıdaki mog nesnesi kurulan python versiyonuna göre farklılık göstermektedir
# Sizde hangisi çalışıyorsa onu kullanabilirsiniz.
Mog_Nesnesi = cv2.bgsegm.createBackgroundSubtractorMOG()  # arka plan
# Bos_frame'i videoda araba geçmeyen bir anda aldığım ekran görüntüsünden elde ettim. Dolu görüntü ve boş görüntü arasındaki,
# farkı anlamak için boş bir frame oluşturuyoruz.
Bos_Frame = cv2.imread('C:/Users/murat/video1.png')
Onceki_Kontor = []
Maske = Mog_Nesnesi.apply(Bos_Frame)
while (video.isOpened()):
    ret, frame = video.read()
    Maske = Mog_Nesnesi.apply(frame)

    # cv2.dilate fonksiyonu bizim thresh olarak çevirdiğimiz frame videosunda parça parça gözüken araba imgelerini
    # birleştirmeye yarıyor. Zaten dilate opencv'de 'yayma' olarak geçtiği için birbirine yakın olan parçaları bir bütün
    # olarak imgeye yayıyor. Bunu yapma sebebimiz kontör tespitlerinde her küçük parçayı bir imge olarak ele almaması içindir.
    Thresh_Maske = cv2.dilate(Maske, None, iterations=2)

    # findContours metodu opencv'de kontör yaklaşma metodu olarak bilinir.
    # cv2.CHAIN_APPROX_SIMPLE parametresi kontörlerimizin köşe noktalarını almamızı sağlar.
    # *     *

    # *     * imgeyi bir kare olarak düşünürsek şekildeki gibi köşeleri alır.(Daha iyi anlaşılması için şeklen göstermek istedim).
    Kontor = cv2.findContours(Thresh_Maske.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    Simdiki_Kontor = []
    for kontor in Kontor:
        # Buradaki kontrol bizim thresh framemizde ki tespit edilecek olan noktaların boyutunu kontrol etmek içindir.
        # Bu değer küçüldükçe frame içinde yer alan ufak thresh parçalarını da almaktadır. Bu bizim istediğimiz birşey değildir.
        # Bizim aradığımız araç boyutunda ki thresh imgeleridir.
        # Bu imgeleri en optimize şekilde veren değeri ben 5000 olarak belirledim. Siz deneyerek daha optizimize olan değeri bulabilirsiniz.
        if cv2.contourArea(kontor) < 5000:
            continue

            # Bulunan kontorün boyutlarını alıyoruz.
        (x, y, w, h) = cv2.boundingRect(kontor)

        # Kontor çizimini bulunan x,y boyutuna göre köşelerine uygun ölçüde yerleştiriyoruz. Yani Kutu içerisine alıyoruz.
        # cv2.rectangle 5 değer almaktadır.
        # 1-frame videomuz,
        # 2-tespit edilen thresh imge boyutları,
        # 3-çizilecek karenin boyutları,
        # 4-çizilecek karenin rengi,
        # 5-karenin kalınlığı
        cv2.rectangle(frame, (x, y), (x + w - 20, y + h - 20), (0, 255, 0), 2)

        # şimdiki kontor listesine x,y uzunluğunu atıyoruz.
        Simdiki_Kontor.append([x, y])

    # Onceki ve şimdiki olarak tanımladığımız bu listeler araç saymak için karşılaştırma yapacağımız değişkenlerdir.
    if (len(Onceki_Kontor) == 0):
        # Bu kontrol ilk çalıştırdığımızda gerçekleşecek olan işlemdir. Yani döngü ilk başladığında girilecek olan kontroldür.
        # Burada görüntüye giren ilk imgeyi önceki olarak tanımlıyoruz ki sonradan gelecek olanlara şimdiki diyebilelim diye.
        Onceki_Kontor = Simdiki_Kontor
        continue

    Kapali_Kontor_Listesi = []
    for i in range(len(Simdiki_Kontor)):
        #
        minimum_aralık = 2000000
        for j in range(len(Onceki_Kontor)):
            uzunluk_x = Simdiki_Kontor[i][0] - Onceki_Kontor[j][0]
            print("x uzunlugu-> " + str(uzunluk_x))
            uzunluk_y = Simdiki_Kontor[i][1] - Onceki_Kontor[j][1]
            print("y uzulugu-> " + str(uzunluk_y))
            kontor_uzaklık = uzunluk_x * uzunluk_x + uzunluk_y * uzunluk_y
            print("kontor_uzaklık -> " + str(kontor_uzaklık))
            if (kontor_uzaklık < minimum_aralık):
                minimum_aralık = kontor_uzaklık
                closest_contour = j
                print("j -> " + str(j))
        Kapali_Kontor_Listesi.append(closest_contour)
        print("Kapalı kontor listesi-> " + str(Kapali_Kontor_Listesi))
    for i in range(len(Simdiki_Kontor)):
        y_previous = Onceki_Kontor[Kapali_Kontor_Listesi[i]][1]
        print("y_previous  -> " + str(y_previous))
        if (Simdiki_Kontor[i][1] < line and y_previous > line):
            print("kontrol  -> " + str(Simdiki_Kontor[i][1]) + " < " + str(line) + " and " + str(
                y_previous) + " > " + str(line))
            Giden_Araba_Sayisi = Giden_Araba_Sayisi + 1
            print("ARABA SAYISI= " + str(Giden_Araba_Sayisi))
    Onceki_Kontor = Simdiki_Kontor
    print("ONCEKI KONTOR= " + str(Onceki_Kontor) + " VE " + "SIMDIKI_KONTOR= " + str(Simdiki_Kontor))
    cv2.line(frame, (0, line), (frame.shape[1], line), (0, 255, 255), 5)
    cv2.putText(frame, "Araba Sayisi: " + str(Giden_Araba_Sayisi), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('Frame2', frame)
    zaman = time.strftime("%S")
    saniye = int(zaman)
    if (saniye % 5 == 0):
        Aktar(Giden_Araba_Sayisi);

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    print("DONGU SONU------------------------------------------------\n\n\n")
video.release()
cv2.destroyAllWindows()