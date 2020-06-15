import subprocess
import os
import pandas as pd

df = pd.read_csv("job-data.csv")
df = df.fillna("")

df.head()

for index, row in df.iterrows():
    company = row['company'].replace(u'\xa0', u' ')
    job = row['job'].replace(u'\xa0', u' ')
    job_id = str(row['job_id'])
    student = str(row['student'])
    company_adj = row['company_adj'].replace(u'\xa0', u' ')
    project_adj1 = row['project_adj1'].replace(u'\xa0', u' ')
    project_adj2 = row['project_adj2'].replace(u'\xa0', u' ')
    interest1 = row['interest1'].replace(u'\xa0', u' ')
    interest2 = row['interest2'].replace(u'\xa0', u' ')
    bodypar1 = row['bodypar1'].replace(u'\xa0', u' ')
    bodypar2 = row['bodypar2'].replace(u'\xa0', u' ')

    with open("rel-files/jonathan_coverletter.xtx","r") as f:
        tex = f.read()

    tex = tex.replace("**@company**", company)
    tex = tex.replace("**@job**", job)
    tex = tex.replace("**@job_id**", job_id)
    tex = tex.replace("**@student**", student)
    tex = tex.replace("**@company_adj**", company_adj)
    tex = tex.replace("**@project_adj1**", project_adj1)
    tex = tex.replace("**@project_adj2**", project_adj2)
    tex = tex.replace("**@interest1**", interest1)
    tex = tex.replace("**@interest2**", interest2)
    tex = tex.replace("**@bodypar1**", bodypar1)
    tex = tex.replace("**@bodypar2**", bodypar2)



    with open("/mnt/d/Files/Documents/git/auto-apply/rel-files/jonathan_cover_letter.xtx","w") as f:
        f.write(tex)
    
    input("Press enter to continue")

    startpoint = "/mnt/d/Files/Documents/git/auto-apply/rel-files"
    endpoint = "/mnt/d/Program Files/OneDrive/Documents/University Spring 2020/coop/"

    os.system("cd " + startpoint + " && xelatex jonathan_cover_letter.xtx")

    os.system("cd '" + endpoint + "' && mkdir '" + company +"-" + job_id + "'")
    os.system("cd "+ startpoint +" && cp jonathan_cover_letter.pdf '"+ endpoint + company +"-" + job_id + "'")

    os.system("cd rel-files && rm jonathan_cover_letter.pdf jonathan_cover_letter.aux jonathan_cover_letter.xtx jonathan_cover_letter.log jonathan_cover_letter.out")


    print('done')