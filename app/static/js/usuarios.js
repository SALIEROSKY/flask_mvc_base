// Filtrar usuarios por estado
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

// Confirmar eliminación
function eliminarUsuario(id) {
  Swal.fire({
    title: '¿Eliminar usuario?',
    text: "Esta acción no se puede deshacer.",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonText: 'Sí, eliminar',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.isConfirmed) {
      fetch(`/usuarios/${id}`, { method: 'DELETE' })
        .then(res => res.json())
        .then(data => {
          Swal.fire('Eliminado', data.mensaje, 'success')
            .then(() => location.reload());
        })
        .catch(() => Swal.fire('Error', 'No se pudo eliminar el usuario.', 'error'));
    }
  });
}

// Confirmar creación o edición
function confirmarAccion(event, mensaje) {
  event.preventDefault();
  Swal.fire({
    title: mensaje,
    icon: 'question',
    showCancelButton: true,
    confirmButtonText: 'Sí, continuar',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.isConfirmed) {
      event.target.submit();
    }
  });
}
