// SweetAlert para roles

function eliminarRol(id) {
  Swal.fire({
    title: '¿Eliminar rol?',
    text: "Esta acción no se puede deshacer.",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonText: 'Sí, eliminar',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.isConfirmed) {
      fetch(`/api/roles/${id}`, { method: 'DELETE' })
        .then(res => res.json())
        .then(data => {
          if (data.mensaje) {
            Swal.fire('Resultado', data.mensaje, 'info')
              .then(() => location.reload());
          }
        })
        .catch(() => Swal.fire('Error', 'No se pudo eliminar el rol.', 'error'));
    }
  });
}

function confirmarAccionRol(event, mensaje) {
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
