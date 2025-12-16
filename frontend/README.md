# Physical AI & Humanoid Robotics

## A Comprehensive Guide to Building AI-Native Physical Intelligence Systems

This repository hosts the official website and content for **"Physical AI & Humanoid Robotics,"** a comprehensive textbook designed for AI and Robotics students, researchers, and enthusiasts. This book provides a practical and theoretical foundation for understanding and building intelligent robotic systems using an AI-native, spec-driven approach.

### About the Book

The textbook is structured into four core modules, each delving into essential concepts, architectural patterns, and practical implementation details required for developing robots that perceive, reason, and act in the physical world:

*   **Module 1: ROS 2 Fundamentals**: Master the basics of the Robot Operating System (ROS 2), Python agents for robotic control, and Universal Robot Description Format (URDF) modeling.
*   **Module 2: Digital Twin Simulation**: Explore the creation and utilization of digital twins using powerful simulation platforms like Gazebo and Unity, enabling high-fidelity robot simulation and realistic sensor data generation.
*   **Module 3: The AI-Robot Brain (NVIDIA Isaac™)**: Understand the architecture and implementation of AI-driven robot brains, integrating perception, planning, and decision-making systems with NVIDIA Isaac™ technologies.
*   **Module 4: Vision-Language-Action (VLA)**: Dive into the cutting-edge integration of Large Language Models (LLMs) with robotics to enable natural language-driven robot actions, leading to more autonomous and intuitive human-robot interaction.

Each module includes in-depth explanations, illustrative examples, and practical guidance to maximize your learning and empower you to develop the next generation of AI-powered physical intelligence.

### Getting Started (Local Development)

To set up the project locally and start the development server:

1.  **Navigate to the `frontend` directory**:
    ```bash
    cd frontend
    ```
2.  **Install Dependencies**:
    ```bash
    npm install
    ```
3.  **Start the Development Server**:
    ```bash
    npm start
    ```
    This command starts a local development server and opens a browser window. Most changes are reflected live without having to restart the server.

### Building the Project

To generate a static build of the website:

1.  **Navigate to the `frontend` directory**:
    ```bash
    cd frontend
    ```
2.  **Run the build command**:
    ```bash
    npm run build
    ```
    This command generates static content into the `build` directory.

### Deployment

This website is typically deployed using platforms like Vercel. Ensure your deployment platform is configured to:

*   Set the **Root Directory** to `frontend`.
*   Use `npm install` as the **Install Command**.
*   Use `npm run build` as the **Build Command**.

### Contributing

Contributions are welcome! If you find any issues, have suggestions, or would like to contribute content, please open an issue or submit a pull request.

### License

This project is licensed under the MIT License.