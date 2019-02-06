# NxCerti

NxCerti does exactly what the name suggests; it creates certificates if provided with the base template and names.

## To Use

NOTE: If you have experience with programming, please look into the configuration variables present in `main.py` for better customization. The below instructions are with
default configuration.

The client uses pipenv and python imaging library.

- Keep the base template image for the certificates in the project folder with the name "template.png".
- Keep the names to be put on certificates in a csv file "names.csv" (in the project's folder) with names at O'th index with no heading.
- Modify settings such as color, font, font-size and position of the text in the configuration present inside `main.py`.

### First Run

Below are the steps on how to use it **for the first time**:

- `cd /to/project/directory`
- `pip install pipenv`
- go to project directory and run `pipenv shell --three`
- install all dependencies
    `pipenv install`
- run the project and follow the CLI
    `python3 main.py`

### Consecutive Run

Below are the steps that need to be followed if you've already ran the program once.
- `cd /to/project/directory`
- `pipenv shell`
- `python3 main.py`

The virtual environment created in first step is used here :)

NOTE: All your certificates will be saved in the project directory in a folder named "certificates".

## Contributing

Feel free to raise issues and contribute to the project.