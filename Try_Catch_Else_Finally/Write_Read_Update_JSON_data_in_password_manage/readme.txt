Here we are updating our Password-Manager project with search functionality
where we write the name of the website and when we click search, the saved email and password corresponding to that website pops up

as we worked upon data.txt file in our previous project which makes it very difficult to search; so we are going to be leveling up our data storage in out Password Manager;
by switching from saving data straight to a text file to a fancier data format known as "JSON" i.e. JavaScript Object Notation.

it has similar syntax as dictionaries

A JSON is essentially composed of a bunch of nested lists and dictionaries and it has that key value pair data structure.

To work with JSON data in python we can use the inbuilt JSON library, and we are going to use it to "Write", "Read" and "Update" data to a JSON file.

        * Write in JSON : json.dump()

                        with open("data.json", "w") as file:
                            json.dump(new_data, file , indent=4)

        * Read in JSON : json.load()

                        with open("data.json", "r") as file:           # writing in data.json file
                            data = json.load(file)
                            print(data)

        * Update in JSON : json.update()

                        with open("data.json", "r") as file:
                            data = json.load(file)                  # retrieving old data
                            data.update(new_data)                   # updating old data

                        with open("data.json", "w") as file:
                            json.dump(data, file , indent=4)        # writing new data



Note : the data we dump, load or update in json should be in dictionary


The exception with our program is when we dump our very first data into the data.json file it gives the "FileNotFoundError" error