$(document).ready(function () {
	// show automatically after 1s
	setTimeout(showModal, 1000);
	$("#closeBtn").click(function () {
		$("#shopAnnouncementModal").hide();
	});
	function showModal() {
		// get value from localStorage
		var is_modal_show = sessionStorage.getItem("alreadyShown");
		if (is_modal_show != "already shown") {
			$("#shopAnnouncementModal").show();
			sessionStorage.setItem("alreadyShown", "already shown");
		} else {
			console.log(is_modal_show);
		}
	}
});
