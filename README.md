# Static-Site-Generator

## Overview

The project takes markdown files as input and generates static HTML pages, making it an excellent tool for lightweight website development.

## Installation

1. Clone Repository:
```git clone https://github.com/frozendolphin/Static-Site-Generator.git```
2. Ensure python is installed (version 3.x recommended):
```python --version```

## Usage

#### Running the Local Server

1. Keep markdown files in `content/`
2. Run local server with main.sh script:
```./main.sh```
the python server will start at `http://localhost:8888/`

#### Building for Deployment

To generate for deployment, use build.sh script:
```./build.sh```
This creates a `docs/` directory, which can be used for GitHub Pages hosting. 

## License

This project is licensed under the MIT License.