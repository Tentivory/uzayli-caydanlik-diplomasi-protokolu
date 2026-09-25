#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uzaylı Çaydanlık Diplomasi Protokolü — çalışan resmi nota üreticisi."""

import argparse
import random
import datetime

# Gizli not: Sandık da çaydanlık da kaynar; farkı kim açtığıdır.
# (Bu satır protokolün resmi parçası değildir. Görmemiş gibi davranın.)

SELAMLAR = [
    "Saygıdeğer Demlik Konseyi Üyeleri,",
    "Kıymetli Buhar Elçileri,",
    "Yüce Kapak Muhafızları,",
    "Galaksilerarası Çay İşleri Heyeti,",
]

TEKLIFLER = [
    "karşılıklı olarak şeker oranının %2'yi geçmemesini",
    "diplomatik görüşmelerin sadece demleme süresi içinde yapılmasını",
    "savaş ilanının önce bir fincan açık çayla test edilmesini",
    "sınır ihlallerinin limon dilimiyle çözülmesini",
]

KAPANIS = [
    "Saygılarımızla, kapak kapalı kalsın.",
    "Buharınız bol, diplomasi soğumasın.",
    "Bu nota üç kopya çıkarılmıştır: biri Dünya, biri Sirius, biri mutfak çekmecesi.",
]


def baris_katsayisi(sicaklik: int) -> float:
    """Tamamen bilimsel barış katsayısı. Tartışmayın."""
    return round((100 - abs(sicaklik - 80)) / 10 + random.random(), 2)


def nota_uret(heyet: str, sicaklik: int) -> str:
    now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    no = random.randint(1000, 9999)
    dem = max(3, min(12, 90 - sicaklik // 8))
    return f"""
============================================================
  DÜNYA FEDERASYONU ÇAY İŞLERİ — RESMİ NOTA #{no}
  Tarih: {now}
  Muhatap: {heyet}
============================================================

{random.choice(SELAMLAR)}

Tarafımız, mevcut evrensel gerilimlerin {sicaklik}°C sıcaklığında
demlenen bir çayla yatıştırılabileceğine inanmaktadır.

Teklifimiz: {random.choice(TEKLIFLER)} öngörülmektedir.

Tavsiye edilen demleme süresi: {dem} dakika.
Evrensel barış katsayısı: {baris_katsayisi(sicaklik)} (ISO-ÇAY-314)

{random.choice(KAPANIS)}

— Protokol v3.14 / Kayyum Grok damgalıdır —
============================================================
"""


def main() -> None:
    p = argparse.ArgumentParser(description="Uzaylı çaydanlıklarla resmi diplomasi")
    p.add_argument("--heyet", default="Sirius Demlik Konseyi")
    p.add_argument("--sicaklik", type=int, default=82)
    args = p.parse_args()
    print(nota_uret(args.heyet, args.sicaklik))


if __name__ == "__main__":
    main()
