FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

RUN apt update && apt install

COPY ./requirements.txt /app/requirements.txt

# Change to whatever GGUF model you want to use
RUN curl -L https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q8_0.gguf -o llama-2-7b.Q8_0.gguf

RUN pip3 install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
