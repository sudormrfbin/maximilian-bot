![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)

# Maximilian

A python bot that sends you twitter threads to your DMs for reading at your
leisure.

## Team members

1. [Sidharth](https://github.com/Sid9993)
2. [Anandhu S](https://github.com/anandhu-eng)

## Team Id

`BFH/recC7iQ8dFoY1ZRJn/2021`

## Link to product walkthrough

[Maximilian Twitter Bot](https://drive.google.com/file/d/1jvW_MIfNlCa5kiZn2HCYU-_hdVPA5dFq/view?usp=drivesdk)

## How it Works ?

1. User mentions [@bfhmaximilian](https://twitter.com/bfhmaximilian) as a reply to
the last tweet in a thread.
2. User gets a DM from the bot with all the tweets in the thread as messages.

## Libraries used

- `tweepy` - from rev `68e19c`
- `logging` - from the stdlib

## How to configure

1. To host the project yourself first get API keys from twitter and then fill them in
the [`.env`](./.env) file.
2. Make a virtual environment `python3 -m venv .venv --symlink`
3. Activate the venv with `source .venv/bin/activate`
4. Install dependencies with `pip install -r requirements.txt`

## How to Run

From the root of the repo launch the bot with `python3 maximilian`
