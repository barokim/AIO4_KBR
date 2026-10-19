"use strict";

// 서버 호출 없이 현재 페이지 안에서 실습을 실행합니다.
function readInteger(input) {
  const value = input.valueAsNumber;
  if (!Number.isSafeInteger(value)) {
    throw new Error("정확히 계산할 수 있는 범위의 정수를 입력하세요 (±9,007,199,254,740,991).");
  }
  return value;
}

function showResult(id, message, error = false) {
  const output = document.getElementById(id);
  output.textContent = message;
  output.closest(".result").classList.toggle("error", error);
}

function bindForm(id, outputId, calculate) {
  document.getElementById(id).addEventListener("submit", (event) => {
    event.preventDefault();
    try {
      calculate(event.currentTarget);
    } catch (error) {
      showResult(outputId, error.message, true);
    }
  });
}

document.querySelectorAll("nav button").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll("nav button").forEach((item) => {
      item.setAttribute("aria-pressed", String(item === button));
    });
    document.querySelectorAll(".exercise").forEach((section) => {
      section.hidden = section.id !== button.dataset.target;
    });
  });
});

bindForm("variables-form", "variables-output", (form) => {
  const first = readInteger(form.elements.first);
  const second = readInteger(form.elements.second);
  const sum = first + second;
  if (!Number.isSafeInteger(sum)) throw new Error("합계가 정확한 정수 계산 범위를 벗어났습니다. 더 작은 값을 입력하세요.");
  showResult("variables-output", `${first} + ${second} = ${sum}`);
});

bindForm("pass-form", "pass-output", (form) => {
  const score = readInteger(form.elements.score);
  showResult("pass-output", `입력한 점수: ${score}점\n${score >= 60 ? "합격" : "불합격"}`);
});

bindForm("even-form", "even-output", (form) => {
  const numbers = ["n1", "n2", "n3", "n4", "n5"].map((name) => readInteger(form.elements[name]));
  const evenNumbers = numbers.filter((number) => number % 2 === 0);
  showResult("even-output", `저장된 숫자: [${numbers.join(", ")}]\n짝수:\n${evenNumbers.length ? evenNumbers.join("\n") : "짝수가 없습니다."}`);
});

document.getElementById("multiplication-run").addEventListener("click", () => {
  const table = document.createElement("table");
  const caption = table.createCaption();
  caption.textContent = "2단부터 9단까지의 구구단";
  const heading = table.createTHead().insertRow();
  for (let dan = 2; dan <= 9; dan++) {
    const cell = document.createElement("th");
    cell.scope = "col";
    cell.textContent = `${dan}단`;
    heading.append(cell);
  }
  const body = table.createTBody();
  for (let multiplier = 1; multiplier <= 9; multiplier++) {
    const row = body.insertRow();
    for (let dan = 2; dan <= 9; dan++) {
      row.insertCell().textContent = `${dan} × ${multiplier} = ${dan * multiplier}`;
    }
  }
  document.getElementById("multiplication-output").replaceChildren(table);
  document.getElementById("multiplication-status").textContent = "9번의 행 반복 × 8번의 열 반복 = 72개의 계산";
});

let secret;
let count;
let score;
let finished;
const gameForm = document.getElementById("game-form");

function resetGame() {
  secret = Math.floor(Math.random() * 100) + 1;
  count = 0;
  score = 100;
  finished = false;
  gameForm.reset();
  gameForm.elements.guess.disabled = false;
  document.getElementById("game-submit").disabled = false;
  document.getElementById("game-count").textContent = "0번";
  document.getElementById("game-score").textContent = "100점";
  const empty = document.createElement("li");
  empty.className = "empty";
  empty.textContent = "아직 입력한 숫자가 없습니다.";
  document.getElementById("game-history").replaceChildren(empty);
  showResult("game-output", "게임이 준비되었습니다. 첫 번째 숫자를 입력하세요.");
}

bindForm("game-form", "game-output", (form) => {
  if (finished) return;
  const guess = readInteger(form.elements.guess);
  if (guess < 1 || guess > 100) throw new Error("1~100 사이의 정수를 입력하세요.");
  count += 1;
  score -= 10;
  const hint = guess > secret ? "컴퓨터보다 큽니다." : guess < secret ? "컴퓨터보다 작습니다." : "정답입니다.";
  const history = document.getElementById("game-history");
  if (count === 1) history.replaceChildren();
  const entry = document.createElement("li");
  entry.textContent = `${guess} → ${hint}`;
  history.append(entry);
  document.getElementById("game-count").textContent = `${count}번`;
  document.getElementById("game-score").textContent = `${score}점`;
  if (guess === secret) {
    finished = true;
    showResult("game-output", `정답입니다! 정답: ${secret}\n총 시도 횟수는: ${count}번입니다.\n최종 점수는: ${score}점입니다.`);
    form.elements.guess.disabled = true;
    document.getElementById("game-submit").disabled = true;
  } else {
    showResult("game-output", `${guess}: ${hint}\n${guess > secret ? "더 작은 숫자를 입력해 보세요." : "더 큰 숫자를 입력해 보세요."}`);
    form.elements.guess.value = "";
    form.elements.guess.focus();
  }
});

document.getElementById("game-reset").addEventListener("click", () => {
  resetGame();
  gameForm.elements.guess.focus();
});
resetGame();
