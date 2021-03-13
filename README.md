<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">10fastfingers Auto Type</h3>

  <p align="center">
    An Over-complexify Auto Type Program
    <br />
    <br />
    <a href="https://github.com/gordon-nguyen/10fastfingers-auto-type/issues">Report Bug</a>
    ·
    <a href="https://github.com/gordon-nguyen/10fastfingers-auto-type/issues">Request Feature</a>
  </p>
</p>





<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
10fastfingers Auto Type is a program that automate the typing experience for you, with various features and settings to choose.



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




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/gordon-nguyen/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/gordon-nguyen/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/gordon-nguyen/repo.svg?style=for-the-badge
[forks-url]: https://github.com/gordon-nguyen/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/gordon-nguyen/repo.svg?style=for-the-badge
[stars-url]: https://github.com/gordon-nguyen/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/gordon-nguyen/repo.svg?style=for-the-badge
[issues-url]: https://github.com/gordon-nguyen/repo/issues
[license-shield]: https://img.shields.io/github/license/gordon-nguyen/repo.svg?style=for-the-badge
[license-url]: https://github.com/gordon-nguyen/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gordon-nguyen
