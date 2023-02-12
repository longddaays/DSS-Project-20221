from datetime import datetime
def timeTransform(data):
    data['time_open'].head(2)
    data_new = data.copy()
    data_new[['time1','time2']] = data_new['time_open'].str.split('|',1, expand = True)
    data_new[["start_time1","end_time1"]] = data_new["time1"].str.split('-', 1, expand=True)
    data_new[["start_time2","end_time2"]] = data_new["time2"].str.split('-', 1, expand=True)
    data_new["start_time1"] = data_new["start_time1"].str.split().str.join(' ')
    data_new["start_time2"] = data_new["start_time1"].str.split().str.join(' ')
    data_new["end_time1"] = data_new["end_time1"].str.split().str.join(' ')
    data_new["end_time2"] = data_new["end_time2"].str.split().str.join(' ')
    for i in range(data_new.shape[0]):
        try:
            try: 
                data_new["start_time2"].iloc[i] = datetime.strptime(data_new["start_time2"].iloc[i], '%H:%M').time()
                data_new["end_time2"].iloc[i] = datetime.strptime(data_new["end_time2"].iloc[i], '%H:%M').time()
            finally: 
                data_new["start_time1"].iloc[i] = datetime.strptime(data_new["start_time1"].iloc[i], '%H:%M').time()
                data_new["end_time1"].iloc[i] = datetime.strptime(data_new["end_time1"].iloc[i], '%H:%M').time()
        except: continue
    return data_new
