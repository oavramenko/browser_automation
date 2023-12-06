from selenium import webdriver
# options stop Chrome from closing after execution of programme
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 
browser = webdriver.Chrome(options=options)

urls = ["https://www.github.com/", "https://www.aswf.io", "https://roadmap.sh/roadmaps"]
# opens first tab
#browser.get("https://www.mooc.fi/en/")


dev_resources = ["https://free-for.dev/#/"]
devs_100_main = ["https://communitytaught.org/dashboard","https://www.twitch.tv/learnwithleon", "https://communitytaught.org/class/all","https://100devs-info.netlify.app/#nine",]
devs_100_resources = ["https://www.typingtest.com/benchmark.html","https://www.keybr.com", "https://learn.shayhowe.com/html-css/", "https://www.coursera.org/learn/learning-how-to-learn", ]

organisation = ["https://calendar.google.com/calendar/u/0/r/week", 'email']
job_search_vfx = ["https://www.rodeofx.com/culture-and-talent", "https://framestore.recruitee.com", "https://www.imageworks.com/job-postings", "https://www.dneg.com/careers/open-positions/", "https://www.scanlinevfx.com/careers/"  ]

math_resources = ["https://abuseofnotation.github.io/category-theory-illustrated/01_set/"]

resume_resources = ["https://docs.google.com/document/d/1XgHvZ5wS6DWyqX2ABMiMq4CmGkYtDOUf/edit"]
python_resources = ["https://pythontutor.com/visualize.html#mode=edit","https://www.mooc.fi/en/","https://roadmap.sh/python","https://learning.anaconda.cloud"]

shotgrid_dev_resources = ["https://developer.shotgridsoftware.com/1e047003/?title=Developer+Overview", "https://community.shotgridsoftware.com", "https://github.com/shotgunsoftware/python-api"]
houdini_resources = ["https://www.sidefx.com/learn-main-menu/start-here/"]

french = ["https://usito.usherbrooke.ca", ]
# opens second tab
#browser.execute_script("window.open('about:blank','secondtab');")
#browser.switch_to.window("secondtab")
#browser.get("https://www.github.com/")

# opens third tab
#browser.execute_script("window.open('about:blank','thirdtab');")
#browser.switch_to.window("thirdtab")
#browser.get("https://www.discord.com")

resources =[dev_resources, devs_100_main, dev_resources, math_resources, resume_resources]

# choose your list
choice = input("What do you want to do now? - math, resume, python, french, shotgrid, typing, devops, webdev?")

if choice == "python":
    browser.get(python_resources[0])
    for url in python_resources[1:]:
        browser.execute_script('window.open("{}", "_blank");'.format(url))

#browser.get(urls[0])
#for url in urls[1:]:
#    browser.execute_script('window.open("{}", "_blank");'.format(url))


#    browser.execute_script('''window.open('urls[count]', '_blank');''')
#    browser._switch_to.window(browser.window_handles[number])
