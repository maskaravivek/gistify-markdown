# Gistify Markdown for Hugo or Medium

The script converts all the code blocks in a markdown to Github Gists and dumps the updated markdown to a few file.

# Prerequisite

Create a personal access token and set `GITHUB_TOKEN` python environment variable. 

https://github.com/settings/tokens

You can copy `.env.example` to `.env` and run the following command to set the environment variable. 

```
export $(cat .env | xargs)
```

## Usage

To gistify markdown to hugo format use:

```
python main.py data/test.md data/output.md hugo
```

To gistify markdown to Medium format use: 

```
python main.py data/test.md data/output.md medium
```

