print("Hello problem 1 from Week 2 Lesson 1.")

## Pr 2  Explain why you should ALWAYS have a .gitignore file in your repo.

## ANS: Because you don't want git to commit and push any scratch work you might use on your local
# computer to the repository

## Pr 3

#Using `open` , create a new file that records user input (min 1, max 4 inputs) and then opens that files and
# APPENDS the following "Received User Input"

received_user_input1 = input("What's your name?")
received_user_input2 = input("How old are you?")
User_Input_file = open('user_input.txt','a')
User_Input_file.write(received_user_input1 + "\n")
User_Input_file.write(received_user_input2 + "\n")
User_Input_file.close()



## Pr 4

# repeat # 3 with a `with`

received_user_input3 = input("Are you enjoying your homework?")
received_user_input4 = input("What's your opinion of these young 2LTs all around you?")

with open('user_input.txt', 'a') as User_Input_file:
User_Input_file.write(received_user_input3 + "\n")
User_Input_file.write(received_user_input4 + "\n")
User_Input_file.close()

## Pr 5

#* Create a new git repo in github.
#* Populate it with typical files and directories (.gitignore and README.md)
#* Commit your changes.
#* Push it to your repository