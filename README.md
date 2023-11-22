# LLAMA SERVER
![Icon](/server.png)
## llama.cpp Server, OAI compatible 




## Build and Run:
Git clone repo. Make sure docker is installed. Change the model if you want in Dockerfile. 

Run the following (Linux):

    
```bash
sh run.sh
```

or in Windows:

```bash
./run.sh
```

## Example Use
Use the local endpoint as the base url. You are now using llama.cpp models
```python
from openai import OpenAI

client = OpenAI(
    api_key="none",
    base_url="http://localhost"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": 
            '''
            Name 3 excellent science fiction movies.
            '''
        }
    ]
)

print(completion)
```

### Limitations
- Sorry no function calls yet

