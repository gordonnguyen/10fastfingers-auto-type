
<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">10fastfingers Auto Type</h3>

  <p align="center">
    An Over-complicated Auto Type Program
    <br />
    <br />
    <a href="https://github.com/gordon-nguyen/10fastfingers-auto-type/issues">Report Bug</a>
    ·
    <a href="https://github.com/gordon-nguyen/10fastfingers-auto-type/issues">Request Feature</a>
  </p>
</p>





<!-- ABOUT THE PROJECT -->
## About The Project

10fastfingers Auto Type is a Python program that automates your typing experience on 10fastfingers.com, with various features and settings to choose from.
No longer do you have to ruin your precious keyboard or feeling miserable about your slow typing.


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python
* [Selenium](https://selenium-python.readthedocs.io/installation.html)
  ```sh
  pip install selenium
  ```
* [webdriver](https://selenium-python.readthedocs.io/installation.html#drivers) (Chromedriver 89 is already included)

### Installation

1. Clone the repo.
   ```sh
   git clone https://github.com/gordon-nguyen/10fastfingers-auto-type.git
   ```
2. Adjust to your liking in settings.ini. Most are self-explainatory.
   ```sh
    ### SETTING ###
    typing_test_url = https://10fastfingers.com/typing-test/english
    word_per_sec = 0.3  # Wait time before a word is typed
    num_test_loop = 1   # How many time it will loop
    extract_text_to_file = True   # Copy words to a text file

    ### ACCOUNT ### 
    # Enter your account details and change use_account to 'True' if you want to sign in.
    use_account = False
    email = johndoe@hotmail.com
    password = joemama
   ```
3. Double click on the program or run it on your IDE.


<!-- CONTRIBUTING -->
## Contributing

Any contributions or feedbacks are **awesome** and **greatly appreciated**.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Gordon Nguyen

LinkedIn: https://www.linkedin.com/in/gordon-nguyen/

Project Link: [https://github.com/gordon-nguyen/10fastfingers-auto-type](https://github.com/gordon-nguyen/10fastfingers-auto-type)