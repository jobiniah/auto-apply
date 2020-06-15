import subprocess
import os
import pandas as pd

df = pd.read_csv("job-data.csv")

df.head()

for index, row in df.iterrows():
    company = row['company'].replace(u'\xa0', u' ')
    job_id = str(row['job_id'])
    extracurricular = row['extracurricular'].replace(".", " \\newline ").replace(u'\xa0', u' ')
    undergrad = row['undergrad'].replace(".", " \\newline ").replace(u'\xa0', u' ')

    with open("rel-files/deedy_resume-openfont.xtx","r") as f:
        tex = f.read()


    tex = tex.replace("**@course-extra**", extracurricular)
    tex = tex.replace("**@course-under**", undergrad)


    with open("/mnt/d/Files/Documents/git/auto-apply/rel-files/jonathan_resume.xtx","w") as f:
        f.write(tex)

    input("Press enter to continue")

    startpoint = "/mnt/d/Files/Documents/git/auto-apply/rel-files"
    endpoint = "/mnt/d/Program Files/OneDrive/Documents/University Spring 2020/coop/"

    os.system("cd " + startpoint + " && xelatex jonathan_resume.xtx")

    os.system("cd "+ startpoint +" && cp jonathan_resume.pdf '"+ endpoint + company+"-" + job_id + "'")

    os.system("cd rel-files && rm jonathan_resume.pdf jonathan_resume.aux jonathan_resume.xtx jonathan_resume.log jonathan_resume.out")


    print('done')