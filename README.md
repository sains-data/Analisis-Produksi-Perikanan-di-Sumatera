
# 📊 Big Data Analytics for Fisheries Production in Sumatra

This project demonstrates the use of Hadoop’s ecosystem, specifically Apache Spark, for analyzing fisheries production data from Sumatra, Indonesia. The system processes multi-source data using batch analytics to support optimal decision-making and policy formulation.

**Team Members:**  
Dinda Joycehana (122140048)
Elia Meylani Simanjuntak (122450026)
Presilia (122450081)
Randa Andriana Putra (122450083)

---

## 🧱 **System Architecture**

We adopted a multi-layered structure for handling large-scale fisheries production data with a batch processing approach:

| Layer | Description | Tools | Format |
|-------|-------------|-------|--------|
| **Raw Data Layer** | Stores fisheries data from various sources | Kafka, Flume, HDFS | CSV, JSON, Excel |
| **Processing Layer** | ETL, transformation, model training | Spark, Spark Streaming, MLlib | Parquet, Avro |
| **Serving Layer** | Ready-to-query structured data | Hive, HBase | ORC, Parquet |

---

## 📖 **Project Overview**

The project involves:

- Batch data pipeline for fisheries data using Spark
- Machine learning: Predicting fisheries production with Spark MLlib
- Data ingestion and processing using Spark and HDFS
- Integrated data storage with HBase and Hive for query and retrieval

---

## 🌟 **Key Focus Areas**

- **Apache Hadoop Distributed File System (HDFS)**
- **Apache Spark** (MLlib, Streaming)
- **Apache Kafka & Hive**
- **Data Modeling for Batch Processing**
- **Waterfall Methodology** for structured development

---

## ⚙️ **System Components & Tech Stack**

| Category | Tools |
|----------|-------|
| **Distributed Storage** | Hadoop HDFS |
| **Batch Processing** | Apache Spark |
| **Stream Processing** | Spark Streaming, Kafka |
| **Query Layer** | Hive, Spark SQL |
| **Data Lake Store** | Parquet, ORC |
| **Machine Learning** | Spark MLlib |
| **IoT Data** | HBase, Kafka |
| **Orchestration** | Apache Airflow |
| **Monitoring** | Apache Ambari |

---

## 🔄 **Workflow DAG (Airflow)**

```
fisheries_production_pipeline/
├── ingest_fisheries_data
├── clean_data
├── map_reduce_aggr
├── load_to_hdfs
├── analytics_hive
├── predictive_model
├── generate_production_map
└── notify_users
```

---

## 📦 **Folder Structure**

```
fisheries-bigdata-sumatera/
├── datasets/                    # Raw datasets (Kementerian Kelautan dan Perikanan, BPS)
├── docs/                        # Architecture, specs, and documentation
│   ├── architecture.png
│   ├── data_catalog.md
│   └── pipeline.drawio
├── scripts/                     # Scripts for MapReduce, Hive, Kafka, and ML
├── docker/                      # Docker & Docker Compose setup
├── airflow_dags/               # DAGs for pipeline orchestration
├── notebooks/                   # Jupyter notebooks for analysis
└── requirements.txt
```

---

## 🚀 **How to Run the Project (Deployment)**

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/fisheries-bigdata-sumatera.git
   cd fisheries-bigdata-sumatera
   ```

2. Start the cluster:
   ```
   docker-compose up -d
   ```

3. Access the services:
   - Hadoop UI: localhost:9870
   - Spark UI: localhost:4040
   - Hive: localhost:10000
   - Airflow: localhost:8080

4. Load sample data into `/data/raw/` and trigger the Airflow DAG.

---

## 🛡️ **Requirements & Functional Specs**

**Functional Requirements**:
- Ingest and clean fisheries production data into HDFS
- Batch processing with Apache Spark for data transformation
- Predictive model using regression or time-series algorithms
- SQL interface via Hive for data analysis
- Generate production risk maps

**Non-Functional Requirements**:
- Scalability and high availability
- Efficient data storage with Parquet/ORC

---

## 🏠 **Sample Use Case: Sumatera's Fisheries**

In Sumatera, the fisheries industry plays a vital role in economic growth and food security. A significant challenge lies in managing and analyzing vast amounts of fisheries production data across different provinces.

This system integrates:
- **BMKG**: Rainfall, temperature, and humidity
- **BPS**: Historical production data

Results: 
- Real-time insights and accurate predictive analytics assist in informed decision-making for fisheries management.
- Project Documentation
