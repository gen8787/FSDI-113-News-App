// ---- F L A G   C O M M E N T
flagComment = comment_id => alert(`Comment ${comment_id} has been flagged.`);


// ---- I N I T
function init() {
    console.log("Document ready");

    setTimeout(() => $(".alert-log-reg").slideUp("slow"), 5000);
}

window.onload = init;