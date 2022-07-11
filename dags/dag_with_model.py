import logging
import mlflow
import airflow
from airflow.decorators import dag,task
import pandas as pd
from datetime import timedelta,datetime
import os,sys
from scripts.model_handler import Model

default_args={
    'owner':'martinluther',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

text ={
    'id':'14e06377-62ea-4d3d-be34-76cd6aa6a737',
    'headline':'ድርጅቱ ከባንኮች ጋር መሥራቱ አስተማማኝ የክፍያ ሥርዓት እንዲፈጠር አስችሏል',
    'article':'የኢትዮጵያ የምርት ገበያ ድርጅት ከባንኮች ጋር\xa0 በጋራ በመስራቱ በተገበያዮች ላይ '+
    'የክፍያ መተማመን እንዲፈጠር ማስቻሉን አስታውቋል፡፡ምርት\xa0 ገበያው '+
    'ከአሁን ቀደም ከአስር ባንኮች ጋር በጋር በመስራቱ ላለፉት ዘጠኝ ዓመታት\xa0 በሚያከናውነው የግብይት '+
    'ሂደት ላይ \xa0መተማመንን \xa0የፈጠረ የክፍያ ሥርዓት እንዲኖር አስችሏል ብሏል፡፡በዛሬው ዕለት '+
    'ምርት ገበያው ከብርሃን ኢንተርናሽናል ባንክ ጋር በጋር\xa0 ለመስራት የሚያስችለውን ስምምነት '+
    'ተፈራርሟል፡፡የአሁኑን ስምምነት ተከትሎ ምርት ገበያው ደንበኞቹ በአስራ አንድ ባንኮች የክፍያ አገልግሎት መፈጸም\xa0 '+
    'እንዲችሉ የሚያደርግ ነው፡፡በአሁኑ ወቅት ድርጅቱ በዘጠኝ የሀገሪቱ አካባቢዎች እየገነባቸው ባሉ የግብይት '+
    'መፈፀሚያ ማዕከላት ሻጭና አቅራቢዎች የክፍያ አገልግሎት እንዲፈጽሙ የሚያስችል ነው ብለዋል ዋና ስራ አስፈፃሚው '+
    'አቶ ኤርሚያስ እሸቱ፡፡\xa0',
    'audio':'../data/test_amharic.wav'
}

@dag(dag_id='dag_for_updating_metadata',
    default_args=default_args,
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval='@hourly')
def update_metadata():
    @task()
    def run():
        metadata = pd.read_csv('../data/metadata.csv')
        metadata.append({
            'translation':text['article'], 
            'label':text['audio'],
            'channel':0,
            'sample_rate':0,
            'duration':0
        }, ignore_index=True)
    run()


@dag(dag_id='dag_for_updating_model',
    default_args=default_args,
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval='@hourly')
def update_model_training_data():
    @task()
    def run():
        with mlflow.start_run(run_name="update_stt_model"):
            
            model = Model(run=True)
            result = model.validate_transcription(
                    ['../data/test_amharic.wav'] , 
                    ["ጠጁን ኰመኰመ ኰመኰመና ሚስቱን ሲያሰቃያት አደረ"])
            mlflow.log_metric("error",result['error'])
    run()

update_metadata() >> update_model_training_data()