from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col

# Inisialisasi SparkSession
spark = SparkSession.builder \
    .appName("BronzeToSilverETL") \
    .getOrCreate()

# Path HDFS
bronze_path = "hdfs://namenode:9000/bronze"
silver_path = "hdfs://namenode:9000/silver"

# Fungsi ETL untuk data perikanan tangkap
def process_tangkap(file_path, jenis_tangkap):
    df = spark.read.option("header", True).csv(file_path)
    df_cleaned = df.withColumnRenamed("Tahun", "Tahun") \
                   .withColumnRenamed("Provinsi", "Provinsi") \
                   .withColumnRenamed("Jenis Ikan", "Jenis_Ikan") \
                   .withColumnRenamed("Volume (ton)", "Volume") \
                   .withColumnRenamed("Nilai Produksi (juta rupiah)", "Nilai") \
                   .withColumn("Jenis_Tangkap", lit(jenis_tangkap))
    return df_cleaned

# Fungsi ETL untuk data budidaya
def process_budidaya(file_path, jenis_budidaya):
    df = spark.read.option("header", True).csv(file_path)
    df_cleaned = df.withColumnRenamed("Tahun", "Tahun") \
                   .withColumnRenamed("Provinsi", "Provinsi") \
                   .withColumnRenamed("Komoditas", "Komoditas") \
                   .withColumnRenamed("Volume (ton)", "Volume") \
                   .withColumnRenamed("Nilai Produksi (juta rupiah)", "Nilai") \
                   .withColumn("Jenis_Budidaya", lit(jenis_budidaya))
    return df_cleaned

# Proses data tangkap
laut = process_tangkap(f"{bronze_path}/Ikan_Tangkap_Laut.csv", "Laut")
darat = process_tangkap(f"{bronze_path}/Ikan_Tangkap_Darat.csv", "Darat")

# Proses data budidaya
pembenihan = process_budidaya(f"{bronze_path}/Budidaya_Pembenihan.csv", "Pembenihan")
pembesaran = process_budidaya(f"{bronze_path}/Budidaya_Pembesaran.csv", "Pembesaran")
ikan_hias = process_budidaya(f"{bronze_path}/Budidaya_Ikan_Hias.csv", "Ikan Hias")

# Simpan ke silver
laut.write.mode("overwrite").parquet(f"{silver_path}/tangkap_laut")
darat.write.mode("overwrite").parquet(f"{silver_path}/tangkap_darat")
pembenihan.write.mode("overwrite").parquet(f"{silver_path}/budidaya_pembenihan")
pembesaran.write.mode("overwrite").parquet(f"{silver_path}/budidaya_pembesaran")
ikan_hias.write.mode("overwrite").parquet(f"{silver_path}/budidaya_ikan_hias")

spark.stop()
