import subprocess
import os

company = "NASA"
job = "Leader"
job_id = "987654"
student = ""
company_adj = "local"
project_adj1 = "innovative"
project_adj2 = "sustainable"
interest1 = "hands on work"
interest2 = "new technologies"
bodypar1 = "As the project manager of the UBCO Aerospace clubs self landing model rocket project it was important to communicate clearly with my team members, and the club executives.  I interfaced between my 3 sub teams who dealt with the technical work on the project and the executives who dealt with the legal and logistical issues.  Every meeting, I tried to ensure that all 3 sub teams have a goal to work toward, and when they leave I would check to make sure they have a goal to do light research on for next week.  I then reported the progress to my executives, and we re-evaluated project goals as needed. This experience has improved my project planning methodology."
bodypar2 = "I have had the opportunity to be a research assistant at the UBCO CFD Lab.  My job was to analyze slug flow through a capillary tube and suggest points of interest for further analysis.  I met up with the research team on a weekly basis to share my findings and receive new ideas for points of interest.  I have successfully automated my workflow to more effectively analyze the data.  This has helped me develop my critical thinking skills."

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



with open("/mnt/d/Files/Documents/git/auto-apply/rel-files/dummy.xtx","w") as f:
    f.write(tex)

os.system("cd /mnt/d/Files/Documents/git/auto-apply/rel-files && pwd && xelatex dummy.xtx")
#subprocess.call("pwd")
#subprocess.call("xelatex dummy.xtx")"""

print('done')