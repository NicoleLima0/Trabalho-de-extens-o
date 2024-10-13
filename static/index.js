const openModalBtn = document.getElementById("open-modal-btn");
const closeModalBtn = document.getElementById("close-modal-btn");
const modal = document.getElementById("animal-modal");

openModalBtn &&
  openModalBtn.addEventListener("click", () => {
    modal.style.display = "flex";
  });

closeModalBtn &&
  closeModalBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

window.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
});

document.querySelectorAll(".remove-animal-btn").forEach((btn) => {
  btn.addEventListener("click", function () {
    const animalCard = this.closest(".animal-card");
    const animalName = animalCard.getAttribute("data-animal-name");
    fetch(`/remover-animal`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: animalName }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          animalCard.remove();
        } else {
          alert("Erro ao remover o animal.");
        }
      })
      .catch((error) => {
        console.error("Erro:", error);
        alert("Erro ao remover o animal.");
      });
  });
});
