"""
Quiz Questions Bank
====================
All questions for the Accessible Gamified Quiz System.
Each question has:
  - q:  the question text
  - c:  list of 4 answer choices
  - a:  index of the correct answer (0 = A, 1 = B, 2 = C, 3 = D)
  - d:  difficulty level ("easy", "medium", or "hard")
"""

QUESTIONS = {
    "english": [
        {
            "q": "Which sentence is grammatically correct?",
            "c": ["She don't like apples.", "He goes to school every day.", "They was happy.", "We is ready."],
            "a": 1, "d": "easy"
        },
        {
            "q": "What is the plural form of 'criterion'?",
            "c": ["Criterions", "Criterias", "Criteria", "Criterium"],
            "a": 2, "d": "medium"
        },
        {
            "q": "Which word is an antonym of 'benevolent'?",
            "c": ["Kind", "Generous", "Malevolent", "Charitable"],
            "a": 2, "d": "easy"
        },
        {
            "q": "'Neither the students nor the teacher ___ present.' Choose the correct verb.",
            "c": ["were", "are", "is", "have been"],
            "a": 2, "d": "hard"
        },
        {
            "q": "'The bag is very heavy.' — What part of speech is 'heavy'?",
            "c": ["Noun", "Adverb", "Verb", "Adjective"],
            "a": 3, "d": "easy"
        },
        {
            "q": "Which sentence uses the passive voice?",
            "c": ["Maria ate the cake.", "The cake was eaten by Maria.", "Maria is eating cake.", "Maria will eat the cake."],
            "a": 1, "d": "medium"
        },
        {
            "q": "What does the prefix 'mis-' mean in 'misunderstand'?",
            "c": ["Again", "Not", "Wrongly", "Before"],
            "a": 2, "d": "easy"
        },
        {
            "q": "Which is an example of a compound sentence?",
            "c": ["She sings.", "She sings, and he dances.", "Because she sings, people listen.", "The talented singer performed."],
            "a": 1, "d": "medium"
        },
        {
            "q": "'He bit off more than he could chew.' This is an example of:",
            "c": ["Simile", "Metaphor", "Idiom", "Hyperbole"],
            "a": 2, "d": "medium"
        },
        {
            "q": "Choose the correct word: 'The ___ of the school gave a speech.'",
            "c": ["principle", "principal", "either", "neither"],
            "a": 1, "d": "hard"
        },
    ],

    "reading": [
        {
            "q": "What is the main purpose of a thesis statement?",
            "c": ["To summarize the essay", "To state the main argument", "To list evidence", "To introduce the topic"],
            "a": 1, "d": "easy"
        },
        {
            "q": "Which text structure compares two or more concepts?",
            "c": ["Sequence", "Cause and Effect", "Compare and Contrast", "Problem and Solution"],
            "a": 2, "d": "easy"
        },
        {
            "q": "A text that aims to convince the reader is called:",
            "c": ["Narrative", "Descriptive", "Persuasive", "Expository"],
            "a": 2, "d": "easy"
        },
        {
            "q": "'Context clues' help a reader to:",
            "c": ["Find grammar rules", "Determine word meaning from surrounding text", "Understand the author's biography", "Identify the genre"],
            "a": 1, "d": "easy"
        },
        {
            "q": "What is the purpose of a conclusion paragraph?",
            "c": ["Introduce new ideas", "Present new evidence", "Summarize and reinforce the main point", "State the thesis for the first time"],
            "a": 2, "d": "easy"
        },
        {
            "q": "Which of the following is a primary source?",
            "c": ["A textbook chapter", "An encyclopedia entry", "A diary written during World War II", "A documentary film"],
            "a": 2, "d": "medium"
        },
        {
            "q": "'Imagery' in writing appeals primarily to the reader's:",
            "c": ["Logic", "Senses", "Background knowledge", "Emotions only"],
            "a": 1, "d": "medium"
        },
        {
            "q": "An academic text is best characterized by:",
            "c": ["Casual language and opinions", "Formal language, evidence, and citations", "Emotional storytelling", "Short bullet lists only"],
            "a": 1, "d": "medium"
        },
        {
            "q": "What is the function of a topic sentence?",
            "c": ["To end a paragraph", "To introduce the main idea of a paragraph", "To provide supporting details", "To cite a source"],
            "a": 1, "d": "easy"
        },
        {
            "q": "Which rhetorical appeal relies on the speaker's credibility?",
            "c": ["Pathos", "Logos", "Ethos", "Kairos"],
            "a": 2, "d": "hard"
        },
    ],

    "science": [
        {
            "q": "What is the basic unit of life?",
            "c": ["Atom", "Cell", "Organ", "Tissue"],
            "a": 1, "d": "easy"
        },
        {
            "q": "Which organelle is called the 'powerhouse of the cell'?",
            "c": ["Nucleus", "Ribosome", "Mitochondria", "Golgi apparatus"],
            "a": 2, "d": "easy"
        },
        {
            "q": "What gas is most abundant in Earth's atmosphere?",
            "c": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Argon"],
            "a": 2, "d": "easy"
        },
        {
            "q": "Photosynthesis primarily occurs in which organelle?",
            "c": ["Nucleus", "Chloroplast", "Vacuole", "Mitochondria"],
            "a": 1, "d": "easy"
        },
        {
            "q": "What type of rock forms from cooling lava or magma?",
            "c": ["Sedimentary", "Metamorphic", "Igneous", "Limestone"],
            "a": 2, "d": "easy"
        },
        {
            "q": "DNA stands for:",
            "c": ["Deoxyribonucleic Acid", "Diribonucleic Atom", "Deoxyribose Nuclein Acid", "Deoxyribose Nitrogen Acid"],
            "a": 0, "d": "medium"
        },
        {
            "q": "Which process converts glucose into usable energy in cells?",
            "c": ["Photosynthesis", "Transpiration", "Cellular Respiration", "Osmosis"],
            "a": 2, "d": "medium"
        },
        {
            "q": "What layer of Earth lies between the crust and outer core?",
            "c": ["Asthenosphere", "Mantle", "Lithosphere", "Inner core"],
            "a": 1, "d": "medium"
        },
        {
            "q": "Which is a renewable energy source?",
            "c": ["Coal", "Natural gas", "Solar energy", "Petroleum"],
            "a": 2, "d": "easy"
        },
        {
            "q": "Correct sequence of ecological organization (smallest to largest):",
            "c": [
                "Ecosystem→Community→Population→Organism",
                "Organism→Population→Community→Ecosystem",
                "Population→Organism→Ecosystem→Community",
                "Community→Ecosystem→Organism→Population"
            ],
            "a": 1, "d": "hard"
        },
    ],

    "math": [
        {
            "q": "What is the domain of f(x) = 1 / (x – 3)?",
            "c": ["All real numbers except 3", "All real numbers", "x > 3", "x < 3"],
            "a": 0, "d": "medium"
        },
        {
            "q": "Solve for x: 2x + 5 = 13",
            "c": ["x = 4", "x = 9", "x = 3", "x = 6"],
            "a": 0, "d": "easy"
        },
        {
            "q": "Which is a rational function?",
            "c": ["f(x) = √x", "f(x) = (x+2)/(x–1)", "f(x) = 2^x", "f(x) = |x|"],
            "a": 1, "d": "medium"
        },
        {
            "q": "What is the range of f(x) = x²?",
            "c": ["All real numbers", "y ≥ 0", "y > 0", "y ≤ 0"],
            "a": 1, "d": "easy"
        },
        {
            "q": "Evaluate f(3) if f(x) = 2x² – x + 4",
            "c": ["19", "13", "25", "17"],
            "a": 0, "d": "medium"
        },
        {
            "q": "Simplify: (x² – 9) / (x – 3)",
            "c": ["x – 3", "x + 3", "x² + 3", "x + 9"],
            "a": 1, "d": "medium"
        },
        {
            "q": "The vertical line test determines if a graph is a:",
            "c": ["Relation", "Function", "Polynomial", "Sequence"],
            "a": 1, "d": "easy"
        },
        {
            "q": "What is the inverse of f(x) = 3x + 6?",
            "c": ["f⁻¹(x) = (x–6)/3", "f⁻¹(x) = (x+6)/3", "f⁻¹(x) = 3x–6", "f⁻¹(x) = x/3"],
            "a": 0, "d": "hard"
        },
        {
            "q": "Which equation represents a linear function?",
            "c": ["y = x²", "y = 2x + 1", "y = x³", "y = 1/x"],
            "a": 1, "d": "easy"
        },
        {
            "q": "What is the sum of the roots of x² – 5x + 6 = 0?",
            "c": ["6", "–5", "5", "–6"],
            "a": 2, "d": "hard"
        },
    ],
}
