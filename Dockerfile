FROM ubuntu
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
RUN pip3 install  scikit-learn pandas joblib flask
RUN git clone  https://github.com/DavidChatak/mldp.git
WORKDIR /mldp
# COPY . /mldp
EXPOSE 80
CMD python3 postman_test.py
