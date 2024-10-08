# Koushik Krishnan's Resume

from resume_builder.resume_builder import Resume, Section, SectionEntry, ContactInfo, ConcatText, ItalicsText, UnderlinedText, LinkText, BulletedList

resume = Resume(
    contact_info=ContactInfo(
        name="Róbert Leó Jónsson",
        details=[
            "+354 772-1418",
            "robert.leo.jonsson@gmail.com",
            LinkText(
                "linkedin.com/in/robert-leo",
                "https://www.linkedin.com/in/r%C3%B3bert-le%C3%B3-0a01a219b/",
            ),
            LinkText("github.com/Robertleoj", "https://github.com/Robertleoj"),
        ],
        tag_line="An AI engineer specializing in computer vision.",
    ),
    sections = [
        Section(
            title="Experience",
            entries=[
                SectionEntry(
                    title=LinkText("Monumental", "https://www.monumental.co/"),
                    caption="Machine Vision Software Engineer",
                    location="Amsterdam, Netherlands",
                    dates="September 2024 - present",
                    description="Develop and implement vision algorithms to allow construction robots to autonomously build brick walls."
                ),
                SectionEntry(
                    title=LinkText("AIVA", "https://www.aivagolf.com/"),
                    caption="Computer Vision and Software Engineer",
                    location="Reykjavik, Iceland",
                    dates="September 2023 - August 2024",
                    description=BulletedList(
                        [
                            "Real-time vision tasks with data from calibrated cameras, such as 3D pose estimation.",
                            "Low-level C++ programming for hardware-synchronized image acquisition.",
                            "Integrating these solutions into our product.",
                            "Design and manage the PostgreSQL database.",
                            "Design and implement data pipelines.",
                            "Contribute to key business decisions.",
                        ]
                    ),
                ),
                SectionEntry(
                    title=LinkText("Aha.is", "https://www.aha.is/"),
                    caption="AI and Software Engineer",
                    location="Reykjavik, Iceland",
                    dates="April 2021 - August 2023",
                    description=BulletedList(
                        [
                            "Demand prediction using neural network models.",
                            "Data analysis, visualization, and reporting.",
                            "Database programming and design in MySQL."
                        ]
                    ),
                ),
            ],
        ),
        Section(
            title="Academic Work",
            entries=[
                SectionEntry(
                    title=LinkText(
                        text="Expediting Self-Play Learning in AlphaZero-Style Game-Playing Agents",
                        url="https://www.researchgate.net/publication/374297603_Expediting_Self-Play_Learning_in_AlphaZero-Style_Game-Playing_Agents",
                    ),
                    description="A reinforcement learning paper from my Bachelor's thesis. Published in the 2023 European Conference on Artificial Intelligence (ECAI).",
                    dates="May 2022",
                ),
            ],
        ),
        Section(
            title="Education",
            entries=[
                SectionEntry(
                    title=LinkText(
                        "Reykjavik University", url="https://en.ru.is/",
                    ),
                    dates="August 2020 - May 2023",
                    description=ConcatText(
                        "BSc in Discrete Mathematics and Computer Science.",
                        BulletedList(
                            [
                                "Graduated top of my class with a grade average of 9.8/10.",
                                "Dean's list for all semesters.",
                            ]
                        )
                    ),
                )
            ],
        ),
        Section(
            title="Personal Projects",
            entries=[
                SectionEntry(
                    title=LinkText(
                        "Liver Cancer Segmentation using Deep Neural Networks", url="https://github.com/Robertleoj/APDS-final-project"
                    ),
                    description="A one-week project where we applied semantic segmentation with a 2.5D convolutional U-net to locate liver cancer in CT scans.",
                    dates="December 2022"
                ),
                SectionEntry(
                    title=LinkText(
                        "Video Game in C++ with an AI Opponent",
                        url="https://github.com/Robertleoj/Ultimate-Tic-Tac-Toe"
                    ),
                    description="Fun board game implemented in C++, with an AI opponent implemented with Monte Carlo Tree Search.",
                    dates="March 2022"
                )
            ]
        ),
        Section(
            title="Skills",
            entries=[
                SectionEntry(
                    title="AI and Machine Learning",
                    description="I'm skilled in deep learning, and specialize in computer vision. My preferred stack is Python with PyTorch and OpenCV along with the rest of the scientific computing suite in Python (NumPy, Pandas, Matplotlib, Einops, etc). I usually use C++ with a binding library to implement performance-critical algorithms. I also have experience with reinforcement learning and natural language processing.",

                ),
                SectionEntry(
                    title="Mathematics",
                    description="I have a strong background in mathematics, especially in discrete mathematics, linear algebra, multivariable calculus, and probability theory.",
                ),
                SectionEntry(
                    title="Software Engineering",
                    description=ConcatText(
                        "Since my work has been in small companies, I have experience with a wide variety of software engineering areas such as:",
                        BulletedList(
                            [
                                "Database design, programming, and management, mostly in MySQL and PostgreSQL.",
                                "Data engineering.",
                                "Concurrent programming (mostly in C++).",
                                "Low-level programming in C++.",
                                "Docker and Kubernetes.",
                                "Backend programming in Python."
                            ]
                        )
                    )
                ),
                SectionEntry(
                    title="Product Development",
                    description="Since I've worked in small companies, I've been involved in the entire product development lifecycle, from idea to production. I've been involved in key business decisions and product design.",
                )
            ]
        ),
        Section(
            title="Teaching",
            entries=[
                SectionEntry(
                    title="Calculus Teaching Assistant",
                    caption="Reykjavik University",
                    dates="January - May 2024",
                    description="In this course that covered single- and multivariable calculus, I held exercise sessions, graded assignments, and helped organize the course. I did this in my free time as a side job while working at AIVA.",
                ),
                SectionEntry(
                    title="Algorithms Teaching Assistant",
                    caption="Reykjavik University",
                    dates="August - December 2023",
                    description="Here I held exercise sessions, graded assignments, and helped organize the course.",
                ),
            ]
        ),
    ]
)

if __name__ == "__main__":
    resume.cli_main()