#   catatan penting:
#   sebelum me-run file ini wajib menuliskan perintah berikut ke cmd/terminal di virtual environment
#   pip install streamlit
#   pip install pandas
#   pip install matplotlib
#   pip install numpy
#   pip install bokeh
#   pip install scikit-learn
################################################################
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import HoverTool

st.set_page_config(
    layout="wide",
    page_icon='🎭',
    page_title="Waspada Penipuan Online",
)

st.sidebar.markdown("# Data")
st.sidebar.image('Grafik.png')
st.title('Mari Kita Lihat Datanya...')

st.subheader('Pengguna Internet di Indonesia')
st.write('''Berdasarkan data "DIGITAL 2022 INDONESIA" yang diterbitkan oleh We Are Social, pengguna internet di Indonesia
telah mencapai 205 juta orang pada Januari 2022. Atau meningkat sebanyak **1%** dari Januari 2021. 
Artinya **73,7%** dari total penduduk Indonesia telah menggunakan internet.  ''')

#data jumlah pengguna internet di Indonesia
df_penggunainternet = pd.DataFrame({
    'tahun':['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],
    'jumlah(dalam_juta)':[39.6,60.6,71,89.6,90.7,136,146,174,176,203,205]
    
})
##df_penggunainternet 

#grafik jumlah pengguna internet di Indonesia
fig=plt.figure(figsize=(10,5)) 
plt.bar(df_penggunainternet['tahun'],df_penggunainternet['jumlah(dalam_juta)'],color='purple') 
plt.text(-0.5,41,'39.6 Juta')
plt.text(0.5,62,'60.6 Juta')
plt.text(1.6,73,'71 Juta')
plt.text(2.5,92,'89.6 Juta')
plt.text(3.5,97,'90.7 Juta')
plt.text(4.55,138,'136 Juta')
plt.text(5.55,148,'146 Juta')
plt.text(6.55,176,'174 Juta')
plt.text(7.55,178,'176 Juta')
plt.text(8.55,205,'203 Juta')
plt.text(9.55,207,'205 Juta')
plt.xlabel('Tahun',style='oblique')
plt.ylabel('Jumlah Pengguna Internet',style='oblique')
plt.yticks([0,25,50,75,100,125,150,175,200],['','','','','','','','',''])
plt.title('Jumlah Pengguna Internet di Indonesia\n Pada Januari 2012 - Januari 2022')
st.pyplot(fig)
st.caption('sumber data : DIGITAL 2022 INDONESIA, We Are Social')

st.write('''Dari pengguna internet **205 juta** orang ini, pengguna internet dengan kategori dewasa telah sadar
akan kejahatan siber dan mempunyai cara untuk mencegahnya. Berikut adalah data perspektif dan aktivitas 
pengguna internet dewasa di Indonesia berdasarkan data "DIGITAL 2022 INDONESIA."''')

col1,col2=st.columns(2)
n1='<p style="color:Blue;font-size:40px;"><strong>60.3%</strong></p>'
col1.markdown(n1, unsafe_allow_html=True)
col1.write('**Pengguna khawatir tentang antara yang nyata atau yang palsu di internet**')
n2='<p style="color:Red;font-size:40px;"><strong>36.4%</strong></p>'
col2.markdown(n2, unsafe_allow_html=True)
col2.write('**Pengguna khawatir tentang data pribadi mereka di internet**')

col3,col4=st.columns(2)
n3='<p style="color:Orange;font-size:40px;"><strong>36.3%</strong></p>'
col3.markdown(n3, unsafe_allow_html=True)
col3.write('**Pengguna menolak cookie pada situs web**')
n4='<p style="color:Green;font-size:40px;"><strong>41.7%</strong></p>'
col4.markdown(n4, unsafe_allow_html=True)
col4.write('**Pengguna menggunakan alat untuk memblokir iklan di internet**')
n5='<p style="color:Grey;font-size:40px;"><strong>40.8%</strong></p>'
st.markdown(n5, unsafe_allow_html=True)
st.write('**Pengguna menggunakan VPN untuk mengakses internet**')
st.caption('sumber data : DIGITAL 2022 INDONESIA, We Are Social')

#peta sebaran
df_daerah=pd.read_csv('https://raw.githubusercontent.com/benangmerah/wilayah/master/datasources/daftar-nama-daerah.csv')
df_prov=df_daerah.head(33)
df_prov=df_prov[['name','latitude','longitude']]
df_prov.loc[34]=['Provinsi Kalimantan Utara',2.72594,116.911] #menambahkan data kalimantan utara
df_daerah=pd.read_csv('https://raw.githubusercontent.com/ayume-gah/data/main/Persentase%20Rumah%20Tangga%20yang%20Pernah%20Mengakses%20Internet%20dalam%203%20Bulan%20Terakhir%20Menurut%20Provinsi%20dan%20Klasifikasi%20Daerah.csv',delimiter=';')
df_daerah=df_daerah.head(35)
df_daerah=df_daerah['2020']
df_prov['prosentase_rumah_tangga_pengguna_internet']=df_daerah
#df_prov
st.subheader('Peta Sebaran Pengguna Internet di Indonesia')
st.write('Pengguna internet telah tersebar di **34** Provinsi di Indonesia (data Badan Pusat Statistik 2020).')
st.map(df_prov)
st.caption('sumber data : BPS, Badan Pusat Statistik')
if st.checkbox('Tampilkan Sebaran Pengguna Internet',):
    st.write('''##### Data Prosentase Rumah Tangga yang Mengakses Internet di Indonesia Pada Tahun 2020''')
    st.table(df_prov)
    

st.subheader('Anomali Trafik Internet di Indonesia')
st.write('''Badan Siber dan Sandi Negara (**BSSN**) setiap tahunnya merilis laporan Monitoring Keamanan Siber 
yang menampilkan jumlah anomali trafik internet di Indonesia. Jumlah anomali trafik internet ini cenderung 
naik setiap tahunnya terutama di masa pandemi.''')
st.write('''Mengutip dari **kaspersky.com**, peneliti mencatat bahwa peningkatan bekerja jarak jauh 
mengakibatkan bertambahnya aktivitas berbahaya berupa pengiriman *spam*, *phishing*, dan bahkan file berbahaya.''')
st.write('''Dengan meningkatnya bekerja jarak jauh atau WFH, ancaman keamanan siber terutama *phishing* 
menjadi lebih umum terjadi. Karena pada sebagian besar kantor mempunyai tim IT yang mengurus keamanan siber di dalam 
kantor. Namun pada kondisi WFH, pekerja harus lebih memperhatikan ancaman keamanan siber pada perangkat pribadi.''')
st.write('''Pernyataan **kaspersky.com** ini diperkuat dengan data trafik anomali internet di Indonesia di tahun 2021
yang meningkat tajam dari tahun sebelumnya. Hal ini dikarenakan pada tahun 2021, Indonesia masih menerapkan
WFH dan pembelajaran jarak jauh dengan minimnya sekuritas pada perangkat pribadi.''')


#data jumlah anomali trafik internet di Indonesia
df_anomali= pd.DataFrame({
    'Tahun':['2018','2019','2020','2021','2022 (data Jan-Feb 2022)'],
    'Jumlah':[232447974,290381283,495337202,1637973022,385087218]
})

#grafik anomali trafik
fig=plt.figure(figsize=(10,5)) 
plt.bar(df_anomali['Tahun'],df_anomali['Jumlah'],color='orange') 

plt.text(-0.3,89000000,'232,447,974',color='green')
plt.text(0.7,159000000,'290,381,283',color='green')
plt.text(1.7,359000000,'495,337,202',color='green')
plt.text(2.65,1479000000,'1,637,973,022',color='green')
plt.text(3.6,159000000,'385,087,218\n(data Jan-Feb 2022)',color='green')
plt.xlabel('Tahun',style='italic')
plt.ylabel('Jumlah Anomali Trafik',style='italic')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6],['','','','','','','','',''])
plt.title('Jumlah Anomali Trafik Internet di Indonesia\n Pada Tahun 2018 Hingga 2022')
st.pyplot(fig)
st.caption('sumber data : Laporan Monitoring BSSN, Badan Siber dan Sandi Negara')

#menampilkan tabel anomali
#if st.checkbox('Tampilkan Data Anomali Trafik Internet',):
 #   st.write('''##### Data Jumlah Anomali Trafik Internet di Indonesia\n Pada Tahun 2018 Hingga 2022''')
  #  st.table(df_anomali)

st.subheader('Faktor yang Mempengaruhi Anomali Trafik Internet')
st.write('''Pada tahun 2021, anomali trafik internet meningkat tajam dibandingkan dengan tahun sebelumnya. 
Tahun 2021 adalah masa pandemi **COVID19** di Indonesia, dimana diberlakukannya pembatasan mobilitas 
masyarakat. Sehingga aktivitas bekerja dan belajar dilakukan jarak jauh atau secara daring. Pembatasan 
mobilitas masyarakat ini juga menyebabkan meningkatnya transaksi *e-commerce*, berdasarkan data Bank Indonesia (**BI**).
 Trafik internet meningkat namun tidak diimbangi dengan meningkatnya keamanan siber pada perangkat pribadi, 
 menyebabkan adanya lonjakan kasus anomali trafik internet.''')

a=np.array([(232447974/1000000),(290381283/1000000),(495337202/1000000),(1637973022/1000000)]) #data anomali
p=np.array([146,174,176,203])                               #data pengguna
e=np.array([106,206,266,401])                               #data ecommerce
x=[2018,2019,2020,2021] #tahun

df_data=pd.DataFrame(
    (['2018',a[0]*1000000,p[0],e[0]],['2019',a[1]*1000000,p[1],e[1]],['2020',a[2]*1000000,p[2],e[2]],
    ['2021',a[3]*1000000,p[3],e[3]]),
    columns=['Tahun','Anomali_Trafik(JutaKasus)','Pengguna_Internet(JutaOrang)',
    'Nilai_Transaksi_Ecommerce(TriliunRupiah)']
    )

p1=figure(
    title='Pengguna Internet VS Anomali Trafik VS Nilai Transaksi E-Commerce (Data 2018-2021)',
    x_axis_label='Tahun',
    #tools=[HoverTool()],
    #tooltips='@y',
    width=200,
    height=450,
    )

plot1=p1.line(x,p,legend_label='Pengguna Internet (Juta orang)',color='green',line_width=2)
p1.add_tools(HoverTool(renderers=[plot1],tooltips=[('Pengguna Internet','@y')],mode='vline'))
plot2=p1.line(x,a,legend_label='Anomali Trafik (Juta Kasus)',color='red',line_width=2)
p1.add_tools(HoverTool(renderers=[plot2],tooltips=[('Anomali Trafik',"@y")],mode='vline'))
plot3=p1.line(x,e,legend_label='Transaksi E-Commerce (Triliun Rupiah)',color='blue',line_width=2)
p1.add_tools(HoverTool(renderers=[plot3],tooltips=[('Transaksi E-Commerce',"@y")],mode='vline'))
p1.legend.location="top_center"
st.bokeh_chart(p1,use_container_width=True)
st.caption('sumber data: BSSN, BPS, BI')

option = st.selectbox(
    '',
    ('Silakan Pilih','Korelasi Pengguna Internet VS Anomali Trafik',
    'Korelasi Nilai Transaksi E-Commerce VS Anomali Trafik', 'Tabel Data')
)

if (option =='Korelasi Pengguna Internet VS Anomali Trafik'):
    st.write('##### Korelasi Pengguna Internet VS Anomali Trafik')
    chart_data=pd.DataFrame(
    ([a[0],p[0]],[a[1],p[1]],[a[2],p[2]],[a[3],p[3]]),
    columns=['Anomali Trafik(Juta kasus)','Pengguna Internet(Juta orang)']
    )
    st.line_chart(chart_data)
    st.write('''Berdasarkan perhitungan korelasi Pearson, diketahui bahwa antara pengguna internet 
    dengan anomali trafik mempunyai korelasi (hubungan) positif yang kuat. Artinya meningkatnya pengguna 
    internet di Indonesia mempunyai pengaruh pada peningkatan anomali trafik internet di Indonesia.''')
    #korelasi 
    korelasi=np.corrcoef(p,a) #pengguna dan data anomali
    st.write(korelasi)
elif (option=='Korelasi Nilai Transaksi E-Commerce VS Anomali Trafik'):
    st.write('##### Korelasi Nilai Transaksi E-Commerce VS Anomali Trafik')
    chart_data1=pd.DataFrame(
    ([a[0],e[0]],[a[1],e[1]],[a[2],e[2]],[a[3],e[3]]),
    columns=['Anomali Trafik(Juta kasus)','Nilai Transaksi E-Commerce (Triliun Rupiah)']
    )
    st.line_chart(chart_data1)
    st.write('''Berdasarkan perhitungan korelasi Pearson, diketahui bahwa antara nilai transaksi *e-commerce* 
    dengan anomali trafik mempunyai korelasi (hubungan) positif yang kuat. Artinya meningkatnya nilai 
    transaksi yang berarti meningkatnya aktivitas *e-commerce* di Indonesia mempunyai pengaruh pada 
    peningkatan anomali trafik internet di Indonesia.''')
    #korelasi 
    korelasi1=np.corrcoef(e,a) #pengguna dan data anomali
    st.write(korelasi1) 
elif (option=='Tabel Data'):
    st.write('##### Data Anomali Trafik, Pengguna Internet dan Nilai Transaksi E-Commerce')
    df_data=df_data.set_index('Tahun')
    st.table(df_data)
    st.caption('sumber data: BSSN, BPS, BI')
else:
    st.write('')

#from sklearn.model_selection import train_test_split
df=pd.read_csv('https://raw.githubusercontent.com/ayume-gah/data/main/anomali%20bulanan.csv',delimiter=';')
#df

#top 10 anomali
st.subheader('Laporan Anomali Trafik Internet di Indonesia')
tahun_anomali=st.radio(
    'Laporan Anomali Trafik pada Tahun:',
    ('2022(Jan-Feb)','2021','2020','2019','2018')
)

if tahun_anomali == '2022(Jan-Feb)' :
    d_2022=np.array([68.8,9.5,7.3,6.6,3.8,3.2,0.8,0.1,0.03])
    l_2022=['MALWARE','EXPLOIT','TROJAN Activity','Information Leakeage',
    'Information Gathering','Other','Web Application Attack','APT',
    'Denial of Service']

    #pie chart cyber crime
    fig=plt.figure(figsize=(9,9))
    myexplode=[0.1,0,0,0,0,0,0,0,0]
    plt.pie(d_2022, labels=l_2022, autopct='%1.2f%%', explode=myexplode, startangle=90)
    plt.title('TOP Anomali Trafik di Tahun 2022 (Jan-Feb)')
    st.pyplot(fig)
elif tahun_anomali == '2021' :
    d_2021=np.array([46.6,4.3,3.5,3.3,3.1,3,2.9,1.6,1.2,30.5])
    #1.1,29.4])
    l_2021=['MyloBot','PROTOCOL-SCADA Moxa','MiningPool','Win.Trojan.ZeroAccess',
    'Discover Using Socks Agent','CVE-2017-0147','Win.Trojan.AllAple','RDP Account Brute Force',
    'Generic Trojan RAT','Lainnya']
    #'ISC BIND DoS Vulnerability','Lainnya']

    #pie chart cyber crime
    fig=plt.figure(figsize=(9,9))
    myexplode=[0.1,0,0,0,0,0,0,0,0,0]
    plt.pie(d_2021, labels=l_2021, autopct='%1.1f%%',explode=myexplode, startangle=90)
    plt.title('TOP Anomali Trafik di Tahun 2021')
    st.pyplot(fig)
elif tahun_anomali == '2020' :
    d_2020=np.array([14.6,11.9,4.9,2.7,2.1,1.7,1.6,1.5,1.4,57.6])
    l_2020=['Win.Trojan.AllAple','Win.Trojan.ZeroAccess','PROTOCOL-SCADA Moxa','Trojan.WillExec',
    'CVE-2017-11882','Generic Trojan','Win32/Gamarue','Mining Trojan','Trojan Glupteba','Lainnya']
    #'Cobalt Strike','Lainnya']

    #pie chart cyber crime
    fig=plt.figure(figsize=(9,9))
    myexplode=[0.1,0,0,0,0,0,0,0,0,0]
    plt.pie(d_2020, labels=l_2020, autopct='%1.1f%%',explode=myexplode, startangle=90)
    plt.title('TOP Anomali Trafik di Tahun 2020')
    st.pyplot(fig)
elif tahun_anomali == '2019' :
    d_2019=np.array([64,36])
    l_2019=['Serangan Lainnya','Serangan Malware']

    #pie chart cyber crime
    fig=plt.figure(figsize=(9,9))
    myexplode=[0,0.1]
    plt.pie(d_2019, labels=l_2019, autopct='%1.1f%%',explode=myexplode, startangle=90)
    plt.title('TOP Anomali Trafik di Tahun 2019')
    st.pyplot(fig)
elif tahun_anomali == '2018' :
    d_2019=np.array([34.6,16.1,10.5,38.8])
    l_2019=['Aktifitas Trojan','Percobaan Pengambil-alihan Akun User','Percobaan Serangan DoS','Lainnya']

    #pie chart cyber crime
    fig=plt.figure(figsize=(9,9))
    myexplode=[0.1,0,0,0]
    plt.pie(d_2019, labels=l_2019, autopct='%1.1f%%',explode=myexplode, startangle=90)
    plt.title('TOP Anomali Trafik di Tahun 2018')
    st.pyplot(fig)
else:
    st.write('')
st.caption('sumber data : Laporan Monitoring BSSN, Badan Siber dan Sandi Negara')
st.write('''Anomali trafik berupa ***Malware*** jenis *Botnet*, *Triton* dan aktivitas program
    ***MiningPool*** merupakan indikasi adanya kegiatan *phishing*. Karena ***Malware*** dan program 
    ***MiningPool*** sering disebarkan melalui *phising*, yang kemudian menggandakan atau mengambil data 
    pribadi korban untuk dimanfaatkan seperti :''')   
st.write('''> * Menjual data pribadi korban ke pihak ketiga yang membutuhkan data calon konsumen. Misal, untuk tujuan marketing.''')
st.write('''> * Menjual data pribadi korban untuk kepentingan politik.''')
st.write('''> * Menjalankan aksi penipuan. Misal, menyatakan korban telah memenangkan sebuah undian tertentu yang pada akhirnya meminta korban untuk mengirimkan sejumlah uang.''')
st.write('''> * Membobol akun yang dimiliki korban dengan menggunakan data pribadi korban tersebut.''')
st.write('''> * Melakukan pinjaman online dengan menggunakan data pribadi korban.''')
st.write('\n')
st.write('''Anomali trafik berupa ***Malware*** jenis *Trojan Horse*, sering disebarkan melalui teknik
*social engineering* untuk membajak/meretas perangkat korban.''')   

st.write('\n')

#data dan grafik kasus phishing
st.write('##### Laporan Aktivitas Phishing Domain .id')
st.write('''Laporan ini dikumpulkan oleh Indonesia Anti-phishing Data Exchange (IDADX)
dari hasil data APWG yang
dilaporkan oleh anggotanya di http://www.apwg.org, melalui email kiriman ke
reportphishing@antiphishing.org, data phishing dari Netcraft yang dikirimkan melalui email. 
Selain itu, IDADX juga mendapatkan
laporan dari anggotanya yang dilaporkan melalui situs web http://idadx.id dan menerima
laporan phishing dari masyarakat.''')

x=[1,2,3,4,5,6]
#x=['01-2022','02-2022','03-2022','04-2022','05-2022','06-2022']
y=[(1210+18+39),(994+23+39),(965+17+55),(2122+54+45),(1693+32+37),(1764+40+61)]
p=figure(
    title='Jumlah Kasus Phishing di Indonesia Pada Tahun 2022',
    x_axis_label='Bulan ke-',
    y_axis_label='Jumlah Kasus',
    tools=[HoverTool()],
    tooltips='@y kasus',
    width=250,
    height=250
)
p.line(x,y,legend_label='Kasus Phishing',color='red',line_width=2)
st.bokeh_chart(p,use_container_width=True)
st.caption('sumber data : Laporan Aktivitas Phishing Domain .id, Indonesia Anti-phishing Data Exchange')

