function showAlert(message, type) {
  let icon = "info";
  if (type === "success") icon = "success";
  if (type === "danger") icon = "error";
  if (type === "warning") icon = "warning";

  Swal.fire({
    icon: icon,
    title: message,
    timer: 2000,
    showConfirmButton: false
  });
}
