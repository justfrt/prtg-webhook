# Build from debian
FROM debian

# Install required packages
RUN apt-get update && apt-get install -y \
    git \
    python-dev \
    build-essential \ 
    curl

# Install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py

# Add workdirektory
RUN mkdir /http_temp
WORKDIR /http_temp

# Download and install the Adafruit DHT library
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT && python setup.py install

# Install the requests library
RUN pip install requests

# Add the sensorreading script and make it executable
ADD ./temp_reading.py /http_temp
RUN chmod +x /http_temp/temp_reading.py

# Run the sensorreading script in the container
CMD ["python", "/http_temp/temp_reading.py"]
