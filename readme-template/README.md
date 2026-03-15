# CodeBlitz

Welcome to CodeBlitz! We're excited for you to join our high-speed coding competition. This repository is your central hub for all challenges, starter code, and submissions.

---

## Getting Started: Cloning the Repository

To begin, get this repository onto your local machine. Choose the method that best fits your workflow:

### 1. Command Line (CLI)

Open your terminal or command prompt and run:

```bash
git clone <repository-url>
```

### 2. VS Code

1. Open VS Code.
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette.
3. Type **Git: Clone** and press `Enter`.
4. Paste the repository URL and select a local folder.

### 3. JetBrains IDEs (IntelliJ, PyCharm, CLion)

1. On the Welcome Screen, select **Get from VCS**.
2. Alternatively, if a project is already open, go to **Git > Clone...**
3. Ensure **Version Control** is set to `Git`, paste the URL, and click **Clone**.

### 4. GitHub Desktop

1. Open GitHub Desktop.
2. Go to **File > Clone repository...**
3. Select the **URL** tab.
4. Paste the repository URL and click **Clone**.

---

## Project Structure

Your assigned tasks live inside the stage directory for the current level:

```
stage{x}/
├── problems/
│   └── problem{x}/
│       ├── README.md        # Problem description and requirements
│       ├── starter.cpp      # Starter code (C++)
│       ├── starter.py       # Starter code (Python)
│       └── starter.java     # Starter code (Java)
│
├── solutions/
│   └── solution{x}/         # <-- Add your code here
│
└── tests/                   # DO NOT MODIFY
    └── test{x}/
        ├── input1.txt
        ├── input2.txt
        ├── input3.txt
        ├── expected1.txt
        ├── expected2.txt
        └── expected3.txt
```
 
- **`problems/`** — Contains one folder per problem, each with a README and starter files in C++, Python, and Java.
- **`solutions/`** — Place your finished code inside the corresponding `solution{x}/` folder. This is the only directory the grading system reads from.
- **`tests/`** — Contains input/expected output files used by the automated grader. **Do not touch anything here — modifying test files will result in disqualification.**
---

## How to Submit

To ensure your work is graded, follow these specific submission rules:

1. **Main Branch Only** — Push your code directly to the `main` branch. Solutions on other branches will **not** be checked.
2. **Target Directory** — Only files placed inside the `solutions/` directory will be seen by the grading system.
3. **Push via Command Line:**

```bash
git add stage{x}/solutions/your_file.py
git commit -m "Solved problem X"
git push origin main
```

---

## Important Rules

> **Please read carefully — do not ignore.**

To keep the automated grading system running smoothly:

- **DO NOT MODIFY** any files in the `.github/workflows/` directory.
- **DO NOT MODIFY** `grade.sh` or `runner.py`.
- Pushes to files **outside** of `solutions/` will be ignored by the automation scripts.

> [!CAUTION]
> Tampering with grading scripts or workflow files may result in **disqualification** or **failed stage progression**.

---

## Need Help?

If you run into any technical issues or have questions about the problem statements, don't hesitate to reach out to any **Event Organizer**. We're here to help!

**Good luck, and happy coding!**
