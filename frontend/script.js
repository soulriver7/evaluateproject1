const evaluationForm = document.getElementById("evaluation-form");
const evaluationResult = document.getElementById("evaluation-result");

evaluationForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const studentInfo = {
    name: document.getElementById("student-name").value,
    personality: document.getElementById("personality").value,
    hobbies: document.getElementById("hobbies").value,
    specialties: document.getElementById("specialties").value,
    awards: document.getElementById("awards").value,
  };
  const desiredPath = document.getElementById("desired-path").value;

  fetch("/generate_evaluation", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ studentInfo, desiredPath }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        console.error(data.error);
        evaluationResult.textContent = "평가내역 생성에 오류가 발생했습니다.";
      } else {
        evaluationResult.textContent = data.evaluation;
      }
    })
    .catch((error) => {
      console.error(error);
      evaluationResult.textContent = "서버와의 통신에 실패했습니다.";
    });
});