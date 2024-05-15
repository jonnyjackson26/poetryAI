from WordInfo import WordInfo


def main():
    path="input/1nephi1.txt"
    try:
        with open(path, 'r') as file:
            file_contents = file.read()
            #convert to lower case
            file_contents = file_contents.lower()
            #remove characters 
            characters_to_remove = "()[],<>@#$%^&*-+=;\n"
            for char in characters_to_remove:
                file_contents = file_contents.replace(char, '')
            file_contents = file_contents.replace(".", ' ')

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

            
            #write results to ouptut/output.txt
            with open("output/output.txt", "w") as output_file:
                for word in table:
                    output_file.write(word + " " + table[word].toString() + "\n")





    except FileNotFoundError:
        print("File not found or path is incorrect.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()