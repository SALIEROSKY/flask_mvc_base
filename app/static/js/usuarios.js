async function eliminarUsuario(id) {
  if (confirm("¿Seguro que deseas eliminar este usuario?")) {
    const response = await fetch(`/usuarios/${id}`, { method: 'DELETE' });
    const result = await response.json();
    alert(result.mensaje);
    location.reload();
  }
}

function filtrarUsuarios(tipo) {
  const filas = document.querySelectorAll("tbody tr");
  filas.forEach(fila => {
    const badge = fila.querySelector(".badge");
    const esActivo = badge && badge.classList.contains("bg-success");

    fila.style.display =
      tipo === "todos" ||
      (tipo === "activos" && esActivo) ||
      (tipo === "inactivos" && !esActivo)
        ? ""
        : "none";
  });
}
