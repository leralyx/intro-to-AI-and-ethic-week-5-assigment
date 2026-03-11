# vowels = "eouiaEOUIA"
# word = input("the word pls")
# quantity = 0

# for letter in word :
#     if letter in vowels:
#         quantity +=1 
# print(quantity)

# --------------------------- kara -> arak
# the_word = input("the word to reverse")
# print(the_word[::-1])
#-----------------------

# the_word = input("the word pls")

# the_new_word = the_word[::-1]

# if the_word == the_new_word:
#     print("this word is paly...")
# else:
#     print("isnt the paly....")

#---------------------------------------------

# the_words_r = input("text something")

# dicti = {}

# the_words = the_words_r.split(" ")

# for word in the_words :
#   if word not in dicti:
#       dicti[word] = 0
#   else:
#       dicti[word] += 1
      


# for key, value in dicti.items():
#     print(f"{key} -> {value}")

#------------------------------------

# the_sentence = input("text smt")
# lists = the_sentence.split(" ")
# longest = ""
    
# for w in lists :
#     if len(w) > len(longest) :
#         longest = w
# print(longest)

#-----------------------------------         
# text  = input("text pls").lower
# patern  = input("pattern pls").lower


# frequency = 0 
# indexes = []

# for i in range(len(text) - len(patern) + 1):
#     if text[i : i + len(patern)] == patern :
#         frequency += 1
#         indexes.append(i)
        
# print(indexes)
# print(frequency , "tada")

# -----------------------

# text = input("info pls")
# patern = "mabc"
# new_text = []

# new_text_ = ''
# for i in text :
#      for y in  patern :
#          new_text.append(chr(ord(i) + ord(y)))
         
# print(*new_text)

#----------------------------
