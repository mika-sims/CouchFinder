// Auto-dismiss the messages after 2 seconds
const autoDismissTime = 2000;
const alerts = document.querySelectorAll('.message');

alerts.forEach(function(alert) {
  setTimeout(function() {
    alert.remove();
  }, autoDismissTime);
});