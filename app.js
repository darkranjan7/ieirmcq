const QUESTION_FILE = "IEIR_MCQ.json";
const STORAGE_KEY = "ieir-mcq-progress-v1";

const state = {
  questions: [],
  currentIndex: 0,
  progress: {},
};

const elements = {
  questionCounter: document.getElementById("questionCounter"),
  questionText: document.getElementById("questionText"),
  optionsContainer: document.getElementById("optionsContainer"),
  prevButton: document.getElementById("prevButton"),
  nextButton: document.getElementById("nextButton"),
  starButton: document.getElementById("starButton"),
  starIcon: document.getElementById("starIcon"),
  menuButton: document.getElementById("menuButton"),
  resetButton: document.getElementById("resetButton"),
  menuDrawer: document.getElementById("menuDrawer"),
  drawerOverlay: document.getElementById("drawerOverlay"),
  closeMenu: document.getElementById("closeMenu"),
  questionGrid: document.getElementById("questionGrid"),
};

function loadProgress() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) {
    return {};
  }
  try {
    const parsed = JSON.parse(raw);
    if (parsed && typeof parsed === "object") {
      return parsed;
    }
  } catch (error) {
    console.warn("Failed to parse saved progress", error);
  }
  return {};
}

function saveProgress() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.progress));
}

function getQuestionState(index) {
  return state.progress[index] || {
    attempts: 0,
    correct: false,
    starred: false,
    selectedOption: null,
  };
}

function updateQuestionState(index, update) {
  const existing = getQuestionState(index);
  state.progress[index] = { ...existing, ...update };
  saveProgress();
}

function renderQuestion() {
  const question = state.questions[state.currentIndex];
  if (!question) {
    return;
  }

  const questionState = getQuestionState(state.currentIndex);

  elements.questionCounter.textContent = `Question ${state.currentIndex + 1} of ${state.questions.length}`;
  elements.questionText.textContent = question.question;
  elements.optionsContainer.innerHTML = "";

  const options = Object.entries(question.options);
  options.forEach(([key, text]) => {
    const optionButton = document.createElement("button");
    optionButton.className = "option";
    optionButton.type = "button";
    optionButton.textContent = `${key.toUpperCase()}. ${text}`;

    if (questionState.selectedOption === key) {
      const isCorrect = key === question.correct_answer.option;
      optionButton.classList.add(isCorrect ? "correct" : "wrong");
      optionButton.classList.add("disabled");
    }

    optionButton.addEventListener("click", () => handleOptionClick(key));
    elements.optionsContainer.appendChild(optionButton);
  });

  elements.prevButton.disabled = state.currentIndex === 0;
  elements.nextButton.disabled = state.currentIndex === state.questions.length - 1;

  elements.starIcon.textContent = questionState.starred ? "★" : "☆";
  elements.starButton.setAttribute("aria-pressed", questionState.starred ? "true" : "false");

  renderQuestionGrid();
}

function handleOptionClick(optionKey) {
  const question = state.questions[state.currentIndex];
  const questionState = getQuestionState(state.currentIndex);

  if (questionState.correct) {
    return;
  }

  const isCorrect = optionKey === question.correct_answer.option;
  const updatedAttempts = questionState.attempts + 1;

  updateQuestionState(state.currentIndex, {
    attempts: updatedAttempts,
    correct: isCorrect,
    selectedOption: optionKey,
  });

  if (isCorrect) {
    markOption(optionKey, true);
  } else {
    markOption(optionKey, false);
  }

  renderQuestionGrid();
}

function markOption(optionKey, isCorrect) {
  const buttons = Array.from(elements.optionsContainer.querySelectorAll(".option"));
  buttons.forEach((button) => {
    if (button.textContent.startsWith(optionKey.toUpperCase())) {
      button.classList.add(isCorrect ? "correct" : "wrong");
      button.classList.add("disabled");
    }
  });
}

function renderQuestionGrid() {
  elements.questionGrid.innerHTML = "";

  state.questions.forEach((question, index) => {
    const button = document.createElement("button");
    const questionState = getQuestionState(index);

    button.type = "button";
    button.textContent = question.number;

    if (questionState.correct && questionState.attempts === 1) {
      button.classList.add("correct");
    } else if (questionState.attempts > 0) {
      button.classList.add("wrong");
    }

    if (questionState.starred) {
      button.classList.add("starred");
    }

    if (index === state.currentIndex) {
      button.style.outline = "2px solid #c77d4a";
    }

    button.addEventListener("click", () => {
      state.currentIndex = index;
      closeDrawer();
      renderQuestion();
    });

    elements.questionGrid.appendChild(button);
  });
}

function toggleStar() {
  const questionState = getQuestionState(state.currentIndex);
  updateQuestionState(state.currentIndex, {
    starred: !questionState.starred,
  });
  renderQuestion();
}

function goToNext() {
  if (state.currentIndex < state.questions.length - 1) {
    state.currentIndex += 1;
    renderQuestion();
  }
}

function goToPrev() {
  if (state.currentIndex > 0) {
    state.currentIndex -= 1;
    renderQuestion();
  }
}

function openDrawer() {
  elements.menuDrawer.classList.add("open");
  elements.menuDrawer.setAttribute("aria-hidden", "false");
}

function closeDrawer() {
  elements.menuDrawer.classList.remove("open");
  elements.menuDrawer.setAttribute("aria-hidden", "true");
}

function resetProgress() {
  if (!confirm("Reset all saved progress?")) {
    return;
  }
  state.progress = {};
  state.currentIndex = 0;
  saveProgress();
  renderQuestion();
}

async function loadQuestions() {
  const response = await fetch(QUESTION_FILE);
  if (!response.ok) {
    throw new Error("Failed to load questions");
  }
  const data = await response.json();
  state.questions = data;
  state.progress = loadProgress();
  renderQuestion();
}

function init() {
  elements.prevButton.addEventListener("click", goToPrev);
  elements.nextButton.addEventListener("click", goToNext);
  elements.starButton.addEventListener("click", toggleStar);
  elements.menuButton.addEventListener("click", openDrawer);
  elements.closeMenu.addEventListener("click", closeDrawer);
  elements.drawerOverlay.addEventListener("click", closeDrawer);
  elements.resetButton.addEventListener("click", resetProgress);

  loadQuestions().catch((error) => {
    elements.questionText.textContent = "Failed to load questions.";
    console.error(error);
  });
}

init();
