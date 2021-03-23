// ---- I N I T
function init() {
    console.log("Document ready");

    setTimeout(() => $(".alert-log-reg").slideUp("slow"), 5000);
}

window.onload = init;