FROM python:3.8

COPY requirements.txt ./

RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 8000

COPY . .

ENV SQLALCHEMY_DATABASE_URI="sqlite:///./agspace.db"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
