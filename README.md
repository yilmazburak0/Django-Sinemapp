# Django-Sinemapp

Django-Sinemapp, Django web çatısı kullanılarak geliştirilmiş kapsamlı bir sinema filmleri uygulamasıdır. Bu platform, kullanıcıların filmleri keşfetmelerine, yorumlamalarına ve kişisel izleme listeleri oluşturmalarına olanak tanır.

## Özellikler

- **Film Kataloğu**: Vizyondaki ve yakında gösterime girecek filmler için detaylı bilgiler
- **Film Detayları**: Bütçe, IMDB puanı, açıklama, çıkış tarihi gibi kapsamlı film bilgileri
- **Oyuncu Kadrosu**: Filmlerin oyuncu kadrosu bilgileri
- **Film Fragmanları**: Entegre video oynatıcı ile film fragmanları görüntüleme
- **Kullanıcı Yorumları**: Filmler hakkında yorum yapma ve puanlama sistemi
- **İzleme Listesi**: Kullanıcıların kendi izleme listelerini oluşturabilmesi
- **Kullanıcı Hesapları**: Kayıt olma, giriş yapma ve profil yönetimi
- **Responsive Tasarım**: Mobil cihazlarla uyumlu arayüz

## Teknolojiler

### Backend
- **Django 3.2.7**: Python tabanlı web framework
- **SQLite**: Veritabanı yönetim sistemi
- **CKEditor**: Zengin metin editörü entegrasyonu

### Frontend
- **HTML5/CSS3**: Sayfa yapısı ve stillendirme
- **Bootstrap 5**: Responsive tasarım framework'ü
- **Font Awesome 4.7**: İkon kütüphanesi
- **JavaScript**: Dinamik frontend işlevselliği

## Proje Yapısı

```
Django-Sinemapp/
├── sinemapp/               # Proje ana dizini
│   ├── static/             # Statik dosyalar (CSS, JS, resimler)
│   ├── staticfiles/        # Toplanan statik dosyalar
│   ├── templates/          # Genel şablonlar
│   ├── uploads/            # Kullanıcı yüklemeleri (filmler, profil resimleri)
│   ├── movies/             # Film uygulaması
│   │   ├── migrations/     # Veritabanı migrasyonları
│   │   ├── templates/      # Film şablonları
│   │   ├── __init__.py
│   │   ├── admin.py        # Admin paneli yapılandırması
│   │   ├── apps.py         # Uygulama yapılandırması
│   │   ├── forms.py        # Form tanımlamaları
│   │   ├── models.py       # Veritabanı modelleri
│   │   ├── tests.py        # Testler
│   │   ├── urls.py         # URL yapılandırması
│   │   └── views.py        # Görünüm fonksiyonları
│   ├── account/            # Kullanıcı hesapları uygulaması
│   │   ├── migrations/     # Veritabanı migrasyonları
│   │   ├── templates/      # Hesap şablonları
│   │   ├── __init__.py
│   │   ├── admin.py        # Admin panel yapılandırması
│   │   ├── apps.py         # Uygulama yapılandırması
│   │   ├── forms.py        # Hesap formları
│   │   ├── models.py       # Kullanıcı modelleri
│   │   ├── tests.py        # Testler
│   │   ├── urls.py         # URL yapılandırması
│   │   └── views.py        # Kullanıcı görünümleri
│   ├── sinemapp/           # Proje yapılandırması
│   │   ├── __init__.py
│   │   ├── asgi.py         # ASGI yapılandırması
│   │   ├── settings.py     # Proje ayarları
│   │   ├── urls.py         # Ana URL yönlendirmeleri
│   │   └── wsgi.py         # WSGI yapılandırması
│   ├── db.sqlite3          # SQLite veritabanı
│   ├── manage.py           # Django yönetim aracı
│   └── requirements.txt    # Gerekli Python paketleri
└── README.md               # Proje dokümantasyonu
```

## Kurulum

1. Projeyi klonlayın:
```
git clone https://github.com/yilmazburak0/Django-Sinemapp.git
cd Django-Sinemapp
```

2. Sanal ortamı oluşturun ve etkinleştirin:
```
python -m venv myenv
# Windows için
myenv\Scripts\activate
# Linux/Mac için
source myenv/bin/activate
```

3. Gerekli paketleri kurun:
```
pip install -r sinemapp/requirements.txt
```

4. Veritabanı migrasyonlarını uygulayın:
```
cd sinemapp
python manage.py migrate
```

5. Sunucuyu başlatın:
```
python manage.py runserver
```

6. Tarayıcınızda `http://127.0.0.1:8000` adresine giderek uygulamayı görüntüleyebilirsiniz.

## Ortam Değişkenleri

Proje aşağıdaki ortam değişkenlerini kullanır:

- `SECRET_KEY`: Django güvenlik anahtarı
- `IS_DEVELOPMENT`: Geliştirme modunu etkinleştirme (True/False)
- `APP_HOST`: Uygulama host adresi

## Admin Paneli

Admin paneline erişmek için bir süper kullanıcı oluşturun:

```
python manage.py createsuperuser
```

Oluşturduğunuz kullanıcı bilgileriyle `http://127.0.0.1:8000/admin` adresinden admin paneline erişebilirsiniz.

## Lisans

Bu proje açık kaynak olarak dağıtılmakta olup, geliştirme ve test amaçlı kullanıma sunulmuştur.

## İletişim

yilmazburak1210@gmail.com
