# pages/3_pencegahan.py
import streamlit as st
from streamlit_player import st_player

st.set_page_config(
    layout="wide",
    page_icon='🎭',
    page_title="Waspada Penipuan Online",
)

#st.markdown ("Pencegahan Penipuan Online")
st.sidebar.markdown("# Pencegahan")
st.sidebar.image('klik.jpeg')
st.markdown('''<h1 style="margin-bottom:30px">Kenali, Cegah dan Atasi </h1>''',unsafe_allow_html=True)
col1,col2=st.columns([5,3])
with col1:
    st.write('''<p style="text-align:justify">Dibalik kecanggihan teknologi dan internet, masih banyak terdapat upaya jahat seseorang atau
    sekelompok orang untuk merugikan orang lain.</p>''',unsafe_allow_html=True)
    st.markdown('''<p style="text-align:justify">Salah satu modus pelaku kejahatan scamming/phising dalam sector finansial biasanya dilakukan dengan mengirimkan email atau pesan pribadi melalui chat WhatsApp kepada nasabah. Salah satu kasus penipuan yang terjadi dalam waktu dekat ini ialah penipuan yang mengatasnamakan salah satu bank terbesar di Indonesia. Isi pesan penipuan dalam email yang menggunakan profil dan kop surat meneyerupai akun email asli tersebut, berupa ancaman yang mengharuskan nasabah untuk melakukan konfirmasi terkait biaya administrasi terbaru sebesar Rp150.000,-/bulan. Nasabah akan diarahkan pada link palsu yang menyerupai link resmi untuk konfirmasi tersebut. Hal ini menyebabkan banyak nasabah yang terkecoh dan memberikan data pribadinya melalui link tersebut, sehingga pelaku penipuan dapat menguras saldo rekening korban melalui data tersebut.</p>''',unsafe_allow_html=True)
    st.write('''<p style="text-align:justify">Berikut adalah cara-cara mengenali kejahatan siber, cara mencegahnya dan mengatasinya.</p>''',unsafe_allow_html=True)
with col2:
    st.image('bri.jpeg')

st.write('### Mengidentifikasi *Phising* :')
col1,col2,col3=st.columns([2,4,2])
with col1:
    st.write()
with col2:
    st_player("https://youtu.be/yipOr_Mrcy4")
with col3:
    st.write()

option = st.selectbox(
    '',
    ('Pilih Tips','Mengidentifikasi ciri-ciri Phising',
    'Pencegahan Phising'))

if option=='Mengidentifikasi ciri-ciri Phising':
   st.write('#### Berikut tips dalam mengenali ciri-ciri Phising:')
   st.write('''
   1. Alamat *email* tidak sama seperti situs resmi, menggunakan domain yang berbeda.
   2. Ada lampiran *link* di dalam *email*.\n
      *Link* ini jika diperhatikan dengan teliti akan terlihat beda dengan *link* situs resmi.
   3. *Email* berisikan permintaan informasi pribadi, seperti nomor rekening bank, kartu kredit, ataupun diarahkan untuk login dengan kredensial internet banking.
   4. *Website* tidak menggunakan awalan **HTTPS**.\n
      Meskipun tidak semua website HTTP adalah *website phishing*, tapi *website* perusahaan besar tidak
      mungkin tidak menggunakan HTTPS.
   5. Domain *website* ada *typo*.\n
      Satu domain *website* tidak bisa digunakan untuk dua *website*. Sehingga *website phishing* pasti akan
      menambahkan 1-2 huruf atau karakter pada domain *webside*-nya.
   ''')
   st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
   st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{padding-left:2px;}</style>', unsafe_allow_html=True)
   pilih=st.radio('Contoh Phishing',('Email phishing 1','Email phishing 2', 'Website phishing 1', 'Website phishing 2'))

   if pilih=='Email phishing 1':
      st.image('bawaslu.jpeg')
   elif pilih=='Email phishing 2':
      st.image('mandiri.JPG')
   elif pilih=='Website phishing 1':
      st.image('webpaypal.jpeg')
   elif pilih=='Website phishing 2':
      st.image('amazon.png')
   else:
      st.write('')

elif option=='Pencegahan Phising':
   st.write('#### Tips-tips agar terhindar dari kejahatan Phising:')
   st.write('''Jika menerima email phising, yang harus dilakukan adalah :
   1. Jangan pernah memberikan informasi pribadi atau sensitif melalui email apapun.
   2. Jangan percaya link atau attachment dalam email yang tidak dikenal.
   3. Verifikasi tujuan link yang sebenarnya, meskipun berasal dari sumber terpercaya.
   4. Ketikan alamat situs Web daripada menggunakan link dari email yang tidak dikenal.
   5. Waspada nomor telepon dalam email. Gunakan nomor telepon yang ditemukan di daftar kontak anda atau
      di direktorat terpercaya seperti index buku telepon.
      ''')
else:
   st.write('')


st.write('### Mengidentifikasi *Scamming* :')
col1,col2,col3=st.columns([2,4,2])
with col1:
    st.write()
with col2:
    st_player("https://youtu.be/oZCm0pkFmNo")
with col3:
    st.write()

option = st.selectbox(
    '',
    ('Pilih Tips','Mengidentifikasi ciri-ciri Scamming',
    'Pencegahan Scamming'))

if option=='Mengidentifikasi ciri-ciri Scamming':
   st.write('#### Berikut tips dalam mengenali ciri-ciri Scamming:')
   st.write('''
   1. *Scammer* mengaku dari organisasi yang dikenal.\n
      Penipu menghubungi dengan berpura-pura mengatas-namakan organisasi resmi. Misalnya, pemerintah, kepolisian, rumah sakit, bank, marketplace, perusahaan terkenal,
      atau yang lain.
   2. *Scammer* mengatakan ada masalah.\n
      *Scammer* mengabarkan adanya masalah yang melibatkan anggota keluarga. Atau ada masalah di akun rekening
      maupun sosmed.
   3. *Scammer* menggunakan alasan menang hadiah.\n
      Dan untuk mendapatkan hadiahnya perlu membayar biaya tertentu.
   4. *Scammer* memaksa untuk segera melakukan perintah mereka.\n
      Menyuruh cepat-cepat mentransfer sejumlah uang tanpa alasan pasti.
   5. Menginstruksikan membayar dengan cara tertentu.\n
      *Scammer* memperintahkan mengirim uang melalui perusahaan pembayaran asing, bukan melalui rekening bank
      besar atau melalui *e-wallet* dengan nama yang asing.
   ''')
   st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
   st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{padding-left:2px;}</style>', unsafe_allow_html=True)
   pilih=st.radio('Contoh Scamming',('Email scamming 1','Email scamming 2', 'Email scamming 3'))

   if pilih=='Email scamming 1':
      st.image('emailscam.png')
   elif pilih=='Email scamming 2':
      st.image('scam.png')
   elif pilih=='Email scamming 3':
      st.image('Netflix.jpeg')
   else:
      st.write('')

elif option=='Pencegahan Scamming':
    st.write('''Agar terhindar dari *scamming*, adapun beberapa cara yang bisa kamu lakukan agar tidak menjadi
        korban diantaranya:
    1. Jaga Informasi Pribadi\n
       Jangan memberikan informasi pribadi atau keuangan sembarangan. Misalnya nomor KTP, nomor rekening bank
       atau nomor kartu kredit.
    2. Waspada Pada Perintah *Scammer*\n
       Jangan langsung ikuti perintah apapun dari *scammer*. Terlebih jika dipaksa untuk memberikan informasi
       pribadi atau membayar sejumlah uang.
    3. Pastikan Pembayarannya Resmi\n
       Ketahui bagaimana *scammer* meminta untuk membayar. Perusahaan yang sah akan menyediakan beberapa metode
       pembayaran valid seperti melalui akun bank atau dompet digital resmi.
    ''')

else:
   st.write('')


st.subheader('Berbagai Tips Pencegahan Kejahatan Siber')
st.write('Berikut tips-tips yang bisa dipelajari untuk mencegah mengalami kejahatan siber,')
option = st.selectbox(
    '',
    ('Pilih Tips','Pengamanan akun medsos',
    'Aman belanja online', 'Cek rekening penipuan','Cara aman bekerja dari rumah (WFH)'))

if option=='Pengamanan akun medsos':
   st.write('#### Berikut tips-tips pengamanan akun sosial media pribadi kita :')
   st.write('''
   - Selalu update sistem operasi dan aplikasi pada perangkat.
   - Selalu ingat alamat email dan nomor HP yang didaftarkan ke Instagram supaya pemulihan akun dapat dilakukan.
   - Aktifkan mfa (multi-factor authentication) dengan menggunakan salah satu aplikasi seperti Google Authenticator, Microsoft Authenticator, VIP Access, Authy, dan sebagainya. Mfa yang paling tidak aman adalah kode OTP yang dikirimkan melalui SMS!
   - Gunakan password yang kuat, tidak mudah tertebak. Lebih baik lagi menggunakan password manager yang memiliki fitur enkripsi.
   - Hati-hati dalam bersosial media, apabila ada teman yang meminta uang. Verifikasi ke akun lain, cobalah untuk menelpon atau bertemu langsung.
   ''')
elif option=='Aman belanja online':
   st.write('#### Tips-tips agar tidak tertipu ketika belanja online :')
   st.write('''
   - Riset Barang yang Dibeli.
   - Perhatikan Gambar Produk.
   - Cek Deskripsi Barang Terlebih Dahulu.
   - Perhatikan Ulasan Pembeli.
   - Cek Harga Produk.
   - Pilih Metode Pembayaran yang Tepat. Jangan melakukan pembayaran diluar aplikasi. Jika kita tidak membeli produk di marketplace, cek rekening penjual tersebut apakah akun tersebut benar atau akun tersebut sering digunakan untuk menipu.
   - Pastikan Membeli di Toko Online Terpercaya.
   ''')
elif option=='Cek rekening penipuan':
   st.write('#### Cara Cek Rekening Penipuan :')
   st.write('''
   **1. Cek rekening penipu di CekRekening.id by Kominfo** \n
      Website CekRekening.id juga memiliki fitur daftarkan rekening dan melaporkan rekening. Fitur daftarkan rekening, bermanfaat untuk kepercayaan pelanggan ketika metransfer uang. Sedangkan fitur laporkan rekening, digunakan untuk laporan nomor rekening penipuan dan transfer uang. Pengecekan rekening dapat dilakukan dengan cara:
      - Akses website [cekrekening.id](https://cekrekening.id/home)
      - Pilih 'Periksa Rekening' kemudian klik 'Cek Sekarang'
      - Pilih jenis akun (bank atau e-wallet)
      - Tulis nama bank dan nomor rekening
      - Tuliskan nomor virtual account dan nama e-wallet jika memilih e-wallet
      - Klik saya bukan robot
      - Pilih cek sekarang \n
   ''')
   st.image('cekrekening.png')
   st.caption('Halaman web cekrekening.id')
   st.write('''
   **2. Cek Rekening di Kredibel.co.id** \n
      Website Kredibel.co.id (sebuah komunitas anti fraud dengan jumlah 650 ribu anggota di Indonesia) menyediakan layanan untuk laporan penipuan lebih lengkap. Website ini menyediakan fitur cek rekening, cek telepon, dan laporkan penipuan. Website Kredibel.co.id memenuhi sertifikasi keamanan dan Penyelenggara Sistem Elektronik Kominfo. Cara cek rekening penipu di Kredibel.co.id:
      - Akses website [kredibel.co.id](https://www.kredibel.co.id)
      - Pilih Cek Rekening
      - Masukkan nomor rekening dan klik kolom biru bertuliskan cari \n
      Nantinya akan muncul informasi apakah nomor rekening tersebut dipakai sebagai penipuan.
      Anda juga bisa menemukan ulasan yang berada di bagian bawah pencarian rekening. Berbagai komentar dan bintang muncul beserta no rekening. Selain itu, Anda bisa memilih cek rekening sesuai bank yang dituju.
   ''')
   st.image('kredibel.png')
   st.caption('Halaman web kredibel.co.id')
elif option=='Cara aman bekerja dari rumah (WFH)':
   st.write('#### Cara tetap aman saat bekerja dari rumah (WFH)')
   st.write('''Berikut adalah tips keamanan WFH untuk memastikan Anda dan staf Anda bekerja dari rumah
   dengan aman, yang dirangkum dari situs [kaspersky](https://www.kaspersky.com/resource-center/threats/remote-working-how-to-stay-safe
).\n
   1. Gunakan perangkat lunak antivirus dan keamanan internet di rumah.
   2. Jauhkan anggota keluarga dari perangkat kerja. Gunakan kata sandi untuk mencegah pihak ketiga mengakses file sensitif.\n
   3. Gunakan penutup *webcam* geser atau cabut *webcam* eksternal agar peretas tidak mudah mengakses *webcam* tanpa izin dan mengganggu privasi Anda.\n
   4. Gunakan *Virtual Private Network* (**VPN**) perusahaan saat bekerja untuk menjaga keamanan data kantor yang berpotensi diekspos oleh peretas.
   5. Gunakan solusi penyimpanan terpusat seperti *cloud* atau *server* yang dilindungi oleh *firewall*, agar
      dokumen penting memiliki cadangan dan lebih aman.\n
   6. Amankan *Wi-Fi* rumah Anda. Keamanan *Wi- Fi* dapat ditingkatkan dengan cara:

      •	Gunakan kata sandi yang kuat dan unik.

      •	Ubah **SSID** Anda. Aktifkan enkripsi jaringan.

      •	Batasi akses jaringan ke ***MAC address*** tertentu untuk keamanan tambahan.

      •	Jalankan versi terbaru dari *firmware* Anda dengan sering mengunjungi halaman pengaturan *router*.

      •	Selalu perbarui *patch* dan aplikasi.

   7. Waspada terhadap aplikasi konferensi video untuk melindungi informasi sensitif perusahaan.

      •	Pastikan rapat bersifat pribadi, baik dengan mewajibkan kata sandi untuk masuk atau mengontrol akses
         tamu dari ruang tunggu.

      •	Mempertimbangkan persyaratan keamanan saat memilih vendor. ***Enkripsi end to end*** menawarkan privasi
         dan keamanan yang penting.

      •	Pastikan aplikasi diperbarui dengan menginstal *patch* terbaru dan pembaruan aplikasi.

   8. Pastikan kata sandi Anda kuat dan aman di seluruh perangkat.
   9. Lindungi perbankan *online* Anda.

      •	Hanya gunakan aplikasi dan layanan terakreditasi untuk menangani keuangan. Cek kredibilitas platform
         dengan mencari ulasan dan informasi lebih lanjut sebelum menggunakannya.

      •	Pastikan Anda masuk melalui *Secure Hypertext Transfer Protocol* (**https:// bukan http://**) saat mengakses
         situs web perbankan.

      •	Perhatikan juga ikon gembok di ujung kiri URL, yang menunjukkan bahwa situs web memiliki sertifikat
         keamanan yang diautentikasi.

      •	Jika menggunakan *mobile banking*, gunakan fitur verifikasi sidik jari atau identifikasi wajah untuk
         masuk, yang dapat meningkatkan keamanan lebih jauh.

      •	Jangan memberikan detail bank Anda kepada siapa pun, atau mentransfer dana ke vendor yang tidak
         diminta.

   10. Waspadalah terhadap penipuan *email* dan keamanan *email* Anda. Email merupakan salah satu sarana komunikasi termudah untuk dieksploitasi dan dikompromikan.\n
   • Pastikan *email* hanya dapat diakses dengan aman melalui VPN perusahaan, yang membuat koneksi jaringan
     terenkripsi dengan mengautentikasi pengguna dan/atau perangkat dan mengenkripsi data saat transit antara
     pengguna dan layanan Anda.

   •	Pastikan perangkat mereka mengenkripsi data saat tidak tidak digunakan, yang akan melindungi data
      *email* di perangkat jika perangkat hilang atau dicuri. Pastikan enkripsi bawaan telah diaktifkan dan
      dikonfigurasi.

   •	Waspadalah terhadap serangan *phishing* yang semakin marak.

''')
else:
   st.write('')

st.write('\n')
st.write('\n')
st.write('\n')
if 'count' not in st.session_state:
   st.session_state['count']=0

st.write('Apakah anda menyukai konten web ini?')
col1,col2=st.columns(2)
like= col1.button('Ya')
tidak=col2.button('Tidak')

if like:
   st.session_state['count']+=1
   a=st.session_state
   col3,col4=st.columns([2.5,8])
   col3.write(a)
   col4.write('\n')
   #col2.write('\n')
#col2.write('\n')
   col4.write('**orang menyukai konten web ini**')
elif tidak:
    st.write('#### Terima kasih')
    st.balloons()

st.write('\n')
st.write('\n')
st.write('\n')
st.info('Hackathon of Women In Tech by Kominfo. PINK HAT, 2022')
