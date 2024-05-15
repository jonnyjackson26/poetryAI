from Table import Table


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

            
            table=Table(file_contents.split(" "))
            print(table.continueGenerating())


    except FileNotFoundError:
        print("File not found or path is incorrect.")
    #except Exception as e:
    #    print("An error occurred:", e)


if __name__ == "__main__":
    main()