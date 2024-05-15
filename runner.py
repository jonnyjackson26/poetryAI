from WordInfo import WordInfo


def main():
    path="1nephi1.txt"
    try:
        with open(path, 'r') as file:
            file_contents = file.read()
            #print("File contents:",file_contents)
            #convert to lower case
            file_contents = file_contents.lower()
            #remove characters 
            characters_to_remove = "()[],<>@#$%^&*-+=;\n"
            for char in characters_to_remove:
                file_contents = file_contents.replace(char, '')
            file_contents = file_contents.replace(".", ' ')
            #print("updated File contents:",file_contents)

            table={}
            words=file_contents.split(" ")
            for i in range(len(words) - 1):
                current_word = words[i]
                next_word = words[i + 1]
                
                if current_word in table:
                    table[current_word].addFollowingWord(next_word)
                else:
                    table[current_word] = WordInfo()
                    table[current_word].addFollowingWord(next_word)

            for word in table:
                print(word,table[word].toString())




    except FileNotFoundError:
        print("File not found or path is incorrect.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()