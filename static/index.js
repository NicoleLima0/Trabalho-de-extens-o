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
