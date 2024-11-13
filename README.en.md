# 📊 Quantitative Trading Analysis

Welcome to **Quantitative Trading Analysis**, a repository dedicated to quantitative analysis applied to trading. Here you’ll find resources for developing algorithmic strategies, statistical analysis, and backtesting.

## 📁 Repository Content

This repository contains three main components:

- **Jupyter Notebooks**: Implementations of trading strategies that you can run and modify.
- **Python Scripts**: Python tools for analysis and simulation.
- **Documentation**: Bibliographic references and explanatory notes that help to understand the methods and theories applied.

## 🚀 Setting Up the Working Environment

To facilitate the setup of a consistent working environment, I have included a configuration script (`setup_env.py`) that creates a virtual environment with all necessary dependencies.

### Prerequisites

1. **Python 3.x** installed on your system.
2. **Required packages**: specified in `requirements.txt`.

### Preparing and Running the Virtual Environment

1. **Install Build Tools (Windows)**:
   - Before running the script, it is recommended to download and install [BuildTools](https://visualstudio.microsoft.com/es/visual-cpp-build-tools/) to avoid issues with some dependencies.
   
2. **Compile Optional Dependencies**:
   - If you encounter problems installing the `zipline` dependency, it is recommended to download the `.whl` file from [here](https://github.com/cgohlke/talib-build) and compile it.

3. **Create and Activate the Virtual Environment**:
   - Run the following command in the terminal from the project directory:

     ```bash
     python setup_env.py
     ```

   - This command will create the `venv-quant` virtual environment and install all dependencies listed in `requirements.txt`. You can change the name of the virtual environment in the script if you prefer.

4. **Confirmation Message**:
   - If everything runs correctly, you should see the message:
     ```
     Dependencies installed successfully.
     ```

5. **Activate the Virtual Environment**:
   - Once the environment is created, activate it with the following command:

     ```bash
     venv-quant\Scripts\activate  # On Windows
     # or
     source venv-quant/bin/activate  # On Linux/Mac
     ```

   - When activated, you’ll see `(venv-quant)` at the start of your terminal line, indicating that you’re working in the correct virtual environment.

## 💡 Additional Notes

- **Updating Dependencies**: If you need to add more packages, add them to `requirements.txt` and re-run the `setup_env.py` script.
- **Contributions**: Improvements, suggestions, and contributions are welcome.

This `README.md` should help you set up and quickly get started with quantitative trading analysis. Good luck with your research and strategies! 📈

---

## 👨‍💻 Developer

This project was developed and is maintained by:

- **Iker Arana**
- [LinkedIn](https://www.linkedin.com/in/iker-arana-0ab741a6/) | [GitHub](https://github.com/aranagarapena?tab=repositories)

For inquiries, suggestions, or collaboration on the project, please feel free to reach out. 


---
