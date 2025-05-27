
# 🎣 Fisheries Production Analysis System – Lampung Province (2019–2023)

This project builds a Big Data analytics system to analyze fishery production trends in **Lampung Province, Indonesia**, over a 5-year period (2019–2023). The system adopts a **Medallion Architecture (Bronze–Silver–Gold)** with processing built on top of the **Apache Hadoop ecosystem**, combined with **machine learning** (K-Means & Linear Regression) and **interactive visualization dashboards**.

## 📦 System Architecture

- 🔹 **Bronze Layer**: Stores raw data (CSV, SHP) from KKP, BMKG, and BIG.
- 🔸 **Silver Layer**: Performs data cleaning and normalization using Apache Spark.
- 🟡 **Gold Layer**: Aggregates and analyzes data using ML models and prepares it for dashboards.

### 🔧 Technologies Used

| Component        | Tool/Technology             |
|------------------|-----------------------------|
| Distributed Storage | Hadoop HDFS               |
| Batch Processing  | Apache Spark, Spark MLlib   |
| Query Layer       | Apache Hive                 |
| Workflow Orchestration | Apache Airflow        |
| Visualization     | Apache Superset             |
| Deployment        | Docker & Docker Compose     |
| Monitoring        | Apache Ambari               |

## 🔍 Key Features

- 📈 Analyze fishery production (volume & value) by region and type
- ☁️ Integrate weather data (temperature, rainfall, humidity) from BMKG
- 🔍 Cluster regions using K-Means based on environmental and production features
- 🔮 Predict production trends using Linear Regression
- 🗺️ Visualize spatial-temporal insights with interactive dashboards
- 🔄 Monitor and automate pipelines with Apache Airflow

## 🗂️ Project Structure

![alt text](Produksi_ikan_tangkap_laut.csv.png)

```

analisis-produksi-perikanan-di-sumatera/
├── conf/                          # Konfigurasi sistem Hadoop, Hive, dll
│   ├── core-site.xml
│   ├── hbase-site.xml
│   ├── hdfs-site.xml
│   ├── hive-site.xml
│   ├── log4j.properties
│   ├── mapred-site.xml
│   ├── masters
│   ├── slaves
│   └── yarn-site.xml
│
├── dataset/                       # Dataset mentah (CSV, TIFF)
│   ├── BATNAS_100E-105E_10S-05S_MSL_v1.5.tif
│   ├── BATNAS_105E-110E_05S-000_MSL_v1.5.tif
│   ├── BATNAS_105E-110E_10S-05S_MSL_v1.5.tif
│   ├── Budidaya_Ikan_Hias.csv
│   ├── Budidaya_Pembenihan.csv
│   ├── Budidaya_Pembesaran.csv
│   ├── Data_Curah_Hujan_2019-2023.csv
│   ├── Data_Rata-rata_Kelembapan_2019-2023.csv
│   ├── Data_Rata-rata_Suhu_2019-2023.csv
│   ├── Ikan_Tangkap_Laut.csv
│   └── Ikan_tangkap_darat.csv
│
├── scripts/                       # Script kontrol cluster
│   ├── bootstrap-datanode.sh
│   ├── bootstrap-namenode.sh
│   ├── start.sh
│   └── stop.sh
│
├── Dockerfile.airflow             # Dockerfile untuk Airflow
├── Dockerfile.hadoop              # Dockerfile untuk Hadoop (namenode/datanode)
├── Dockerfile.hbase               # Dockerfile untuk HBase
├── Dockerfile.hive                # Dockerfile untuk Hive
├── Dockerfile.spark               # Dockerfile untuk Spark
├── Dockerfile.superset            # Dockerfile untuk Superset
├── Dockerfile.tez                 # Dockerfile untuk Tez (opsional)
├── Dockerfile.zookeeper           # Dockerfile untuk Zookeeper
│
├── README.md                      # Dokumentasi proyek
├── bronze_to_silver.py            # ETL script: tahap Bronze → Silver
├── docker-compose.yml             # Komposisi container
├── mysql-connector-java-8.0.28.jar # JDBC driver MySQL (Hive metastore)
├── spark--org.apache.spark.deploy.master.Master... # (kemungkinan file log/temp)
├── superset-init.sh               # Superset inisialisasi script
├── superset_config.py             # Superset konfigurasi file
└── zoo.cfg                        # Konfigurasi Zookeeper


````

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/sains-data/analisis-produksi-perikanan-di-sumatera.git
cd analisis-produksi-perikanan-di-sumatera

````
### 2. Prepare Your Environment

```bash
cp .env.example .env 
```

### 3. Start the Local Cluster with Docker

```bash
docker-compose up -d
```

### 4. Initialize the Cluster

```bash
docker exec -it namenode bash /scripts/init/init-hdfs.sh
docker exec -it hive-server bash /scripts/init/init-hive.sh
docker exec -it hbase-master bash /scripts/init/init-hbase.sh
```
### 5. Upload Raw Datasets to HDFS (Bronze Layer)

```bash
docker exec -it spark-master python3 /scripts/utils/hdfs_utils.py
```

### 6. Run the ETL Pipeline

```bash
docker exec -it spark-master python3 /scripts/etl/bronze_to_silver.py
```
```bash
docker exec -it spark-master python3 /scripts/etl/silver_to_gold.py
```

### 7. Run Data Quality Checks

```bash
docker exec -it spark-master python3 /scripts/etl/data_quality_check.py
```
### 8. Automate with Airflow

```bash
http://localhost:8081
```

### 9. Access Dashboards (Superset)

```bash
http://localhost:8088
```

```bash
Username: admin
Password: admin1233
```

### 10. Monitoring with Prometheus & Grafana

```bash
Prometheus: http://localhost:9090

Grafana: http://localhost:3000
Login: admin / admin
Load the dashboard from:
monitoring/grafana/dashboards/
```

## 📖 **Sample Output**

The project involves:

- Production summary table by district/year

- Fishery productivity cluster map (K-Means)

- Time-series graphs with weather overlay

- Interactive dashboards with geospatial visualizations

---
## **📊 Dataset**
- Fishery production (capture & aquaculture) – [KKP]

- Weather data: temperature, rainfall, humidity – [BMKG]

- Geographic data (elevation, depth, zones) – [BIG]

---

**Team Members:**  
- Dinda Joycehana (122140048)
- Elia Meylani Simanjuntak (122450026)
- Presilia (122450081)
- Randa Andriana Putra (122450083)

---

