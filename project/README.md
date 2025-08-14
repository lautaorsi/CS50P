Email sender for professors 
Video Demo:  https://clipchamp.com/watch/HmCHVtCsW1i
Description:
The aim of this script is to automatize email sending to student's based on their performance,(e.g. if a student took n exams, they would pass if the sum of their grades divided by n were greater or equal than the passing grade). When dealing with a large class it can be quite a hassle to send emails to your students, especially at the end of semesters while keeping that personal touch. So with this program one would be able to work on a large scale with that personal touch. The script handles every error, exception and input a user were to write.

If the student were to pass they would get a personalized email (provided the excel had enough data to make it personal) with their grade, a diploma and n amount of cookies (n being the student's overall score). The diploma itself contains the students name, current date and a duck as the signature. Different names could be used for the diploma's certification (in this case CS50 is used for demonstration, but that can be changed)

If the student were to fail they would get a personalized email (provided the excel had enough data to make it personal) letting them know they didn't reach the requirements and a cookie to cheer them up.

The project.py file acts as the main script, including a secondary script called diploma.py that handles the creation of the diploma's pdf, using the student's first and last name, the folder also contains the diploma template, the cs50 duck image and a testing file which thoroughly examines functions within the main file.

The code also uses different imports, including email, pdf reader and editor, excel reader, datetime, number to word converter and time functions 

Many visual effects were added to the code to make it look more movie-like, but it can be certainly executed faster without the visuals (for example, the validating animations, and the 'stop' feature that could be simply replaced by ctrl + c)

Email's format guideline's have been followed to avoid getting the email marked as spam, although in some cases it still might be flagged as such. (RFC 5322)

Although the script doesn't actually read the excel's headers it does ask the user's for the header order, this is to avoid any header title being different from any sort of hard-coding names, this way any given excel can be used despite the language or name variations (as long as they contain the same data)

The email validator doesn't require the user to write '@gmail.com', although it can interpret both types, if a wrong username or password is provided the error will be handled and the user will have to run the script again

If the user's input for the excel header's doesn't match the actual file, an error will be raised and the user will have to run the script again, a loop instance will be provided for the user to validate that their input is correct, until approvement the user will be reprompted for the header's order

