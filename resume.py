from resume_builder.resume_builder import (
    Resume,
    Section,
    SectionEntry,
    ContactInfo,
    ConcatText,
    ItalicsText,
    UnderlinedText,
    LinkText,
    BulletedList,
)

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
    ),
    sections=[
        Section(
            title="",
            entries=[
                SectionEntry(
                    description="Machine vision engineer building production robotics systems. Specialized in camera systems, 3D vision, and real-world perception."
                ),
            ],
        ),
        Section(
            title="Experience",
            entries=[
                SectionEntry(
                    title=LinkText("Monumental", "https://www.monumental.co/"),
                    caption="Machine Vision Software Engineer",
                    location="Amsterdam, Netherlands",
                    dates="September 2024 - present",
                    description=ConcatText(
                        "Robotics scale-up that makes masonry robots.",
                        BulletedList(
                            [
                                "Built and deployed a photogrammetry pipeline for large-scale construction site reconstruction.",
                                "Designed and shipped a stereo camera system for sub-mm brick analysis on a robotic end-effector.",
                                "Developed deep learning models for 3D reconstruction and perception under harsh real-world conditions.",
                                "Improved robot kinematics calibration and debugging workflows.",
                            ]
                        ),
                    ),
                ),
                SectionEntry(
                    title=LinkText("AIVA", "https://www.aivagolf.com/"),
                    caption="Computer Vision and Software Engineer",
                    location="Reykjavik, Iceland",
                    dates="September 2023 - August 2024",
                    description=ConcatText(
                        "Golf swing analysis using calibrated multi-camera systems",
                        BulletedList(
                            [
                                "Built real-time 3D human pose estimation from calibrated multi-camera data.",
                                "Wrote low-level C++ for hardware-synchronized image acquisition.",
                                "Designed and managed the PostgreSQL database.",
                                "Designed and implemented the data pipelines for the cameras.",
                            ]
                        ),
                    ),
                ),
                SectionEntry(
                    title=LinkText("Aha.is", "https://www.aha.is/"),
                    caption="AI and Software Engineer",
                    location="Reykjavik, Iceland",
                    dates="April 2021 - August 2023",
                    description="Demand prediction with neural networks, data analysis, and database design in MySQL.",
                ),
            ],
        ),
        Section(
            title="Education",
            entries=[
                SectionEntry(
                    title=LinkText("Reykjavik University", url="https://en.ru.is/"),
                    dates="August 2020 - May 2023",
                    description=ConcatText(
                        "BSc in Discrete Mathematics and Computer Science.",
                        BulletedList(
                            [
                                "Graduated top of my class with a grade average of 9.8/10.",
                                "Dean's list for all semesters.",
                            ]
                        ),
                    ),
                )
            ],
        ),
        Section(
            title="Skills",
            entries=[
                SectionEntry(
                    description=BulletedList(
                        [
                            "Cameras & Optics - camera/lens selection, calibration, integration",
                            "Photogrammetry - large-scale reconstruction systems",
                            "Stereo Vision - multi-camera systems, depth, calibration",
                            "Deep Learning - training + deploying vision models",
                            "Systems - real-time pipelines, concurrency, architecture",
                        ]
                    ),
                ),
            ],
        ),
        Section(
            title="Tech",
            entries=[
                SectionEntry(
                    description="Python, C++, PyTorch, OpenCV, Ceres, Eigen, OpenGL, Nix, PostgreSQL",
                ),
            ],
        ),
        Section(
            title="Personal Projects",
            entries=[
                SectionEntry(
                    title=LinkText(
                        "lensboy - camera calibration library (Python)",
                        "https://github.com/Robertleoj/lensboy",
                    ),
                    description=BulletedList(
                        [
                            "Developed spline-based distortion models and board warp estimation for high-precision calibration",
                            "Designed a flexible, engineer-friendly calibration pipeline beyond standard OpenCV approaches",
                            "Applied in real-world camera systems requiring sub-mm accuracy",
                        ]
                    ),
                    dates="February 2026",
                ),
                SectionEntry(
                    title=LinkText(
                        "slamd - GPU-accelerated 3D visualization library",
                        url="https://github.com/Robertleoj/slamd",
                    ),
                    description="Real-time 3D visualization library built with C++, OpenGL, and ImGUI.",
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
    ],
)

if __name__ == "__main__":
    resume.cli_main()
