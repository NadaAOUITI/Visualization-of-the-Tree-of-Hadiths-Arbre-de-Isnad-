# Visualization of the Tree of Hadiths (Arbre de Isnad)

Interactive visualization of the isnad chain in the Hadith collection to explore narration authenticity.

## Table of Contents
1. [Project Objective](#project-objective)
2. [Motivation](#motivation)
3. [Problem Statement](#problem-statement)
4. [Graph Construction](#graph-construction)
    - 4.1 [Adjacency List](#adjacency-list)
    - 4.2 [Space Complexity](#space-complexity)
5. [Visualization Methods](#visualization-methods)
    - 5.1 [Node Positioning](#node-positioning)
    - 5.2 [Visualization Tips](#visualization-tips)
6. [Strategy and Complexity](#strategy-and-complexity)
    - 6.1 [Chain Insertion Algorithm](#chain-insertion-algorithm)
    - 6.2 [Connection Management](#connection-management)
7. [Challenges Encountered](#challenges-encountered)
8. [Usage Guide](#usage-guide)
9. [Technologies Used](#technologies-used)

---
##Project Architecture
The project's architecture is based on a graph-based model, where nodes represent narrators, and directed edges signify connections in the isnad chains. Key design components include:

Adjacency List Implementation: Efficiently stores narrators and their relationships in a Python dictionary, where keys are narrators, and values are lists of connected narrators.
Hierarchical Node Positioning: Node layers are computed using Breadth-First Search (BFS), placing the root narrators at the top and their successors in subsequent layers.
Validation Mechanisms: Temporal connections between narrators are validated based on criteria like death-date proximity.
## Project Objective
Create an interactive tool to model, manage, and visualize the chains of narration (isnad) of Hadiths, based on optimized data structures.

## Motivation
In Islamic studies, tracing and analyzing the chains of narration (isnad) is crucial to authenticate Hadiths. This project aims to simplify this process by offering an effective visual representation of relationships between narrators.

## Problem Statement
- **Nature of the Problem**: Model the chains of narration with narrators (nodes) and their relationships (edges).
- **Chosen Structure**: Adjacency list, to minimize memory usage compared to an adjacency matrix.
- **Node and Edge Modeling**:
  - **Nodes (Narrators)**: Represent narrators as objects with properties such as name, birthdate, and death date.
  - **Edges (Connections)**: Represent connections between narrators, based on temporal or other criteria.

## Graph Construction

### 4.1 Adjacency List
- **Format Used**: A Python dictionary where each key is a narrator, and its value is a list of connected narrators.
- **Methods**:
  - Add a narrator
  - Remove a narrator
  - Add a connection
  - Remove a connection

### 4.2 Space Complexity
- **Adjacency List**: O(V + E), where V is the number of narrators and E is the number of connections.

## Visualization Methods

### 5.1 Node Positioning
- Nodes are arranged in layers:
  - The root node is at the top.
  - Successive layers represent narrators in the chain, calculated using a breadth-first search (BFS).
- **Complexity**: O(V + E) for traversal and positioning.

### 5.2 Visualization Tips
- **Libraries Used**:
  - **NetworkX**: Graph structure and directed graphs.
  - **Matplotlib**: Graph rendering.
  - **Arabic_reshaper** and **Bidi**: Correct rendering of Arabic text.
- **Features**:
  - Adjustable node size based on their degree.
  - Display labels in Arabic.
  - Customizable colors to differentiate layers.

## Strategy and Complexity

### 6.1 Chain Insertion Algorithm
- Traverse the chains of narrators, adding nodes and edges to the graph.
- Connect each chain to the root node.
- **Time Complexity**: O(n), where n is the total number of narrators in all chains.

### 6.2 Connection Management
- Add or remove connections based on the difference in death dates (e.g., within 40 years).
- **Time Complexity**: O(1) for each verification.

## Challenges Encountered
- **Displaying Data in Arabic**: Solved by using `arabic_reshaper` and `bidi` libraries.
- **Handling Missing Data**: Used `pandas` to manage Excel files and handle missing values.
- **Temporal Connection Criteria**: Compared dates formatted using `pd.to_datetime`.

## Usage Guide

### 8.1 Loading Narrators
- Place the Excel files (“annexe2” and “annexe1”) in the same directory.
- Run the script to load the narrators and their chains of narration.

### 8.2 Manipulating Narrators
- Add or modify a narrator using the `ajouter_narrateur` or `modifier_narrateur` functions.
- Remove a narrator with `supprimer_narrateur`.

### 8.3 Visualization
- Run `graphen.py`.
- Nodes and edges will automatically be positioned and labeled.

  ![Python](https://img.shields.io/badge/python-3.8-blue)


## Technologies Used
- **Programming Language**: Python 3
- **Libraries**: `pandas`, `NetworkX`, `matplotlib`, `arabic_reshaper`, `bidi`
- **Tools**: Visual Studio Code / PyCharm
- **Data**: Excel files
