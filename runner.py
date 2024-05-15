from Table import Table
import re


def main():
    path="input/1nephi1.txt"
    try:
        with open(path, "r", encoding="utf-8") as file:
            file_contents = file.read()
            #convert to lower case
            file_contents = file_contents.lower()
            #remove characters 
            characters_to_remove = "()[],<>@#$%^&*'\"-+=;"
            for char in characters_to_remove:
                file_contents = file_contents.replace(char, '')
            # Add a space before and after '.', '!', '?', making them words
            file_contents = re.sub(r'(?<=[^.!?])([.!?])', r' \1 ', file_contents)
            file_contents = file_contents.replace("\n", ' ')

            
            table=Table(file_contents.split(" "))
            print(table.continueGenerating())


    except FileNotFoundError:
        print("File not found or path is incorrect.")
    #except Exception as e:
    #    print("An error occurred:", e)


if __name__ == "__main__":
    main()