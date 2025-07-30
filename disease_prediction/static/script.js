
document.addEventListener("DOMContentLoaded", () => {
  const modelBtn = document.getElementById("modelButton");
  const modelDropdown = document.getElementById("modelDropdown");

  modelBtn.addEventListener("click", (e) => {
    e.preventDefault(); 
    modelDropdown.classList.toggle("show");
  });

  document.addEventListener("click", (e) => {
    if (!modelBtn.contains(e.target) && !modelDropdown.contains(e.target)) {
      modelDropdown.classList.remove("show");
    }
  });
});



