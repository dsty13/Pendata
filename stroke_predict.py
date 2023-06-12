import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
st.title("Brain Stroke Prediction")
st.write('Merupakan aplikasi untuk memprediksi apakah kita beresiko terkena stroke atau tidak')
selected = option_menu(
    menu_title=None,
    options=['Data','Preprocessing','Modelling','Implementasi','Profile'],
    orientation='horizontal',
    menu_icon=None,
    default_index=0,
    styles={
    "nav-link":{
        "font-size":"12px",
        "text-align":"center",
        "margin":"3px",
        "padding":"5px",
        "--hover-color":"#ff000000",},
    "nav-link-selected":{
        "background-color":"blue"},
    }
)


if selected == 'Data':
    st.title("Dataset Brain Stroke")
    st.write('Data yang digunakan yaitu dataset Brain Stroke yang saya peroleh dari kaggle')
    st.write('Dataset Brain Stroke dapat diakses pada link : https://www.kaggle.com/datasets/jillanisofttech/brain-stroke-dataset')
    data = pd.read_csv('https://raw.githubusercontent.com/dsty13/dataset/main/brain_stroke.csv')
    data
    st.write('Tipe data yang yang digunakan pada dataset brain stroke adalah numerik dan kategorikal dengan jumlah 11 kolom dimana 10 kolom merupakan fitur dan 1 kolom merupakan label')
    st.write('Berikut Merupakan Informasi Atribut yang ada dalam dataset Brain Stroke :')
    st.write('1. gender: Male, Female')
    st.write('2. age: usia pasien')
    st.write('3. hypertension:0 jika pasien tidak menderita hipertensi, 1 jika pasien menderita hipertensi')
    st.write('4. heart_disease:0 jika pasien tidak memiliki penyakit jantung, 1 jika pasien memiliki penyakit jantung ')
    st.write('5. ever_married: Ya atau Tidak')
    st.write('6. worktype: anak-anak, Pemerintah, Tidak pernah bekerja, Swasta , Wiraswasta')
    st.write('7. Residence_type: Desa atau Kota')
    st.write('8. avg_glucose_level: kadar glukosa rata-rata dalam darah')
    st.write('9. bmi: indeks massa tubuh')
    st.write('10. smoking_status: pernah merokok, tidak pernah merokok, merokok dan Tidak diketahui')
    st.write('11. stroke: 1 jika pasien mengalami stroke atau 0 jika tidak')
    
    
if selected == 'Preprocessing':
    st.title("Tahapan Preprocessing")
    st.write("Tahapan Preprocessing yang dilakukan yaitu mengubah data kategorical menjadi Numerik dan Melakukan Normalisasi Min-Max")
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.preprocessing import LabelEncoder
    data = pd.read_csv('https://raw.githubusercontent.com/dsty13/dataset/main/brain_stroke.csv')
    
    st.title("Label Encoder")
    st.write('Preprocessing Mengubah Data Kategorical menjadi Numerik')
    kolom = ['gender','ever_married','work_type','Residence_type','smoking_status']
    encoder = LabelEncoder()
    for k in kolom :
        data[k]=encoder.fit_transform(data[k])
    data 
    
    st.title("Min-Max Scalar")
    st.write('Preprocessing Menggunakan Min-Max Scalar')
    k_minmax=['age','avg_glucose_level','bmi']
    scaler_minmax = MinMaxScaler()
    data[k_minmax] = scaler_minmax.fit_transform(data[k_minmax])
    data
        
    
    
if selected == 'Modelling':
    st.title("Berikut Merupakan Tahapan Model")
    st.write("Model yang digunakan yaitu model Decision Tree, Naive Bayes, KNN, ANN")
    radio = st.radio(
        "Pilih Model:",
        ('Decision Tree', 'Naive Bayes','KNN', 'ANN'))
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.naive_bayes import GaussianNB
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.neural_network import MLPClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    
    df = pd.read_csv('https://raw.githubusercontent.com/dsty13/dataset/main/stroke_minmax.csv')
    
    X = df.drop(['stroke'], axis=1)
    y = df['stroke']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21)
    if radio=='Decision Tree':
        clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
        clf_gini.fit(X_train, y_train)
        y_pred_gini = clf_gini.predict(X_test)
        st.write('Akurasi Model Decision Tree:' ,(accuracy_score(y_test, y_pred_gini)))
        df= pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred_gini})
        df
    if radio=='Naive Bayes':
        classifier = GaussianNB()
        classifier.fit(X_train, y_train)
        y_pred_nb = classifier.predict(X_test) 
        st.write("Akurasi Model Naive Bayes : ", accuracy_score(y_test, y_pred_nb))
        df= pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred_nb})
        df
    if radio=='KNN':
        knn = KNeighborsClassifier(n_neighbors= 11, metric = "euclidean")
        knn.fit(X_train, y_train)
        y_pred_knn = knn.predict(X_test)
        knn_accuracy = accuracy_score(y_test,y_pred_knn)
        st.write("Akurasi Model KNN:", knn_accuracy)
        df= pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred_knn})
        df
    if radio=='ANN': 
        clf = MLPClassifier(hidden_layer_sizes=(100,100,100), max_iter=1000, alpha=0.0001,
                     solver='sgd', verbose=10,  random_state=21,tol=0.001)
        clf.fit(X_train, y_train)
        y_pred_ann=clf.predict(X_test) 
        accuracy_score(y_test, y_pred_ann) 
        st.write("Akurasi Model ANN:", accuracy_score(y_test, y_pred_ann))
        df = pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred_ann})
        df
if selected == 'Implementasi':
    st.title('Ayo Cek Apakah Anda Beresiko Terkena Stroke')
    img = Image.open('stroke.png')
    st.image(img)
    st.write('Isilah Form berikut untuk mengetahui apakah Anda beresiko terkena Stroke atau Tidak')
    col1,col2=st.columns(2)
    with col1:
        list_gender = ['silahkan pilih','male','female']
        gender = st.selectbox('Jenis kelamin :',list_gender)
        if gender=='male':
            gender=1
        if gender=='female':
            gender=0
        age = st.number_input('Usia Anda :')
        list_tensi = ['silahkan pilih','Iya','Tidak']
        hypertension = st.selectbox('Apakah Anda Memiliki Hipertensi? ',list_tensi)
        if hypertension =='Iya':
            hypertension=1
        if hypertension =='Tidak':
            hypertension=0
        list_hd = ['silahkan pilih','Iya','Tidak']
        heart_disease = st.selectbox('Apakah Anda Memiliki Penyakit Jantung? ',list_hd)
        if heart_disease =='Iya':
            heart_disease=1
        if heart_disease =='Tidak':
            heart_disease=0
        list_em = ['silahkan pilih','Iya','Tidak']
        ever_married = st.selectbox('Apakah Anda Sudah Menikah? ',list_em)
        if ever_married =='Iya':
            ever_married=1
        if ever_married =='Tidak':
            ever_married=0
        
    with col2:
        list_wk = ['silahkan pilih','Anak-anak','PNS','Swasta','Wiraswasta','Tidak Bekerja']
        work_type = st.selectbox('Apakah Pekerjaan Anda? ',list_wk)
        if work_type =='Anak-anak':
            work_type=3
        if work_type=='PNS':
            work_type=0
        if work_type =='Swasta':
            work_type=1
        if work_type=='Wiraswasta':
            work_type=2
        if work_type=='Tidak Bekerja':
            work_type=4
        list_Rt= ['silahkan pilih','Desa','Kota']
        Residence_type = st.selectbox('Pilih Daerah Tempat Tinggal Anda ',list_Rt)
        if Residence_type=='Desa':
            Residence_type=0
        if Residence_type=='Kota':
            Residence_type=1
        avg_glucose_level = st.number_input('Rata-rata Kadar Glukosa Anda  :')
        bmi = st.number_input('Indeks Massa Tubuh Anda :')
        list_ss = ['silahkan pilih','Pernah Merokok','Tidak Pernah Merokok','Merokok','Tidak Diketahui']
        smoking_status = st.selectbox('Apakah Anda Merokok? ',list_ss)
        if smoking_status=='Pernah Merokok':
            smoking_status=1
        if smoking_status =='Tidak Pernah Merokok':
            smoking_status=2
        if smoking_status=='Merokok':
            smoking_status=3
        if smoking_status=='Tidak Diketahui':
            smoking_status=0
    
 
    button = st.button('Cek Prediksi Stroke',use_container_width = 500, type='primary')
    if button:
        if gender !='silahkan pilih' and age !=0 and hypertension !='silahkan pilih' and heart_disease!='silahkan pilih' and ever_married!='silahkan pilih' and  work_type!='silahkan pilih' and Residence_type!='silahkan pilih' and avg_glucose_level!=0 and bmi!=0 and smoking_status !='silahkan pilih':
            age=((age-0.08)/(82-0.08))*(1-0)+0
            avg_glucose_level=((avg_glucose_level-55.12)/(271.74-55.12))*(1-0)+0
            bmi=((bmi-14)/(48.9-14))*(1-0)+0
            #st.write(age,avg_glucose_level,bmi)
            #st.write(gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status)
            import pickle
            with open ('knn_stroke.pkl','rb') as read:
                knn=pickle.load(read)
            cek=knn.predict([[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status ]])
            if cek==0:
                st.write('Anda Tidak Beresiko terkena Stroke')
            else:
                st.write('Anda Beresiko terkena Stroke')
        else:
            st.write('KOLOM BELUM TERISI')
if selected =='Profile':
    st.title('My Biodata')   
    st.write('Nama : Desti Fitrotun Nisa')
    st.write('Nim : 210411100182')
    st.write('Kelas : Penambangan Data B')


       














