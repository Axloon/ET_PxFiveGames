function abrirModal(modalId) {
  var modal = document.getElementById("miModal" + modalId);
  if (modal) {
      modal.style.display = "block";
  }
}

function cerrarModal(modalId) {
  var modal = document.getElementById("miModal" + modalId);
  if (modal) {
      modal.style.display = "none";
  }
}