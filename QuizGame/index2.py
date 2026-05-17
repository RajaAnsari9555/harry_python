def quizgame():
 score = 0;
 questions={
   "What is the capital of India? ": "delhi",
        "What is 2 + 2? ": "4",
        "Which language is used for web? ": "javascript"
  }
 for question , answer in questions.items():
  
  user_answer = input(question).lower()
  if user_answer == answer:
   print("✅ Correct!")
   score = score+1;
  else:
   print( print("❌ Wrong!"))

 print ("\nYour score is:", score)   
 
quizgame() 
  