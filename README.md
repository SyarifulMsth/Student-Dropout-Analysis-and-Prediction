


# # Students' Performance Analysis
Data Science Project: Students Dropout and Academic Success

![Image](https://images.unsplash.com/photo-1456406644174-8ddd4cd52a06?q=80&w=1468&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

## 🏷️Metodologi 

Metodologi manajemen proyek yang digunakan dalam proyek ini adalah CRISP-DM. Metodologi ini merupakan salah satu dari beberapa metodologi yang sering digunakan dalam dunia industri. Selain CRISP-DM, terdapat beberapa metodologi manajemen proyek yaitu Ad Hoc, Waterfall, Agile Scrum & Kanban.

CRISP-DM (Cross-Industry Standard Process for Data Mining) adalah pendekatan yang menggambarkan proses standar untuk proyek data mining, data science, dan machine learning. Dalam metodologi ini, pengerjaan suatu proyek diawali dengan tahap business understanding sehingga dapat membantu memastikan proyek terlaksana sesuai dengan kebutuhan bisnis. Keunggulan lain dari metodologi ini adalah proses kerjanya bersifat iteratif, sehingga proses kerjanya dapat disesuaikan dengan kebutuhan eksperimen proyek data science. Berbeda dengan metodologi waterfall yang hanya berjalan satu arah.

CRISP-DM terdiri dari 6 fase dan disusun sebagai sebuah siklus, yang bertujuan untuk memaksimalkan hasil proyek ilmu data. Tahapan CRISP-DM dapat dilihat pada gambar berikut:

![CRISP-DM](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/academy/dos:418b0f7f4b2dc3d25a68e4f10cca803820230908164632.jpeg)


## 🧭Business Understanding 
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias  _dropout_. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. 

### Business Problems
Untuk mencegah permasalahan Jaya Jaya Institute menjadi lebih parah. Maka perlu diidentifikasi faktor apa saja yang berpengaruh terhadap tingkat dropout yang tinggi dan mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout, sehingga dapat diberi bimbingan khusus. 

### Project Scope
Berdasarkan permasalahan yang telah diuraikan, maka untuk menjawab permasalahan bisnis tersebut akan dibuat sistem machine learning dengan menggunakan algoritma Random Forest Classification. Sehingga dapat diidentifikasi faktor-faktor yang berkontribusi terhadap tingginya tingkat dropout pada Jaya Jaya Jaya Institute.

Selain itu juga akan dibuat business dashboard yang dapat digunakan oleh Jaya Jaya Institute untuk membantu memantau data dan memonitor performa siswa.

Berikut beberapa pertanyaan yang akan dijawab dalam proyek ini dengan mengikuti konsep SMART-Question:
### SMART Question (Specific - Measurable - Action oriented - relevant - Time bond) :
- **Specific :** Faktor-faktor apa saja yang berkontribusi terhadap tingkat dropout Jaya Jaya Jaya Institute?
- **Measurable :** Berapa jumlah atau persentase faktor yang mempengaruhi tingkat dropout Jaya Jaya Jaya Institute?
- **Action oriented:** Tindakan apa yang dapat dilakukan Jaya Jaya Jaya Institute untuk menangani faktor penyebab siswa dropout dan mengurangi tingkat dropout?
- **Relevant :** Apakah tindakan yang akan dilakukan tersebut dapat mengurangi jumlah siswa yang dropout?
- **Time bond :** Berapa lama implementasi dari rencana untuk mengurangi jumlah siswa yang dropout tersebut? 

### Project Preparation 
1. **Dataset** 
Proyek Data Science ini menggunakan [Dataset Predict Students' Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

2. **Tech Stack** 	
	 - **Programming Languages** : Python
	- **AI/ML** : Tensorflow, pandas, numpy, scikit-learn, SciPy, matplotlib, seaborn, sqlalchemy, psycopg2-binary, joblib
	- **Database** : PostreSQL
	- **Devops** : Docker image with Metabase
	- **Other** : Git

3. **Setup Environment** 

    **Library**
    
	`pip install numpy pandas scipy matplotlib seaborn jupyter sqlalchemy psycopg2-binary scikit-learn==1.2.2 joblib==1.3.1`
    
    **Metabase** <br>
    username :  
    password : 

## 📚 Data Understanding 
Dataset yang digunakan pada proyek data science ini adalah [Dataset Predict Students' Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success). Dataset tersebut terdiri dari 4424 records data dan 37 features.

| Column Name                        | Description                                                                                                                                                  |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Marital status                     | The marital status of the student. (Categorical)                                                                                                            |
| Application mode                   | The method of application used by the student. (Categorical)                                                                                                |
| Application order                  | The order in which the student applied. (Numerical)                                                                                                         |
| Course                             | The course taken by the student. (Categorical)                                                                                                              |
| Daytime/evening attendance         | Whether the student attends classes during the day or in the evening. (Categorical)                                                                          |
| Previous qualification             | The qualification obtained by the student before enrolling in higher education. (Categorical)                                                               |
| Nationality                        | The nationality of the student. (Categorical)                                                                                                               |
| Mother's qualification             | The qualification of the student's mother. (Categorical)                                                                                                    |
| Father's qualification             | The qualification of the student's father. (Categorical)                                                                                                    |
| Mother's occupation                | The occupation of the student's mother. (Categorical)                                                                                                       |
| Father's occupation                | The occupation of the student's father. (Categorical)                                                                                                       |
| Displaced                          | Whether the student is a displaced person. (Categorical)                                                                                                     |
| Educational special needs          | Whether the student has any special educational needs. (Categorical)                                                                                        |
| Debtor                             | Whether the student is a debtor. (Categorical)                                                                                                              |
| Tuition fees up to date            | Whether the student's tuition fees are up to date. (Categorical)                                                                                            |
| Gender                             | The gender of the student. (Categorical)                                                                                                                    |
| Scholarship holder                 | Whether the student is a scholarship holder. (Categorical)                                                                                                  |
| Age at enrollment                  | The age of the student at the time of enrollment. (Numerical)                                                                                               |
| International                      | Whether the student is an international student. (Categorical)                                                                                              |
| Curricular units 1st sem (credited) | The number of curricular units credited by the student in the first semester. (Numerical)                                                                 |
| Curricular units 1st sem (enrolled) | The number of curricular units enrolled by the student in the first semester. (Numerical)                                                                 |
| Curricular units 1st sem (evaluations) | The number of curricular units evaluated by the student in the first semester. (Numerical)                                                               |
| Curricular units 1st sem (approved) | The number of curricular units approved by the student in the first semester. (Numerical)                                                                 |


## 📚 Data Preparation 

Tahapan Data preparation mencakup proses data gathering, data assessing, data cleaning, atau feature engineering. Dalam proyek ini dilakukan beberapa teknik seperti penanganan missing value, penanganan duplikasi data, dan beberapa teknik lainnya.

**Jelaskan lebih lanjut seperti documentation Machine learning projects**

## 🎯 Modeling 
Pada proyek ini algoritma machine learning yang digunakan yaitu Random Forest Classification.

![image](https://miro.medium.com/v2/resize:fit:1200/1*DvgOxmBc30t9HjDKFYLC0g.jpeg)

Algoritma random forest merupakan salah satu algoritma machine learning yang dapat digunakan untuk menyelesaikan masalah klasifikasi dan regresi. Random forest merupakan algoritma yang sering digunakan karena cukup sederhana namun memiliki stabilitas yang baik.

_Random forest_  termasuk dalam salah satu kategori  _ensemble_  (group)  _learning_, yang terdiri dari banyak pohon keputusan (_decision_  _tree_) yang bekerja bersama untuk meningkatkan kinerja dan akurasi prediksi. Pada model  _machine learning ensemble_, setiap model harus membuat prediksi secara independen. Kemudian, prediksi dari setiap  _model ensemble_  ini digabungkan untuk membuat prediksi akhir.  _Algoritma Random Forest_  mengkombinasikan hasil prediksi dari berbagai  _model decision tree_  yang dibuat secara acak.

**Kelebihan**  :

-   _Random forest_  merupakan algoritma yang sering digunakan karena cukup sederhana tetapi memiliki stabilitas yang mumpuni.
-   Random forest dapat mencegah terjadinya  _overfitting_  apabila dibandingkan dengan  _algoritma Decision Tree_. Selain itu, algoritma ini dapat menangani dataset besar dengan banyak fitur.

**Kekurangan**  :

-   _Random Forest_  memerlukan waktu pelatihan yang lebih lama dibanding  _Decision Tree_  karena kompleksitas modelnya

## 🔁Evaluation
Tahapan evaluasi model merupakan langkah penting dalam data science. Evaluasi model dapat membantu untuk mengetahui mengetahui seberapa baik model dalam memberikan hasil prediksi yang tepat.

Pada proyek  _machine learning_  ini evaluasi model akan menggunakan  _confussion matrix_.  _Confussion matrix_  memberi gambaran bagaimana performa model pada berbagai kelas. Ia menunjukkan berapa banyak jumlah prediksi yang benar (_True_) dan salah (_False_) untuk setiap label.

Dengan menggunakan  _confussion matrix_, maka dapat diketahui seberapa baik performa dari model  _machine learning_  yang dikembangkan. Hasil dari  _confussion matrix_  ini akan digunakan untuk menghitung berbagai metrik lainnya, seperti  _accuracy_,  _precision_,  _recall_, dan  _F-1 score_.

| Metric    | Definition                                                                                   |
|-----------|----------------------------------------------------------------------------------------------|
| **Accuracy** | Metrik evaluasi yang mengukur seberapa baik model membuat prediksi yang benar dari total prediksi yang dilakukan.                         |
| **Precision**| Metrik evaluasi yang digunakan untuk mengukur berapa banyak model menghasilkan prediksi yang benar untuk suatu kelas tertentu. Precision didefinisikan sebagai perbandingan antara jumlah hasil prediksi yang benar untuk kelas tertentu dengan jumlah total prediksi untuk kelas tersebut.              |
| **Recall**  | Metrik yang digunakan untuk mengukur seberapa baik model dalam memprediksi suatu kelas tertentu. Recall didefinisikan sebagai perbandingan antara jumlah hasil prediksi yang benar untuk kelas tertentu dengan jumlah total sampel pada kelas tersebut. |
|**F1-score**| Merupakan kombinasi antara nilai  _precision_  dan  _recall_  dari suatu kelas tertentu.|

## Machine Learning Deployment
 Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

## ⚔️ Business Dashboard 
Berikut merupakan beberapa tahapan yang umum dijumpai dalam pengembangan sebuah business dashboard.

1.  **Define**  
    Pada tahap awal tentunya kita perlu memahami audiens dari dashboard yang akan dibuat. Selain itu, kita juga perlu menentukan tujuan atau keluaran dari dashboard tersebut serta pertanyaan bisnis yang ingin dijawab melalui visualisasi data.  
      
    
2.  **Gather Data**  
    Tahap berikutnya adalah menentukan atau mengumpulkan data yang akan digunakan untuk menjawab pertanyaan bisnis. Pada tahap ini, kita perlu mempertimbangkan sumber dan kualitas data yang akan digunakan.  
      
    
3.  **Prototype**  
    Setelah mengetahui tujuan dan data yang akan digunakan, tahap selanjutnya adalah membuat prototipe/sketsa/mockup dari dashboard yang akan dibuat. Hal ini akan membantu Anda dalam membuat susunan dashboard yang baik dan efektif. Pada prosesnya, Anda perlu mempertimbangkan ukuran tampilan serta penggunaan sweet spot yang tepat.  
      
    
4.  **Build**  
    Jika prototipe yang dibuat telah selesai, Anda dapat mulai membuat dan menyusun dashboard sesuai prototipe yang telah dibuat. Pada prosesnya Anda perlu menentukan bentuk grafik yang tepat untuk menjawab pertanyaan bisnis tersebut.  
      
    
5.  **Evaluasi**  
    Tahap berikutnya adalah mengevaluasi dashboard yang telah dibuat. Hal ini dilakukan untuk memastikan grafik dan komponen visual lain yang terdapat di dalam dashboard telah efektif dan mudah dipahami.  
      
    
6.  **Feedback**  
    Terakhir kita juga perlu meminta feedback kepada audiens atau user terkait dashboard yang telah dibuat. Hal ini tentunya akan sangat membantu kita dalam membuat business dashboard yang lebih baik ke depannya. 
[](https://www.dicoding.com/academies/590/tutorials/34098?hl=define# "dos:0280bed7d6b8c0bce02d491192d7515320230913113346.png")    
    ![image](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/academy/dos:0280bed7d6b8c0bce02d491192d7515320230913113346.png)

### Business Dashboard 
Business dashboard pada proyek ini dapat diakses melalui pranala (link) berikut : 
-  [Demographics of employees](http://localhost:8000/public/dashboard/398cb3da-c03a-42ae-a20c-376731f7d5c2)
- [Employee Turnover Analysis](http://localhost:8000/public/dashboard/9ef77c75-a07e-47ca-bd08-af6aad6837bd)
- [Employee Wellness](http://localhost:8000/public/dashboard/5382b602-4e1d-4c31-a432-d02ba3e00ea9)

## 🎯 Conclusion & Recommendation Actions
**SMART (Specific - Measurable - Action oriented - Relevant - Time bond)**

Based on the KPI & insights obtained from the analysis results, it can be concluded that there are several factors that influence the attrition rate of the Jaya Jaya Maju company. These factors are monthly income, overtime, age, total working years, and distance from home (**Specific**).

From the previously created business dashboard, several insights can be obtained, some of which are as follows:

- As many as 85% (153 employees) who stopped working earned a low-medium monthly income. Meanwhile, employees with higher monthly income (high income) tend to stay or work at the company. (**Measurable**) By considering the impact of wages on the company's attrition rate, reconsideration or efforts are needed to review and collect information to find out whether the company provides competitive wages according to market conditions. So that employees feel appreciated and encouraged to continue working. (**Action oriented & Relevant**)  

- Employees or workers in the 18-40 year age group have a greater tendency to stop working than those in the older age group. (**Measurable**) Therefore, efforts that can be made are aligning the long-term vision with young employees, as well as providing intensive, career, as well as clear promotions. (**Action oriented & Relevant**) 

- The distance between the office and residence also influences the attrition rate of the Jaya Jaya Maju company, based on analysis results, 59% (107 employees) who left or stopped working lived very far from the office. (**Measurable**) Related With this problem, companies can provide transportation support for employees or provide support in the form of transportation allowances. So it can reduce the company's attrition rate. (**Action oriented & Relevant**).

- As many as 54% (98 employees) stopped working due to overtime. (**Measurable**) Therefore, efforts that companies can make are planning or scoping projects that are carried out properly at the beginning and with adequate workforce, so that employees workers do not work overtime. Another alternative is giving compensation to employees who have worked overtime, so that it can reduce the attrition rate. (**Action oriented & Relevant**)

-  As many as 65% (117 employees) who stopped working were related to business travel factors at a rare level. This shows that business travel has an effect on the attrition rate. Steps that companies can take are to review and optimize business travel policies for all employees in order to minimize employee stress levels and help retain employees. (**Action oriented & Relevant**)

The results of the analysis or insight obtained along with the steps the company can take to reduce the attrition rate must be carried out within a clear time period. To begin with, certain programs that have been designed will be implemented during the first six months. Then an evaluation of the program is carried out to find out whether there are significant changes to the attrition rate of the Jaya Jaya Maju company. (**Time Bond**)

On the other hand, steps are also needed such as holding regular face-to-face meetings within a certain period of time between HR managers and employees who are at high risk of leaving or quitting their jobs. With the aim of knowing and discussing the working conditions experienced. So that stakeholders can determine appropriate preventive measures and solutions.

## Acknowledgements 
Realinho,Valentim, Vieira Martins,Mónica, Machado,Jorge, and Baptista,Luís. (2021). Predict students' dropout and academic success. UCI Machine Learning Repository.  [https://doi.org/10.24432/C5MC89](https://doi.org/10.24432/C5MC89).

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://syarifulmsth.github.io) [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syariful-musthofa/) [![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)

## Feedback
If you have any feedback, please reach out at syarifulm007@gmail.com
