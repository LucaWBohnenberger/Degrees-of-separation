# 🎬 Six Degrees of Kevin Bacon 🎭

This project was developed as part of Harvard's **Introduction to Artificial Intelligence (CS50's AI)** course. It implements the "Six Degrees of Kevin Bacon" problem, where any two actors in Hollywood can be connected through a series of movies they both starred in. Using **Breadth-First Search (BFS)**, the program computes the shortest path between two actors by traversing datasets derived from IMDb. 🌐📽️

---

## ✨ Features

- 🔍 Computes the shortest connection between two actors through shared movies.  
- 📂 Supports both large and small datasets for experimentation and testing.  
- 💻 Includes a command-line interface for user interaction.

---

## 📊 Datasets

The repository contains two datasets (`large` and `small`) for testing and experimentation. Both include the following CSV files:

1. **📁 people.csv**:  
   Contains unique actor IDs, names, and birth years.  
   **Example**: id,name,birth 102,Kevin Bacon,1958

2. **📁 movies.csv**:  
Contains unique movie IDs, titles, and release years.  
**Example**: id,title,year 104257,A Few Good Men,1992

3. **📁 stars.csv**:  
Establishes relationships between actors and movies.  
**Example**: person_id,movie_id 102,104257



---

## ⚙️ How It Works

1. **📝 Input**:  
The user provides two actor names via the command-line interface.  

2. **💡 Processing**:  
- Actor IDs are resolved using `person_id_for_name`, which handles disambiguation for actors with the same name.  
- The program computes the shortest path using the `shortest_path` function.  

3. **📤 Output**:  
Displays the shortest sequence of movies and actors connecting the two input actors.

---

## 🎬 Example Run

**Input**:  
Enter the first actor: Jennifer Lawrence
Enter the second actor: Tom Hanks

**Output**:  
Jennifer Lawrence → X-Men: First Class → Kevin Bacon → Apollo 13 → Tom Hanks
Shortest Path: 2 steps


---

## 💡 Key Learnings

While completing this project, I gained insights into:  
- 🧠 **Graph Representation**: Using data structures like dictionaries to model nodes (actors) and edges (movies) in a graph.  
- 🔄 **Breadth-First Search (BFS)**: Implementing BFS to compute the shortest path in a graph.  
- 📂 **Data Loading and Manipulation**: Extracting and organizing relational data from CSV files.  
- 🛠️ **Problem Decomposition**: Structuring complex problems into smaller, manageable components.  

---

## 🚀 Usage

1. **📥 Clone the repository**:  
   ```bash
   git clone https://github.com/LucaWBohnenberger/Degrees-of-separation

2. 📂 Navigate to the project directory:
   ```bash
   cd Degrees-of-separation

3. ▶️ Run the program:
   ```bash
   python degrees.py small

3.1. ▶️ Run the program (This may take some time, as there are hundreds of thousands of rows in the large dataset): 
   ```bash
   python degrees.py large

