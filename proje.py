def tas_kagit_makas_ZEYNEP_BİLGE_ESKİN():

      print("Taş, Kağıt, Makas! Oyununa Hoşgeldin!")
      print("Hazır olduğunda taş, kağıt veya makas yazarak oyunu başlatabilirsin.")
      print("İki tur kazanan ilk kişi oyunun galibi olacak.")
      print("Unutma, oyunu istediğin kadar devam ettirebilirsin!")
      print("Oyundan çıkmak istediğinde 'çıkış' yazman yeterli.")
      print("Bol şans!")

      import random

      while True:
            seçenekler = ["taş", "kağıt", "makas"]
            oyuncu_galibiyet = 0
            bilgisayar_galibiyet = 0
            tur_sayısı = 0

            while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:
                  oyuncu_secimi = input("Taş Mı, Kağıt Mı, Makas Mı? ").lower()

                  if oyuncu_secimi == "çıkış":
                        print("Oyundan çıktınız.")
                        print("Görüşmek üzere!")
                        return


                  if oyuncu_secimi not in seçenekler:
                        print("Bu ne demek? Lütfen tekrar deneyin.")
                        continue

                  bilgisayar_secimi = random.choice(seçenekler)
                  print(f"Bilgisayar şunu seçti: {bilgisayar_secimi}")

                  if oyuncu_secimi == bilgisayar_secimi:
                        print("Berabere Kaldınız!")

                  elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                          (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                          (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                        print("Bu turu kazandın!")
                        oyuncu_galibiyet += 1
                  elif oyuncu_galibiyet < 2 or bilgisayar_galibiyet < 2:
                        print("Bu turu bilgisayar kazandı. Tekrar dene!")
                        bilgisayar_galibiyet += 1


                  print(f"Oyuncunun Skoru: {oyuncu_galibiyet}")
                  print(f"Bilgisayarın Skoru: {bilgisayar_galibiyet}")

            if oyuncu_galibiyet == 2:
                  print("TEBRİKLER! Oyunu Kazandın!")
            else:
                  print("Maalesef oyunu kaybettin. Bilgisayar oyunu kazandı.")
                  print("Belki bir dahaki sefer sen kazanırsın! Denemekten vazgeçme!")

            devam = input("Bir daha oynamak ister misin? (evet/hayır):").lower()
            bilgisayar_yanıt = random.choice(["evet", "hayır"])

            if devam == "hayır" and bilgisayar_yanıt == "evet":
                  oyuncu_son_secim = input("Ama bilgisayar oynamak istiyor, devam etmek ister misin? (evet/hayır): ").lower()
                  if oyuncu_son_secim == "hayır":
                        print("Oyun sona erdi. Sonra görüşürüz!")
                        break

            if devam == "evet" and bilgisayar_yanıt == "hayır":
                  print("Sen oynamak istesen de bilgisayar daha fazla oynamak istemiyor")
                  break

            if devam not in ["evet", "hayır"].lower():
                  print("Sadece evet ya da hayır yazın")

            else:
                  print("Yeni oyun başlatılıyor... Bol şans!")



tas_kagit_makas_ZEYNEP_BİLGE_ESKİN()









