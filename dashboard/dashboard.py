

import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from IPython.display import Markdown

bike_day_cleaned = pd.read_csv('https://raw.githubusercontent.com/FadhilBangkit/submission/refs/heads/main/dashboard/main_data_1.csv')
bike_hour_cleaned = pd.read_csv('https://raw.githubusercontent.com/FadhilBangkit/submission/refs/heads/main/dashboard/main_data_2.csv')


relevant_columns_day = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'cnt']
relevant_columns_hour = ['season', 'yr', 'mnth', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'cnt']


bike_day_df_relevant_q1 = bike_day_cleaned[relevant_columns_day]
bike_hour_df_relevant_q1 = bike_hour_cleaned[relevant_columns_hour]

correlation_day = bike_day_df_relevant_q1.corr()['cnt'].sort_values(ascending=False)
correlation_hour = bike_hour_df_relevant_q1.corr()['cnt'].sort_values(ascending=False)

total_registered_users = bike_day_cleaned['registered'].sum()
total_casual_users = bike_day_cleaned['casual'].sum()

total_registered_users_hour = bike_hour_cleaned['registered'].sum()
total_casual_users_hour = bike_hour_cleaned['casual'].sum()

labels_day = ['Registered Users', 'Casual Users']
sizes_day = [total_registered_users, total_casual_users]
colors_day = ['#66b3ff', '#99ff99']

labels_hour = ['Registered Users', 'Casual Users']
sizes_hour = [total_registered_users_hour, total_casual_users_hour]
colors_hour = ['#66b3ff', '#99ff99']


with st.sidebar:
    st.title('Proyek Dicoding Belajar analisis data dengan Python')
    st.image('data:image/png;base64,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')
    st.image('data:image/png;base64,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')
    st.markdown("""
    - Nama: Muhammad Fadhil Syahputra
    - Email: m247b4ky2802@bangkit.academy
    - ID Dicoding: fadhil_syahputra_HKuX
    """)
    dataset_choice = st.selectbox(
    "Pilih dataset yang ingin ditampilkan:",
    ['Data Harian', 'Data Per Jam']
)

if dataset_choice == 'Data Harian':

  # Teks Pembuka
  st.title('Hasil Analisis data Bike rental (Dataset Harian)')
  st.markdown(
    """
    # Pertanyaan 1
    *Faktor Terbesar Apa yang mempengaruhi jumlah pelanggan yang menyewa sepeda?*
    """
  )
  st.markdown("""
    <style>
    .text-box {
        width: 100%; /* Anda bisa menyesuaikan persentasenya */
        margin: auto;
        text-align: justify;
    }
    </style>

    <div class="text-box">
    Analisis korelasi adalah salah satu metode statistik yang digunakan untuk memahami hubungan antara dua atau lebih variabel. Dalam konteks penyewaan sepeda, analisis ini dapat membantu mengidentifikasi faktor-faktor yang paling mempengaruhi jumlah pelanggan yang menyewa sepeda. Dengan menganalisis data yang relevan, seperti kondisi cuaca, waktu penyewaan, demografi pengguna, dan faktor ekonomi, kita dapat mengeksplorasi hubungan antara variabel-variabel ini dan jumlah penyewa. 
    </div>
    """, unsafe_allow_html=True)
  st.markdown(
    """
    ## 1. Suhu yang dirasakan (atemp)
    """
  )
  st.text('\n')

  #Menampilkan Grafik Yang berkaitan
  a= plt.figure(figsize=(8, 6))
  sns.regplot(x='atemp', y='cnt', data=bike_day_df_relevant_q1, scatter_kws={"color": "#FF4500",'alpha':0.5, 's':20}, line_kws={"color": "#8B0000"})
  plt.title('Korelasi antara Suhu yang Dirasakan (atemp) dan Jumlah Pengguna (cnt)')
  plt.xlabel('Suhu yang Dirasakan (atemp)')
  plt.ylabel('Jumlah Pengguna (cnt)')
  plt.show()
  st.pyplot(a)
  st.markdown("""
    <style>
    .text-box {
        width: 100%; /* Anda bisa menyesuaikan persentasenya */
        margin: auto;
        text-align: justify;
    }
    </style>

    <div class="text-box">
    Grafik di atas adalah grafik scatterplot yang menunjukkan hubungan korelasi antara jumlah pengguna sepeda dengan suhu yang dirasakan (atemp). Grafik ini dilengkapi dengan garis regresi yang memiliki kemiringan positif, menunjukkan bahwa terdapat hubungan positif antara suhu yang dirasakan dan jumlah pengguna sepeda. Ketika suhu meningkat, semakin banyak orang yang cenderung ingin bersepeda. Oleh karena itu, grafik ini memberikan wawasan penting bagi perusahaan dalam menyiapkan sumber daya sepeda pada saat suhu meningkat, seperti selama musim panas, untuk memenuhi permintaan yang lebih tinggi dari pelanggan.
    </div>
    """, unsafe_allow_html=True)
  st.markdown(
    """
    ## 2. Suhu lingkungan (temp)
    """
    
  )
  b= plt.figure(figsize=(8, 6))
  plt.hexbin(x='temp', y='cnt', data=bike_day_df_relevant_q1, gridsize=30, cmap='Reds', mincnt=1)
  plt.colorbar(label='Jumlah Titik Data')
  plt.title('Korelasi antara Suhu (temp) dan Jumlah Pengguna (cnt)')
  plt.xlabel('Suhu (temp)')
  plt.ylabel('Jumlah Pengguna (cnt)')
  plt.show()
  st.pyplot(b)

  #Teks Penjelasan
  st.markdown("""
    <style>
    .text-box {
        width: 100%; /* Anda bisa menyesuaikan persentasenya */
        margin: auto;
        text-align: justify;
    }
    </style>

    <div class="text-box">
    Ternyata bukan hanya suhu yang dirasakan, tetapi suhu lingkungan juga berkorelasi positif terhadap jumlah pengguna. Dari kedua data di atas, dapat disimpulkan bahwa suhu merupakan faktor terbesar yang mempengaruhi keputusan orang untuk bersepeda. Ketika suhu meningkat, baik suhu yang dirasakan maupun suhu lingkungan, semakin banyak orang cenderung memilih bersepeda sebagai aktivitas mereka. Hal ini memberikan wawasan penting bagi pengelola layanan penyewaan sepeda untuk mengantisipasi permintaan pada hari-hari yang lebih hangat. Hal ini bersesuaian dengan nilai korelasi yang sudah didapat, yang menunjukkan hubungan signifikan antara suhu dan jumlah pengguna.
    </div>
    """, unsafe_allow_html=True)
  st.text('')
  st.write(bike_day_df_relevant_q1.corr()['cnt'].sort_values(ascending=False))
  st.markdown("""
  *Nilai atempt dan temp memiliki nilai tertinggi dalam korelasi*
  """)


  #Teks Pembuka pertanyaan kedua
  st.markdown(
    """
    # Pertanyaan 2
    *Faktor Terbesar Apa yang mempengaruhi jumlah pelanggan yang menyewa sepeda?*
    Seberapa banyak Registered user dan casual user?
    """
  )
  st.markdown("""
    <style>
    .text-box {
        width: 100%; /* Anda bisa menyesuaikan persentasenya */
        margin: auto;
        text-align: justify;
    }
    </style>
  
    <div class="text-box">
    Jumlah pengguna terdaftar dan jumlah pengguna casual sangatlah penting bagi perusahaan untuk mengukur seberapa jauh performa pemasaran perusahaan dalam menarik pelanggan agar beralih menjadi pengguna terdaftar. Analisis terhadap kedua kategori pengguna ini memberikan wawasan berharga tentang efektivitas strategi pemasaran yang diterapkan dan membantu perusahaan dalam merumuskan langkah-langkah yang lebih efektif untuk meningkatkan jumlah pengguna terdaftar. Dengan memahami perbandingan antara pengguna terdaftar dan pengguna casual, perusahaan dapat mengidentifikasi area yang perlu ditingkatkan dan mengoptimalkan kampanye pemasaran untuk mencapai tujuan bisnisnya.
    </div>
    """, unsafe_allow_html=True)

  #Grafik Pie
  st.markdown(
    """
    ## Grafik Pie Chart
    """
  )


  c= plt.figure(figsize=(8, 8))
  plt.pie(sizes_day, labels=labels_day, colors=colors_day, autopct='%1.1f%%', startangle=90)
  plt.title('Proporsi Registered dan Casual Users (Data Harian)')
  plt.show()
  st.pyplot(c)

  #Grafik Bar
  st.markdown(
    """
    ## Grafik Bar Chart
    """
  )
  d=plt.figure(figsize=(8, 6))
  plt.bar(labels_day, sizes_day, color=['#66b3ff', '#99ff99'])
  plt.title('Jumlah Registered dan Casual Users (Data Harian)')
  plt.ylabel('Jumlah Pengguna')
  plt.show()
  st.pyplot(d)

  #Kesimpulan
  st.title('Kesimpulan')
  st.markdown("""
  - Jumlah pengguna pada dataset harian sangat erat kaitannya dengan nilai suhu yang dirasakan
  (Korelasi Positif)
  - Mayoritas pengguna sepeda merupakan pengguna yang terdaftar
  """)

elif dataset_choice == 'Data Per Jam':

  # Teks Pembuka
  st.title('Hasil Analisis data Bike rental (Dataset Per-jam)')
  st.markdown(
    """
    # Pertanyaan 1
    *Faktor Terbesar Apa yang mempengaruhi jumlah pelanggan yang menyewa sepeda?*
    """
  )
  st.markdown("""
    <style>
    .text-box {
        width: 100%; /* Anda bisa menyesuaikan persentasenya */
        margin: auto;
        text-align: justify;
    }
    </style>

    <div class="text-box">
    Analisis korelasi merupakan metode statistik yang digunakan untuk memahami hubungan antara dua atau lebih variabel. Dalam konteks penyewaan sepeda, analisis ini dapat membantu dalam mengidentifikasi faktor-faktor yang paling berpengaruh terhadap jumlah pelanggan yang menyewa sepeda. Dengan menganalisis data yang relevan, seperti kondisi cuaca, waktu penyewaan, demografi pengguna, serta faktor ekonomi, kita dapat menjelajahi hubungan antara variabel-variabel tersebut dan jumlah penyewa.
    </div>
    """, unsafe_allow_html=True)
  st.markdown(
    """
    ## 1. Grafik Korelasi Jam dan Jumlah Pengguna
    """
  )
  st.text('\n')

  #Menampilkan Grafik Yang berkaitan
  e= plt.figure(figsize=(12, 6))
  sns.lineplot(x='hr', y='cnt', data=bike_hour_df_relevant_q1)
  plt.title('Korelasi antara Jam (hr) dan Jumlah Pengguna (cnt)')
  plt.xlabel('Jam (hr)')
  plt.ylabel('Jumlah Pengguna (cnt)')
  plt.show()
  st.pyplot(e)

  
  st.markdown("""
    <style>
    .text-box {
        width: 100%; /* Anda bisa menyesuaikan persentasenya */
        margin: auto;
        text-align: justify;
    }
    </style>

    <div class="text-box">
    Dari data di atas, terlihat dua puncak penggunaan sepeda yang menunjukkan bahwa pengguna cenderung bersepeda pada jam pagi dan jam sore hari. Puncak pertama terjadi di pagi hari, ketika banyak orang berangkat kerja atau melakukan aktivitas sehari-hari, sementara puncak kedua terjadi di sore hari, saat orang-orang pulang dari pekerjaan atau kegiatan lainnya. Dengan mengetahui jam-jam sibuk ini, perusahaan dapat merencanakan strategi yang lebih baik untuk memenuhi permintaan penyewaan sepeda, seperti meningkatkan ketersediaan sepeda dan sumber daya pada waktu-waktu tersebut. Hal ini memungkinkan perusahaan untuk mengoptimalkan layanan mereka dan memastikan kepuasan pelanggan.
    </div>
    """, unsafe_allow_html=True)
  st.markdown(
    """
    ## 2. Suhu yang dirasakan (atemp)
    """
    
  )
  f= plt.figure(figsize=(8, 6))
  sns.regplot(x='atemp', y='cnt', data=bike_hour_df_relevant_q1,
              scatter_kws={"color": "#FF4500", 'alpha':0.3, 's':10},
              line_kws={"color": "#8B0000"})
  plt.title('Korelasi antara Suhu yang Dirasakan (atemp) dan Jumlah Pengguna (cnt)')
  plt.xlabel('Suhu yang Dirasakan (atemp)')
  plt.ylabel('Jumlah Pengguna (cnt)')
  plt.show()
  st.pyplot(f)

  #Teks Penjelasan
  st.markdown("""
    <style>
    .text-box {
        width: 100%; /* Anda bisa menyesuaikan persentasenya */
        margin: auto;
        text-align: justify;
    }
    </style>

    <div class="text-box">
    Seperti halnya suhu pada dataset harian, suhu pada dataset per jam (atemp) juga menunjukkan korelasi positif terhadap jumlah pengguna sepeda. Namun, nilai korelasinya lebih rendah dibandingkan dengan yang ditemukan dalam dataset harian. Hal ini menunjukkan bahwa meskipun suhu tetap berpengaruh terhadap keputusan orang untuk bersepeda, fluktuasi suhu yang lebih sering dalam konteks per jam mungkin mengurangi kekuatan hubungan ini. Dengan kata lain, faktor-faktor lain seperti waktu dalam hari, aktivitas yang dilakukan, atau kondisi cuaca juga dapat memainkan peran penting dalam memengaruhi jumlah pengguna sepeda pada tingkat jam.
    </div>
    """, unsafe_allow_html=True)
  st.text('')
  st.write(bike_hour_df_relevant_q1.corr()['cnt'].sort_values(ascending=False))
  st.markdown("""
  *Nilai jam hr merupakan nilai tertinggi dan atemp pada urutan ketiga*
  """)


  #Teks Pembuka pertanyaan kedua
  st.markdown(
    """
    # Pertanyaan 2
    *Faktor Terbesar Apa yang mempengaruhi jumlah pelanggan yang menyewa sepeda?*
    Seberapa banyak Registered user dan casual user?
    """
  )
  st.markdown("""
    <style>
    .text-box {
        width: 100%; /* Anda bisa menyesuaikan persentasenya */
        margin: auto;
        text-align: justify;
    }
    </style>
  
    <div class="text-box">
    Jumlah pengguna terdaftar dan pengguna casual merupakan aspek yang sangat penting bagi perusahaan dalam mengevaluasi sejauh mana efektivitas pemasaran dalam menarik pelanggan untuk beralih menjadi pengguna terdaftar. Melalui analisis terhadap kedua kategori pengguna ini, perusahaan memperoleh wawasan yang berharga mengenai keberhasilan strategi pemasaran yang telah diterapkan. Ini membantu perusahaan merumuskan langkah-langkah yang lebih efektif untuk meningkatkan jumlah pengguna terdaftar. Dengan memahami perbandingan antara pengguna terdaftar dan pengguna casual, perusahaan dapat mengidentifikasi area yang perlu diperbaiki serta mengoptimalkan kampanye pemasaran untuk mencapai tujuan bisnis yang diinginkan.
    </div>
    """, unsafe_allow_html=True)

  #Grafik Pie
  st.markdown(
    """
    ## Grafik Pie Chart
    """
  )


  g = plt.figure(figsize=(8, 8))
  plt.pie(sizes_hour, labels=labels_hour, colors=colors_hour, autopct='%1.1f%%', startangle=90)
  plt.title('Proporsi Registered dan Casual Users (Data Per Jam)')
  plt.show()
  st.pyplot(g)

  #Grafik Bar
  st.markdown(
    """
    ## Grafik Bar Chart
    """
  )
  h = plt.figure(figsize=(8, 6))
  plt.bar(labels_hour, sizes_hour, color=['#66b3ff', '#99ff99'])
  plt.title('Jumlah Registered dan Casual Users (Data Per Jam)')
  plt.ylabel('Jumlah Pengguna')
  plt.show()
  st.pyplot(h)
  
  #Kesimpulan
  st.title('Kesimpulan')
  st.markdown("""
  - Berbeda dengan dataset harian pada dataset per jam banyaknya jumlah pesepeda tergantung dengan waktu pada rentang hari tersebut
  - Mayoritas pengguna pada data set per jam juga merupakan pengguna terdaftar
  """)


  






