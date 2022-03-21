import pandas as pd

df = pd.read_csv('data.csv')
total = 50
pj = df.apply(lambda x:x["job_at_campus"]/total, axis=1)
pp = df.apply(lambda x:x["learnt_python"]/total, axis=1)
jp = df.apply(lambda x:x["learnt_python_and_job"]/total, axis=1)
df['prob_job'] = pj 
df['prob_py'] = pp
df['prob_job_py'] = jp 
cp = df.apply(lambda x:x["prob_job_py"]/x["prob_py"], axis=1)
df['cond_job_and_py'] = cp
cj = df.apply(lambda x:x["prob_job_py"]/x["prob_job"], axis=1)
df['cond_py_and_job'] = cj

print(df)
df.to_csv("new.csv")