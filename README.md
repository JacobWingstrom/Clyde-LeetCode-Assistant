# Clyde: LeetCode Assitant

Clyde is an AI assistant that is meant to help with LeetCode style questions that are 
  commonly asked in programming based interviews. He is not meant for cheating but for 
  helping the user.

## Description

Clyde is an AI assistant using the openAI API and allows the user to use their API key and 
  get assitantce when doing coding interview style questions. Clyde is also able to help 
  with concepts surrounding the problems

## Reason

I made Clyde in order to learn about APIs and API documentation. 

## Getting Started

### Dependencies

[Python 3.13.3](https://www.python.org/)

[PIP](https://pip.pypa.io/en/stable/installation/)

### Installing

Clone the Clyde-LeetCode-Assitant repo into a file and know where you can find it

Open the command prompt by pressing windows + R and typing cmd

in the command prompt type 
```
pip install openai
```

Then get your OpenAI API key from [here](https://platform.openai.com/api-keys)

  Login to your account you wish to use

  Then select Creeate New Secret Key
  
  Create your key and copy it to your clipboard and save it somewhere you can find it if needed

  
  Next in the top right select the three lines and click settings in the bottom right of the panel
  
  Select billing and enter your billing info since OpenAi bills per token used using an API

Open the Clyde.py file in your choice of text editor

On line 38 where it says
```
  api_key = "INSERT OPENAI KEY HERE"
```
Replace the INSERT OPENAI KEY HERE with your api key

### Executing program

In your coomand prompt change your directory to the directory your Clyde.py file is in

  Can do this by using the "cd" command

  For example:
  ```
    cd "CSC Work"/"Clyde-LeetCode-Assistant"
  ```


After your current directory has Clyde.py in run the command
```
python3 Clyde.py
```

Ask any question to Clyde that you need and if you can not figure it out and need the 
  answer you must ask him directly for it. 

## Authors

Contributors names and contact info

[Jacob Wingstrom](jacobwingstrom@arizona.edu)
