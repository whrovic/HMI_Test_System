# Automatic Test for an HMI Unit

# HMI_Test_System
Program of an automatic test system for an HMI Unit

## Code Requirements

1. Python

First you should install the newest version of python from [Microsoft Windows Store](https://www.microsoft.com/store/productId/9NRWMJP3717K) or from the [official website](https://www.python.org/downloads/).

After that, python and pip should be installed in your device. To verify that, you can open the cmd and type the following commands:

```sh
>python --version
Python 3.11.2
```
```sh
>pip -V
pip 23.0.1
```

2. Virtual Environment (Optional)

Python isn’t great at dependency management. If you’re not specific, then pip will place all the external packages that you install in a folder called site-packages/ in your base Python installation.

So in order to keep track of the dependencies, we can use a Virtual Environment.

In order to do so, you need to install the venv package. Open the cmd and install it as following:

```sh
>pip install virtualenv
```

3. Clone the project

First you need to install git from the [official site](https://git-scm.com/downloads).

Now you need to download the project. To do so, you need to clone this repository into your device.
Here, I will use the Visual Studio Code interface, but you can use whatever, even cmd.

- Open the command palette with the key combination of Ctrl + Shift + P.

- At the command palette prompt, enter gitcl, select the Git: Clone command, then select Clone from GitHub and press Enter.

- When prompted for the Repository URL, select clone from GitHub, then press Enter.

- If you are asked to sign into GitHub, complete the sign-in process.

Note: This section was taken from the microsoft official documentation: [GitHub in VSCode](https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette).

4. Create the Virtual Environment (Optional)

To use the virtual environment, you first need to create it.

In the VSCode, if you open the `requirements.txt` file, there is a button that appears in the bottom right corner of the window `Create Environment...`. Click it, then select the Venv option, the Python interpreter (should only appear one, the global one from `C:\Programs...`). Finally, it will appear a checkbox and select the `requirements.txt` file.

The virtual environment will be created in a folder named `.venv` and all the libraries will be installed inside it.


Alternativelly, if you don't use VSCode or the button doesn't show up for any reason, open the cmd and cd to the `HMI_Test_System` folder (the project one), and type the following command:

```sh
>python -m venv .venv
```

In order to use the venv, you type the following command:

```sh
>.venv\Scripts\activate
```

You should always open the venv before running the code.

To deactivate the venv, you type:

```sh
>deactivate
```

5. Python libraries and dependencies

If you followed the previous step and all the libraries are installed you can skip this step.

If you want to use a venv, you should first open it (see previous step).

In order to install all the code dependencies and the python libraries needed for the project, we have a file named `requirements.txt` with all the needed libraries. Open the cmd in the project folder and type the following:

```sh
>pip install -r requirements.txt
```

6. PyQt6 Designer

To use the PyQt6 Designer tool, which is used to design the GUI elements of our program, it is available inside the site_packages folder (in .venv folder or in python installation folder if you don't use venv): \Lib\site-packages\qt6_applications\Qt\bin\designer.exe.

7. Tesseract

Tesseract is used for OCR. To use it, you first need to install tesseract from [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki).
