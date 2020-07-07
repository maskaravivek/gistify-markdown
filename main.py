import requests
import json
import uuid
import os
import sys

def create_gist(title, description, content, format):
    GITHUB_API = "https://api.github.com"
    API_TOKEN = os.environ["GITHUB_TOKEN"]

    # form a request URL
    url = GITHUB_API+"/gists"
    # print headers,parameters,payload
    headers = {'Authorization': 'token %s' % API_TOKEN}
    params = {'scope': 'gist'}
    payload = {
        "description": description,
        "public": True,
        "files": {title: {
            "content": content
        }
        }
    }

    # make a requests
    res = requests.post(url, headers=headers, params=params,
                        data=json.dumps(payload))

    # print response --> JSON
    j = json.loads(res.text)
    return get_formatted_gist_code(j, format)

def get_formatted_gist_code(response, format):
    if format == 'hugo':
        owner = response['owner']['login']
        id = response['id']
        short_code = '{{< gist '+owner+' '+id+' >}}'
        return short_code
    else: 
        return response['html_url']



def read_file(file_name):
    lines = []
    with open(file_name) as fp:
        lines = list(fp)
    return lines

def write_file(file_name, new_content):
    f = open(file_name, "w")
    f.write(new_content)
    f.close()

def iterate_file(input_file_name, output_file_name, format):
    contents = read_file(input_file_name)
    converted_markdown = ""
    code_block_started  = False
    code_block = ""
    for line in contents:
        if line.startswith('```') and not code_block_started:
            code_block_started = True
        elif line.startswith('```') and code_block_started:
            short_code = create_gist(str(uuid.uuid4()), "", code_block, format)
            converted_markdown = converted_markdown+"\n"+short_code+"\n"
            code_block = ""
            code_block_started = False
        elif code_block_started:
            code_block = code_block+line
        else:
            converted_markdown = converted_markdown+line
    write_file(output_file_name, converted_markdown)


iterate_file(sys.argv[1], sys.argv[2], sys.argv[3])
