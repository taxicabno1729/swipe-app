# Swipe App Project (Using Kivy)

## Overview

This is the first draft of a Kivy app. The app is designed to demonstrate swipe card interactions, allowing users to swipe through a series of cards either left or right. The app features smooth animations, gesture recognition, and a clean, minimalist interface. This README file provides instructions on how to set up the development environment, run the app, and contribute to the project.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Smooth Card Swiping: Intuitive touch-based interaction with cards that can be swiped left or right
- Animated Transitions: Fluid animations when cards are swiped or returned to center
- Responsive Design: Clean interface that adapts to different screen sizes with consistent padding and layout

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.7 or higher
- pip (Python package installer)
- virtualenv (optional but recommended for managing dependencies)

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/taxicabno1729/swipe-app.git
   cd kivy-app
   ```

2. **Create a Virtual Environment (Optional):**

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Running the App

1. **Run the App:**

   ```sh
   python main.py
   ```

2. **Using the App:**

   - Swipe cards left or right using touch/mouse drag gestures
   - Each card contains text content that can be read before swiping
   - If you swipe past the threshold distance, the card will animate away
   - If you release before the threshold, the card returns to center
   - After swiping a card, the next card in the deck is automatically shown
   - The app maintains a clean, minimalist interface with rounded white cards on a light gray background

## Directory Structure

```
swipe-app/
├── main.py
├── swipe_container.py
├── swipe_card.py
├── requirements.txt
└── README.md
```

- **app/**: Contains the main application files.
  - **main.py**: Entry point of the application.
  - **screens/**: Contains individual screen classes.
- **assets/**: Contains media files such as images and fonts.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: This file.

## Contributing

We welcome contributions from the community! Here are some ways you can contribute:

1. **Report Bugs**: If you find a bug, please open an issue on our [GitHub Issues](https://github.com/taxicabno1729/swipe-app/issues) page.
2. **Request Features**: If you have ideas for new features, please open an issue.
3. **Submit Pull Requests**: If you want to contribute code, please fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
