FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Python script and data file into the container
COPY Word_Frequency_Analysis.py .
COPY random_paragraphs.txt .

# Command to run the Python script
CMD ["python", "Word_Frequency_Analysis.py"]