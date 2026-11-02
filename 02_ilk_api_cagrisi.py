import requests

talep = "Finans raporu çok yavaş açılıyor ve gösterilen satış tutarları da yanlış."

prompt = f"""
Aşağıdaki teknik destek talebini analiz et.

Talep: {talep}

Kategori yalnızca şunlardan biri olabilir:
Erişim, Performans, Veri Kalitesi, Diğer

Öncelik yalnızca:
Düşük, Orta, Yüksek

Şu alanlarla JSON üret:
kategori, oncelik, gerekce, eksik_bilgiler

eksik_bilgiler bir liste olmalıdır.
Bilgi uydurma.
"""
URL = "http://localhost:11434/api/chat"
for sicaklik in [0.1,0.7,1.3]:

    payload = {"model" : "qwen3.5:4b" ,
              "messages" : [{"role": "user",
                             "content": prompt}],
               "options": {"temperature": sicaklik},
               "stream": False}

    response = requests.post(URL,json=payload)
    response.raise_for_status()
    print(response.json()["message"]["content"])
    print(f"Temperature : {sicaklik}")
