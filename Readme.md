# My Zootopia

My Zootopia is a Python-based project that allows the user to search for an animal name and displays all search results via a dynamic HTML webpage. 
To fetch the Animal data, the Animals API from API Ninjas is used.

## Features

- **API Integration:** Retrieves animal data from API Ninjas [Animals API](https://api-ninjas.com/api/animals).
- **Data Structuring:** Organizes animal data into structured classes.
- **Dynamic HTML Generation:** Creates a custom HTML page with animal cards, each displaying key details.
- **No-Match Message:** Provides a message when no matching animal is found.
- **User Interaction:** Prompts for user input, enabling interactive searches for animals.

## Requirements

- Python 3.7 or higher
- External libraries:
  - [requests](https://pypi.org/project/requests/)
  - [python-dotenv](https://pypi.org/project/python-dotenv/)

Modules used from the python standard library: `sys`, `dataclasses`, `os`.


## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Sammyduzit/My-Zootopia-API.git
   cd My-Zootopia-API
   ```	

2. **Create virtual environment (optional):**
	```bash
	python -m venv venv
	```	
	Activate the virtual environment:
    - On **macOS/Linux**:
		```bash
		source venv/bin/activate
		```	
	- On **Windows**:
		```bash
		venv\Scripts\activate
		```	
3. **Install required packages:**
	
	Install required packages from `requirements.txt` with:
	```bash
	pip install -r requirements.txt
	```	

4. **Create/Implement API KEY**
	- Create a `.env` file in the project root directory.
	
	- If you don't have an API Ninjas API KEY yet (if you do, skip this part):
		* Go to [API Ninjas](https://api-ninjas.com/) website and click on the “Sign Up” button.
		* Enter the details and send the sign up form.
		* Check your email inbox, you should find there a verification link. Click on "Verify Email".
		* On the website, click on "My Account" -> “Show API Key”.

	- Add your API KEY to the `.env` file:
		```bash
		API_KEY=your_api_key_here
		```	

## Usage
1. Run the script using:
	```bash
	python animals_web_generator.py
	```
2. When prompted, enter the name of an animal (or type `q` to quit). The script will:
* Fetch data from the API.
* Process and structure the data.
* Generate the HTML file named `animals.html` with the details of the animals found (or message when no matches found).
* Notify you when the website has been successfully generated.
3. Open the `animals.html` file in your browser to view the generated content.


### Contributing

We welcome your contributions to this project! You can support our mission in a variety of ways:

#### 1. Ethical Contribution
Do a kind deed for local wildlife — offer water or food for birds and stray animals, visit your nearby lake to feed the swans, and show kindness to every creature you encounter.

#### 2. Financial Contribution
- Naturschutzbund Deutschland e. V. (NABU) - https://www.nabu.de/spenden-und-mitmachen/index.html
- Fauna & Flora International (FFI) - https://www.fauna-flora.org/support/
- International Union for Conservation of Nature (IUCN) - https://iucn.org/donate