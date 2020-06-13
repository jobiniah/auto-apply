import subprocess
import os

company = "NASA"
extracurricular = "UBCO CFD Lab, UBCO Aerospace Club"
undergrad = "Project Management, Technical Writing"

with open("rel-files/deedy_resume-openfont.xtx","r") as f:
    tex = f.read()

extracurricular = extracurricular.replace(",", " \\newline ")
undergrad = undergrad.replace(",", " \\newline ")


tex = tex.replace("**@course-extra**", extracurricular)
tex = tex.replace("**@course-under**", undergrad)


with open("/mnt/d/Files/Documents/git/auto-apply/rel-files/jonathan_resume.xtx","w") as f:
    f.write(tex)

startpoint = "/mnt/d/Files/Documents/git/auto-apply/rel-files"
endpoint = "/mnt/d/Program Files/OneDrive/Documents/University Spring 2020/coop/"

os.system("cd " + startpoint + " && xelatex jonathan_resume.xtx")

os.system("cd "+ startpoint +" && cp jonathan_resume.pdf '"+ endpoint + company + "'")

os.system("cd rel-files && rm jonathan_resume.pdf jonathan_resume.aux jonathan_resume.xtx jonathan_resume.log jonathan_resume.out")


print('done')