# Why do this at all ?

mostly because i was too lazy to open a PDF that has my college class schedules and not making calendar twice on my mac and phone(android) seperately.

so i came across twilio's messaging API and thought that i could code a program that sends me notifications directly to my phone as an SMS upon an event occurs, in my case class notification whenever that class has to occur. 

now this is not exactly a good idea and i realized that when i was more than half way done with this project because the same thing is done by a calendar app that too for free. Here a lot of costs are involved and furthermore we have to manually code every event.

As for the learning part this was so much fun. Learned a lot of new stuff.

<br>

# Problems Encountered 

- Time configuration of the cloud was defaulted to UTC and not IST which created a lot of problems for the program as it was working fine but no output was there on the scheduled time. it took a lot of time to figure out this problem and was resolved after which the program worked perfectly!

- Python was terminating upon logging out of the cloud, found the cure for this by using sytemd unit files which made the script run forever and even in case of failures or restarts it will start the script again.

    - file -> NotificationsApp.service 

    - resources -> 

        - https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files

        - https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units

        - https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267

        - https://www.codementor.io/@ufukafak/how-to-run-a-python-script-in-linux-with-systemd-1nh2x3hi0e

- 


<br>
<br>

# cloud setup 

```

sudo apt-get update 
sudo apt-get -y install python3-pip
dpkg-reconfigure tzdata   //change time to local time 
pip install twilio 
pip install schedule 
pip install python-dotenv
pip install datetime 

```
transfer files using scp and run 

<br>
<br>


# Logs

<br>

**17 February 2023, 5:30PM**

the program runs just fine locally but the same project does not run when i put it on the cloud, i have done some troubleshooting and apparently all the libraries and dependencies work, python works with all the dependencies installed and working but  somehow the app does not show any output when run in the cloud. 

now i am going to try to put previous more easy version of the same app and check if it works

<br>

**17 February 2023, 8:30PM**

think i figured it out, it was not the node configuartion or some errors in files or libraries, apparently the time in vm is different from the original (correct) time 
and this is most likely what is causing it not to function properly.

now i have to fix time in cloud and try again. it took me about 3 hrs to figure this out and now it works !

got it to work, this took forever and why was the cloud time in UT when the node created was in Mumbai, India what did it not take india time(IST) by default.

