# 📊 Quantitative Trading Analysis

Welcome to **Quantitative Trading Analysis**, a repository dedicated to quantitative analysis applied to trading. Here, you'll find resources for developing algorithmic strategies, statistical analysis, and backtesting.

## 📁 Repository Contents

This repository contains three main components:

- **Jupyter Notebooks**: Trading strategy implementations you can run and modify.
- **Python Scripts**: Python tools for analysis and simulation.
- **Documentation**: Bibliographic references and explanatory notes to help understand the applied methods and theories.

## 🚀 Setting Up the Work Environment

To simplify setting up a consistent work environment, a configuration script (`setup_env.py`) is included to create a virtual environment with all necessary dependencies.

### Prerequisites

1. **Python 3.x** installed on your system.
2. **Required packages**: listed in `requirements.txt`.

### Preparing and Running the Virtual Environment

1. **Install Build Tools (Windows)**:
   - Before running the script, it is recommended to download and install [BuildTools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) to avoid issues with some dependencies.

2. **Compile Optional Dependencies**:
   - If you encounter issues installing the `zipline` dependency, download the `.whl` file from [here](https://github.com/cgohlke/talib-build) and compile it.

3. **Create and Activate the Virtual Environment**:
   - Run the following command in the terminal from the project directory:

     ```bash
     python 0_setup_env.py
     ```

   - This command will create the virtual environment `venv-quant` and install all dependencies listed in `requirements.txt`. You can rename the virtual environment in the script if needed.

4. **Confirmation Message**:
   - If the setup completes successfully, you should see the following message:
     ```
     Dependencies installed successfully.
     ```
   - It is normal to see errors like this:
     ```
     Error: zipline_reloaded not installed. No module named 'zipline_reloaded'
     Error: scikit_learn not installed. No module named 'scikit_learn'
     ipykernel installed successfully.
     ```

5. **Activate the Virtual Environment**:
   - Once created, activate the environment using the following command in the terminal:

     ```bash
     venv-quant\Scripts\activate  # On Windows
     # or
     source venv-quant/bin/activate  # On Linux/Mac
     ```

   - When activated, `(venv-quant)` will appear at the beginning of your terminal line, indicating that you are using the virtual environment.
   - To confirm that you are using the correct `venv`, you can run the script `1_confirmar_venv.py` with the following command:
     ```bash
     python 1_confirmar_venv.py
     ```
   - The output should be something like:
     ```
     {your directory path}\venv-quant\Scripts\python.exe
     ```

6. **Using the venv as a Kernel in `.ipynb` Files**:
   - Install `ipykernel` in your virtual environment by running:
     ```bash
     pip install ipykernel
     ```
   - Restart VSCode.

7. **Select the Virtual Environment as Kernel in Jupyter Notebooks**:
   - Open your `.ipynb` file in VSCode.
   - At the top-right of the notebook, you'll see an option that says "Select Kernel". Click on it and select your virtual environment `venv-quant` from the list of interpreters.
   - If the kernel doesn't appear, try the following steps:

   7.1. **Manually Add the Virtual Environment to Jupyter**:
      - Activate the virtual environment in the terminal.
      - Register the environment as a Jupyter kernel:
        ```bash
        python -m ipykernel install --user --name=venv-quant --display-name "Python (venv-quant)"
        ```
      - Restart VSCode, open the notebook, and select "Python (venv-quant)" as the kernel.

   7.2. **Verify Configuration in `settings.json` in VSCode**:
      - If the problem persists, configure the virtual environment manually in the `settings.json` file of your project in VSCode:
        - Create a folder named `.vscode` in the root directory of your project if it doesn't exist.
        - Inside `.vscode`, create (or edit) `settings.json` and add the following configuration, adjusting the path for your OS:
          ```json
          {
           "python.pythonPath": "${workspaceFolder}/venv-quant/Scripts/python"  // For Windows
           // "python.pythonPath": "${workspaceFolder}/venv-quant/bin/python"  // For Linux/macOS
          }
          ```
        - Restart VSCode to apply the new settings.

8. **Verify the Active Kernel**:
   - To confirm that you're using the `venv-quant` environment, run the following cell in your notebook:
     ```python
     import sys
     print(sys.executable)
     ```
   - The output should display the path to your virtual environment (`venv-quant`). If you see this, the virtual environment is correctly activated in Jupyter Notebooks within VSCode.

## 💡 Additional Notes

- **Updating Dependencies**: If you need to add more packages, add them to `requirements.txt` and rerun the `setup_env.py` script.
- **If You Encounter Issues with `import pandas_ta as ta`**:
  Run the following command:
  ```bash
  pip install -U git+https://github.com/twopirllc/pandas-ta
