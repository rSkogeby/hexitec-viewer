FROM python:3

WORKDIR /Users/richard/qd/hexitec-viewer

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./src/index.py" ]
