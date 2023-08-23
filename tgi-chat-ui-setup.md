## Chat UI startup notes:
WORK IN PROGRESS

Run mongo for the first time:
```
docker run -d -p 27017:27017 --name mongo-chatui mongo:latest
```
In which case the url of your DB will be MONGODB_URL=mongodb://localhost:27017. 

The next time around, start mongo with:
```
docker start mongo-chatui
```

Run this command in the folder with the private key:
```
ssh -i /path/to/your/privatekey.pem -L 5173:localhost:5173 user@your.ec2.ip.address
```

```
MODELS=`[
{
        "name": "Trelis/Llama-2-7b-chat-hf-function-calling-v2",
        "datasetName": "Trelis/function_calling_extended",
        "description": "function calling Llama-7B-chat",
        "websiteUrl": "https://research.Trelis.com",
        "userMessageToken": "",
        "assistantMessageToken": "",
        "chatPromptTemplate": "<s><FUNCTIONS>{\"function\":\"search_bing\",\"description\":\"Search the web for content on Bing. This allows users to search online/the internet/the web for content.\",\"arguments\":[{\"name\":\"query\",\"type\":\"string\",\"description\":\"The search query string\"}]},{\"function\":\"search_arxiv\",\"description\":\"Search for research papers on ArXiv. Make use of AND, OR and NOT operators as appropriate to join terms within the query.\",\"arguments\":[{\"name\":\"query\",\"type\":\"string\",\"description\":\"The search query string\"}]}</FUNCTIONS><[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\n{{#each messages}}{{#ifUser}}{{content}} [/INST] {{/ifUser}}{{#ifAssistant}}{{content}}</s><s>[INST] {{/ifAssistant}}{{/each}}",
        "parameters": {
                "temperature": 0.01,
                "top_p": 0.95,
                "repetition_penalty": 1.2,
                "top_k": 50,
                "truncate": 1000,
                "max_new_tokens": 1024
        },
        "endpoints": [{
                "url": "http://127.0.0.1:8080"
        }]
}
]`
```

```
MODELS=`[
{
        "name": "Trelis/Llama-2-7b-chat-hf-function-calling-v2",
        "datasetName": "Trelis/function_calling_extended",
        "description": "function calling Llama-7B-chat",
        "websiteUrl": "https://research.Trelis.com",
        "userMessageToken": "",
        "assistantMessageToken": "",
        "chatPromptTemplate": "<s><FUNCTIONS>{\"function\":\"search_bing\",\"description\":\"Search the web for content on Bing. This allows users to search online/the internet/the web for content.\",\"arguments\":[{\"name\":\"query\",\"type\":\"string\",\"description\":\"The search query string\"}]},{\"function\":\"search_arxiv\",\"description\":\"Search for research papers on ArXiv. Make use of AND, OR and NOT operators as appropriate to join terms within the query.\",\"arguments\":[{\"name\":\"query\",\"type\":\"string\",\"description\":\"The search query string\"}]}</FUNCTIONS><[INST] {{#each messages}}{{#ifUser}}{{content}} [/INST] {{/ifUser}}{{#ifAssistant}}{{content}}</s><s>[INST] {{/ifAssistant}}{{/each}}",
        "parameters": {
                "temperature": 0.01,
                "top_p": 0.95,
                "repetition_penalty": 1.2,
                "top_k": 50,
                "truncate": 1000,
                "max_new_tokens": 1024
        },
        "endpoints": [{
                "url": "http://127.0.0.1:8080"
        }]
}
]`
```

```
MODELS=`[
{
        "name": "Trelis/Llama-2-7b-chat-hf-function-calling-v2",
        "datasetName": "Trelis/function_calling_extended",
        "description": "function calling Llama-7B-chat",
        "websiteUrl": "https://research.Trelis.com",
        "userMessageToken": "",
        "userMessageEndToken": " [/INST] ",
        "assistantMessageToken": "",
        "assistantMessageEndToken": " </s><s>[INST] ",
        "chatPromptTemplate": "<s><FUNCTIONS>{functionList}</FUNCTIONS>\n\n[INST] {{#each messages}}{{#ifUser}}{{content}} [/INST] {{/ifUser}}{{#ifAssistant}}{{content}}</s><s>[INST] {{/ifAssistant}}{{/each}}",
        "parameters": {
                "temperature": 0.01,
                "top_p": 0.95,
                "repetition_penalty": 1.2,
                "top_k": 50,
                "truncate": 1000,
                "max_new_tokens": 1024
        },
        "endpoints": [{
                "url": "http://127.0.0.1:8080"
        }]
}
]`
```

```
export default [
    {
        "function": "search_bing",
        "description": "Search the web for content on Bing. This allows users to search online/the internet/the web for content.",
        "arguments": [
            {
                "name": "query",
                "type": "string",
                "description": "The search query string"
            }
        ]
    },
    {
        "function": "search_arxiv",
        "description": "Search for research papers on ArXiv. Make use of AND, OR and NOT operators as appropriate to join terms within the query.",
        "arguments": [
            {
                "name": "query",
                "type": "string",
                "description": "The search query string"
            }
        ]
    }
];
```
