# Food Saver India

This repository contains a Streamlit application (`streamlitapp.py`) for the Food Saver India project. Follow these instructions to set up a virtual environment in VS Code on both **macOS** and **Windows**, install dependencies, and run the app.

![image](https://github.com/user-attachments/assets/dc7137cd-1598-46cf-90a6-1641276742ab)


Repository: [Food_Saver_India](https://github.com/CrunchyExplosion/Food_Saver_India)
Website: [Food_Saver_India](https://foodsaverindia.streamlit.app/)


---

## 🚀 Getting Started

### 1. Clone the Repository

Open your terminal and run the following commands:

```bash
git clone https://github.com/CrunchyExplosion/Food_Saver_India.git
cd Food_Saver_India
```



## 🧪 Setting Up the Virtual Environment

### 💻 macOS / Linux

1. **Create the virtual environment**

   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**

   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**

   Ensure you have a `requirements.txt` file in your repository. Then run:

   ```bash
   pip install -r requirements.txt
   ```

---

### 💻 Windows

1. **Create the virtual environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**

   ```bash
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠 Setting Up Visual Studio Code

1. **Open the Project in VS Code**

   Open VS Code and navigate to your project folder (`Food_Saver_India`).

2. **Select the Virtual Environment Interpreter**

   - Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows) to open the Command Palette.
   - Type `Python: Select Interpreter` and select the interpreter from the `venv` folder.

---

## ▶️ Running the Streamlit App

Once your environment is activated and dependencies are installed, run the app with:

```bash
streamlit run streamlitapp.py
```

A browser window should open automatically (usually at [http://localhost:8501](http://localhost:8501)). If it doesn’t, open the URL manually.

---

## 📦 Generating `requirements.txt` (Optional)

If you need to generate or update the `requirements.txt`, run:

```bash
pip freeze > requirements.txt
```



## ✅ You're All Set!

You now have the virtual environment configured in VS Code on your operating system and can run the Streamlit app !!!
