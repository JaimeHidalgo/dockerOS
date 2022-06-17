# FROM python:3.10

# # Adding trusting keys to apt for repositories

# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -


# # Adding Google Chrome to the repositories

# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'


# # Updating apt to see and install Google Chrome

# RUN apt-get -y update


# # Magic happens

# RUN apt-get install -y google-chrome-stable


# # Installing Unzip
# RUN apt-get install -yqq unzip


# # Download the Chrome Driver
# BROWSER_MAJOR = $(google-chrome --version | sed 's/Google Chrome\([0-9*\].*/\1/g)')
# RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${BROWSER_MAJOR}/chromedriver_linux64.zip

# # # Unzip the Chrome Driver into /usr/local/bin directory

# # RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
# # RUN export Path=$PATH:/usr/local/bin/chromedriver
# # # Set display port as an environment variable
# # ENV DISPLAY=:99

# # WORKDIR /app
# # COPY requirements.txt .
# # RUN pip3 install -r requirements.txt
# # COPY . .
# # #CMD streamlit run app.py


# # CMD ["python", "nft.py"]

# #Testing 

FROM python:3.9
 
ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.29.0
ENV FIREFOX_VER 87.0
 
RUN set -x \
   && apt update \
   && apt upgrade -y \
   && apt install -y \
       firefox-esr \
   && pip install  \
       requests \
       selenium 
 
# Add latest FireFox
RUN set -x \
   && apt install -y \
       libx11-xcb1 \
       libdbus-glib-1-2 \
   && curl -sSLO https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2 \
   && tar -jxf firefox-* \
   && mv firefox /opt/ \
   && chmod 755 /opt/firefox \
   && chmod 755 /opt/firefox/firefox
  
# Add geckodriver
RUN set -x \
   && curl -sSLO https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz \
   && tar zxf geckodriver-*.tar.gz \
   && mv geckodriver /usr/bin/




WORKDIR /app


COPY . .
 
RUN pip3 install -r requirements.txt
 
#CMD python ./app.py
#CMD /bin/bash
CMD tail -f /dev/null