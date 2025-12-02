# 📝 Task Manager - DSA Project

A comprehensive Task Manager application built with Streamlit, demonstrating custom implementations of **Priority Queue** and **Stack** data structures.

## 🎯 Features

### Custom Data Structures (From Scratch)
- **Priority Queue**: Min-heap based implementation with `insert()`, `extract_min()`, and `peek()` operations
- **Stack**: LIFO (Last In, First Out) implementation with `push()`, `pop()`, and `peek()` operations

### Application Features
- ✨ **Add Tasks**: Sidebar form to create tasks with name and priority (1-5)
- 📋 **Pending Tasks Tab**: View all pending tasks from the priority queue with complete button
- ✅ **Completed Tasks Tab**: View completed tasks in a stack with undo functionality
- 🎨 **Color-Coded Priorities**:
  - 🔴 Priority 1 (Critical) - Red
  - 🟠 Priority 2 (High) - Orange
  - 🟡 Priority 3 (Medium) - Yellow
  - 🟢 Priority 4 (Low) - Green
  - 🔵 Priority 5 (Very Low) - Blue
- ⏰ **Timestamps**: Each task includes creation and completion timestamps
- 💾 **Session State**: Persistent data during the session
- 📊 **Statistics**: Real-time counters for pending and completed tasks
- 🎨 **Beautiful Footer**: Professional footer with project information

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/mudasarmajeed5/task-manager-streamlit.git
cd task-manager-streamlit
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## 📖 Usage

1. **Add a Task**: Use the sidebar form to enter a task name and select a priority level (1-5)
2. **View Pending Tasks**: In the "Pending Tasks" tab, see all tasks organized by priority
3. **Complete a Task**: Click the "✓ Complete" button to move the highest priority task to completed
4. **Undo Completion**: In the "Completed Tasks" tab, click "↶ Undo" to move a task back to pending
5. **Monitor Progress**: Check the statistics in the sidebar to track your tasks

## 🏗️ Project Structure

```
task-manager-streamlit/
├── app.py                 # Main Streamlit application
├── data_structures.py     # Custom PriorityQueue and Stack implementations
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🧠 Data Structures Implementation

### Priority Queue (Min-Heap)
- Uses a binary heap to maintain tasks sorted by priority
- Lower priority number = Higher priority (1 is highest)
- Time Complexity:
  - Insert: O(log n)
  - Extract Min: O(log n)
  - Peek: O(1)

### Stack (LIFO)
- Uses a Python list as the underlying structure
- Last completed task is first to be undone
- Time Complexity:
  - Push: O(1)
  - Pop: O(1)
  - Peek: O(1)

## 🎓 Academic Context

This project was developed as a Data Structures and Algorithms (DSA) semester project, demonstrating:
- Custom implementation of fundamental data structures
- Practical application of priority queues and stacks
- Clean code organization and documentation
- User-friendly interface design

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit**: Web application framework
- **Custom Data Structures**: No external libraries (built from scratch using lists)

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created for DSA semester project
